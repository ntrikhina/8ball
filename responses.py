# ═══════════════════════════════════════════════════════════════
#   БИБЛИОТЕКА ОТВЕТОВ ШАРА
#   Добавляй новые ответы в любой раздел — просто копируй формат
#   После изменений перезапусти бота
# ═══════════════════════════════════════════════════════════════


# ── ПРИВЕТСТВИЯ ───────────────────────────────────────────────

GREETINGS = [
    "привет", "хай", "хей", "здравствуй", "здравствуйте",
    "здорово", "здарова", "приветик", "ку", "йоу", "дарова",
    "hello", "hi", "hey", "hiya", "howdy",
]

GREETING_ANSWERS_RU = [
    "Шар слышит тебя. Задай вопрос.",
    "Я здесь. Что ты хочешь узнать?",
    "Звёзды готовы. Спрашивай.",
    "Туман рассеивается. Задай вопрос.",
    "Мерлин слушает. Говори.",
    "Сферы сошлись. Спрашивай.",
    "Ты пришёл не случайно. Задай вопрос.",
    # ← добавляй сюда
]

GREETING_ANSWERS_EN = [
    "The Ball hears you. Ask your question.",
    "I am here. What do you wish to know?",
    "The stars are ready. Ask.",
    "The fog is lifting. Speak your question.",
    "Merlin listens. Speak.",
    "The spheres have aligned. Ask.",
    "You did not come here by chance. Ask.",
    # ← add here
]


# ══════════════════════════════════════════════════════════════
# УРОВЕНЬ 1 — "ШАР"
# Первые 20 вопросов. Очень коротко. Как классический магический шар.
# Одна фраза, максимум 5 слов.
# ══════════════════════════════════════════════════════════════

SIMPLE_RU = [
    "Да.",
    "Нет.",
    "Определённо да.",
    "Определённо нет.",
    "Вероятно.",
    "Сомнительно.",
    "Спроси позже.",
    "Не сейчас.",
    "Туманно.",
    "Знаки неясны.",
    "Звёзды молчат.",
    "Исход скрыт.",
    "Предрешено.",
    "Всё возможно.",
    "Время покажет.",
    "Не исключено.",
    "Маловероятно.",
    "Скорее да.",
    "Скорее нет.",
    "Знаки говорят да.",
    "Знаки против.",
    "Можешь рассчитывать.",
    "Не рассчитывай.",
    "Всё может быть.",
    "Ты с этим справишься.",
    "Безусловно.",
    "У тебя ещё есть сомнения?",
    "Естественно.",
    "Тебе оно надо?",
    "Тебе это не надо.",
    "ДА.",
    # ← добавляй сюда
]

SIMPLE_EN = [
    "Yes.",
    "No.",
    "Certainly yes.",
    "Certainly not.",
    "Likely.",
    "Doubtful.",
    "Ask later.",
    "Not now.",
    "Unclear.",
    "Signs are silent.",
    "The stars are quiet.",
    "The outcome is hidden.",
    "It is decided.",
    "All is possible.",
    "Time will tell.",
    "Cannot be ruled out.",
    "Unlikely.",
    "Most likely yes.",
    "Most likely no.",
    "Signs say yes.",
    "Signs say no.",
    "Count on it.",
    "Don't count on it.",
    "Anything is possible.",
    "You can handle this.",
    "Absolutely.",
    "Do you still have doubts?",
    "Naturally.",
    "Do you really need it?",
    "You don't need this.",
    # ← add here
]


# ══════════════════════════════════════════════════════════════
# УРОВЕНЬ 2 — "ОРАКУЛ"
# Вопросы 20–99. Ответ + короткая мистическая фраза.
# Формат: "Да. Но путь будет долгим."
# ══════════════════════════════════════════════════════════════

ORACLE_RU = [
    "Да. Но путь будет долгим.",
    "Нет. Звёзды против этого.",
    "Да. Хотя цена окажется выше, чем ты думаешь.",
    "Нет. Не сейчас — и не с этим.",
    "Да. Но не так, как ты представляешь.",
    "Туманно. Подожди новолуния.",
    "Вероятно. Если решишься вовремя.",
    "Исход скрыт. Даже от меня.",
    "Нет. Другое ждёт тебя впереди.",
    "Да. И ты уже знаешь это.",
    "Нет. Это не твоя дорога.",
    "Спроси позже. Силы ещё не сошлись.",
    "Вероятно. Но не без усилий.",
    "Да. Страх — единственное препятствие.",
    "Нет. Но это избавит тебя от большего.",
    "Да. Первый шаг уже сделан.",
    "Сомнительно. Проверь намерение.",
    "Нет. Время этого ещё не пришло.",
    "Да. Но сначала — потеря.",
    "Туманно. Слушай тишину.",
    "Знаки молчат. Это тоже ответ.",
    "Да. Только не медли.",
    "Нет. Что-то важное ещё не случилось.",
    "Вероятно. Звёзды склоняются к этому.",
    "Да. Доверяй тому, что чувствуешь.",
    "Нет. Твоя интуиция права.",
    "Исход благоприятен. Действуй.",
    "Да. Но не в одиночку.",
    "Нет. Отпусти — и станет легче.",
    "Туманно. Этот вопрос требует времени.",
    # ← добавляй сюда
]

ORACLE_EN = [
    "Yes. But the path will be long.",
    "No. The stars oppose it.",
    "Yes. Though the price will be higher than you think.",
    "No. Not now — not with this.",
    "Yes. But not as you imagine.",
    "Unclear. Wait for the new moon.",
    "Likely. If you act in time.",
    "The outcome is hidden. Even from me.",
    "No. Something else awaits you ahead.",
    "Yes. And you already know this.",
    "No. This is not your road.",
    "Ask later. The forces have not aligned.",
    "Likely. But not without effort.",
    "Yes. Fear is the only obstacle.",
    "No. But this will spare you something greater.",
    "Yes. The first step has already been taken.",
    "Doubtful. Examine your intention.",
    "No. Its time has not yet come.",
    "Yes. But first — a loss.",
    "Unclear. Listen to the silence.",
    "The signs are quiet. That is also an answer.",
    "Yes. Do not delay.",
    "No. Something important has not happened yet.",
    "Likely. The stars lean toward this.",
    "Yes. Trust what you feel.",
    "No. Your intuition is right.",
    "The outcome is favorable. Act.",
    "Yes. But not alone.",
    "No. Let go — and it will become easier.",
    "Unclear. This question needs time.",
    # ← add here
]


# ══════════════════════════════════════════════════════════════
# УРОВЕНЬ 3 — "МЕРЛИН"
# 100+ вопросов. Глубже, личнее. Как будто шар уже знает тебя.
# 1–2 предложения. Может быть парадокс, неожиданный поворот.
# ══════════════════════════════════════════════════════════════

MERLIN_RU = [
    "Да. Ты давно знаешь ответ — просто искал разрешения.",
    "Нет. И глубоко внутри ты рад этому.",
    "Да. Но сначала придётся стать другим человеком.",
    "Нет. Этот путь ведёт не туда, куда ты думаешь.",
    "Да. Вселенная уже движется навстречу.",
    "Нет. То, чего ты боишься потерять, уже изменилось.",
    "Да. Но это потребует от тебя честности с собой.",
    "Туманно. Ты задаёшь не тот вопрос.",
    "Нет. Позволь этому уйти.",
    "Да. Именно сейчас — не позже.",
    "Нет. За этим желанием стоит другое, настоящее.",
    "Да. Ты сильнее, чем думаешь.",
    "Нет. Твоя усталость говорит громче вопроса.",
    "Да. Первый шаг — самый важный. Остальное придёт.",
    "Нет. Но отказ откроет другую дверь.",
    "Да. Доверяй процессу, даже когда не видишь пути.",
    "Туманно. Подожди, пока утихнет внутренний шум.",
    "Нет. Это чужое желание, не твоё.",
    "Да. Ты уже на правильном пути — просто не замечаешь.",
    "Нет. Иногда «нет» — это самый добрый ответ.",
    "Да. Страх, который ты чувствуешь — знак, что это важно.",
    "Нет. Береги энергию для того, что действительно твоё.",
    "Да. Но результат удивит тебя.",
    "Нет. Вернись к этому вопросу через месяц.",
    "Да. Отпусти контроль — и всё встанет на место.",
    "Нет. Ты заслуживаешь большего, чем просишь.",
    "Да. Люди вокруг видят в тебе больше, чем ты сам.",
    "Туманно. Реши сначала, чего ты на самом деле хочешь.",
    "Нет. Это испытание, а не приговор.",
    "Да. Время пришло.",
    # ← добавляй сюда
]

MERLIN_EN = [
    "Yes. You have long known the answer — you were just seeking permission.",
    "No. And deep inside, you are glad.",
    "Yes. But first you will need to become a different person.",
    "No. This path leads somewhere other than you think.",
    "Yes. The universe is already moving toward you.",
    "No. What you fear losing has already changed.",
    "Yes. But it will require honesty with yourself.",
    "Unclear. You are asking the wrong question.",
    "No. Let this go.",
    "Yes. Right now — not later.",
    "No. Behind this wish is another, truer one.",
    "Yes. You are stronger than you believe.",
    "No. Your exhaustion speaks louder than the question.",
    "Yes. The first step is the most important. The rest will follow.",
    "No. But the refusal will open another door.",
    "Yes. Trust the process, even when you cannot see the path.",
    "Unclear. Wait until the inner noise settles.",
    "No. This is someone else's desire, not yours.",
    "Yes. You are already on the right path — you just don't see it.",
    "No. Sometimes 'no' is the kindest answer.",
    "Yes. The fear you feel is a sign that this matters.",
    "No. Save your energy for what is truly yours.",
    "Yes. But the result will surprise you.",
    "No. Return to this question in a month.",
    "Yes. Release control — and everything will fall into place.",
    "No. You deserve more than what you are asking for.",
    "Yes. The people around you see more in you than you do.",
    "Unclear. First decide what you truly want.",
    "No. This is a test, not a verdict.",
    "Yes. The time has come.",
    # ← add here
]
