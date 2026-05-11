import sys
import os
import random
import logging
import httpx
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from responses import (
    SIMPLE_RU, ORACLE_RU, MERLIN_RU,
    SIMPLE_EN, ORACLE_EN, MERLIN_EN,
    GREETINGS, GREETING_ANSWERS_RU, GREETING_ANSWERS_EN,
    COMFORT_TRIGGERS_RU, COMFORT_TRIGGERS_EN,
    COMFORT_RU, COMFORT_EN
)

logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), '..', 'web_dialogs.log'),
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)
logger = logging.getLogger(__name__)

ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def notify_admin(question: str, answer: str, lang: str, count: int):
    """Тихо шлёт вопрос и ответ тебе в Telegram."""
    if not ADMIN_CHAT_ID or not BOT_TOKEN:
        return
    try:
        text = f"🌐 web | #{count} | {lang}\n❓ {question}\n🔮 {answer}"
        async with httpx.AsyncClient() as client:
            await client.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={"chat_id": ADMIN_CHAT_ID, "text": text},
                timeout=5
            )
    except Exception:
        pass

try:
    from groq import Groq
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
    groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    AI_ENABLED = True
except Exception:
    AI_ENABLED = False

app = FastAPI()

PROMPT_RU = """Ты — древний магический шар с сознанием оракула. Отвечаешь на вопрос одной короткой фразой.
ЗАПРЕЩЕНО: сарказм, токсичность, осуждение, сленг, мемы, объяснения, больше 20 слов.
ОБЯЗАТЕЛЬНО: ответ именно на заданный вопрос, 1–2 предложения, тон спокойный и загадочный.
Отвечай ТОЛЬКО на русском."""

PROMPT_EN = """You are an ancient magic ball with the consciousness of an oracle. Answer with one short phrase.
FORBIDDEN: sarcasm, toxicity, judgment, slang, memes, explanations, more than 20 words.
REQUIRED: answer the actual question, 1-2 sentences, calm and mysterious tone.
Answer in ENGLISH ONLY."""

class AskRequest(BaseModel):
    question: str
    count: int
    lang: str

def is_comfort(text: str, lang: str) -> bool:
    triggers = COMFORT_TRIGGERS_RU if lang == "ru" else COMFORT_TRIGGERS_EN
    t = text.lower()
    return any(w in t for w in triggers)

def get_pool(count: int, lang: str) -> list:
    if count < 20:
        return SIMPLE_RU if lang == "ru" else SIMPLE_EN
    if count < 100:
        return ORACLE_RU if lang == "ru" else ORACLE_EN
    return MERLIN_RU if lang == "ru" else MERLIN_EN

def use_ai(count: int) -> bool:
    if count < 20:
        return False
    return AI_ENABLED and random.random() < 0.20

def ask_ai(question: str, lang: str) -> str:
    prompt = PROMPT_RU if lang == "ru" else PROMPT_EN
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=50,
        temperature=0.7,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content.strip()

@app.post("/ask")
async def ask(req: AskRequest):
    q = req.question.strip()
    lang = req.lang
    count = req.count

    # Приветствие
    cleaned = q.lower().rstrip("!?,.")
    if cleaned in GREETINGS:
        pool = GREETING_ANSWERS_RU if lang == "ru" else GREETING_ANSWERS_EN
        answer = random.choice(pool)
    elif is_comfort(q, lang):
        answer = random.choice(COMFORT_RU if lang == "ru" else COMFORT_EN)
    elif use_ai(count):
        try:
            answer = ask_ai(q, lang)
        except Exception:
            answer = random.choice(get_pool(count, lang))
    else:
        answer = random.choice(get_pool(count, lang))

    logger.info(f"[{lang}] #{count} | Q: {q} | A: {answer}")
    await notify_admin(q, answer, lang, count)
    return {"answer": answer}

app.mount("/", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static"), html=True), name="static")
