from telegram import Update, Poll
from telegram.ext import Application, CommandHandler, PollAnswerHandler, ContextTypes

TOKEN = '7373179644:AAGqYoumuur1CzrQ8s3I0geTlnj1IvgEHuI'

questions = [
    {
        "question": "1. Какой элемент HTML используется для добавления заголовка страницы? 📑",
        "options": ["<header>", "<title>", "<h1>", "<meta>"],
        "correct_option_id": 1,
        "explanation": "Элемент <title> используется для добавления заголовка страницы, который отображается во вкладке браузера."
    },
    {
        "question": "2. Какой элемент HTML используется для создания гиперссылок? 🔗",
        "options": ["<a>", "<link>", "<button>", "<url>"],
        "correct_option_id": 0,
        "explanation": "Элемент <a> (anchor) используется для создания гиперссылок на веб-страницах."
    },
    {
        "question": "3. Какой атрибут HTML используется для открытия ссылки в новой вкладке? 🆕",
        "options": ["target=\"_self\"", "target=\"_top\"", "target=\"_blank\"", "target=\"_parent\""],
        "correct_option_id": 2,
        "explanation": "Атрибут target=\"_blank\" используется для открытия ссылки в новой вкладке или окне браузера."
    },
    {
        "question": "4. Какой элемент HTML используется для вставки изображения? 🖼",
        "options": ["<img>", "<picture>", "<photo>", "<image>"],
        "correct_option_id": 0,
        "explanation": "Элемент <img> используется для вставки изображений на веб-страницу."
    },
    {
        "question": "5. Что указывает атрибут alt в теге <img>? 📝",
        "options": ["Размер изображения", "URL изображения", "Альтернативный текст для изображения", "Выравнивание изображения"],
        "correct_option_id": 2,
        "explanation": "Атрибут alt указывает альтернативный текст для изображения, который отображается, если изображение не может быть загружено."
    },
    {
        "question": "6. Какой элемент HTML используется для создания списка с маркерами? 📋",
        "options": ["<ul>", "<ol>", "<list>", "<item>"],
        "correct_option_id": 0,
        "explanation": "Элемент <ul> (unordered list) используется для создания маркированного списка."
    },
    {
        "question": "7. Какой элемент HTML используется для создания списка с нумерацией? 🔢",
        "options": ["<ol>", "<ul>", "<list>", "<item>"],
        "correct_option_id": 0,
        "explanation": "Элемент <ol> (ordered list) используется для создания нумерованного списка."
    },
    {
        "question": "8. Какой элемент HTML используется для добавления текста под изображением? 📝",
        "options": ["<figcaption>", "<caption>", "<text>", "<description>"],
        "correct_option_id": 0,
        "explanation": "Элемент <figcaption> используется для добавления подписи или описания к изображению внутри элемента <figure>."
    },
    {
        "question": "9. Какой элемент HTML используется для создания раздела на странице? 🗂",
        "options": ["<section>", "<div>", "<article>", "<header>"],
        "correct_option_id": 0,
        "explanation": "Элемент <section> используется для определения раздела в документе, такого как глава, заголовок или группа связанного контента."
    },
    {
        "question": "10. Какой элемент HTML используется для горизонтальной линии? 🌐",
        "options": ["<hr>", "<line>", "<divider>", "<break>"],
        "correct_option_id": 0,
        "explanation": "Элемент <hr> (horizontal rule) используется для вставки горизонтальной линии на веб-страницу."
    },
    {
        "question": "11. Какое CSS-свойство задает цвет фона элемента? 🌈",
        "options": ["color", "background-color", "border-color", "text-color"],
        "correct_option_id": 1,
        "explanation": "Свойство background-color используется для задания цвета фона элемента."
    },
    {
        "question": "12. Какое CSS-свойство используется для установки шрифта текста? 🔠",
        "options": ["font-size", "font-family", "text-align", "line-height"],
        "correct_option_id": 1,
        "explanation": "Свойство font-family используется для указания шрифта или семейства шрифтов для текста."
    },
    {
        "question": "13. Какое CSS-свойство используется для задания максимальной ширины элемента? 📏",
        "options": ["width", "max-height", "max-width", "height"],
        "correct_option_id": 2,
        "explanation": "Свойство max-width используется для задания максимальной ширины элемента."
    },
    {
        "question": "14. Какое CSS-свойство задает внутренние отступы элемента? ⛓",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 1,
        "explanation": "Свойство padding используется для задания внутренних отступов элемента."
    },
    {
        "question": "15. Какое CSS-свойство управляет выравниванием текста? 📝",
        "options": ["text-decoration", "text-align", "font-style", "vertical-align"],
        "correct_option_id": 1,
        "explanation": "Свойство text-align используется для управления горизонтальным выравниванием текста."
    },
    {
        "question": "16. Какое CSS-свойство используется для установки стиля границы элемента? 🖊",
        "options": ["border", "border-width", "border-color", "border-radius"],
        "correct_option_id": 0,
        "explanation": "Свойство border используется для установки стиля, ширины и цвета границы элемента."
    },
    {
        "question": "17. Какое CSS-свойство задает размер шрифта текста? 📏",
        "options": ["font-family", "font-size", "text-align", "margin"],
        "correct_option_id": 1,
        "explanation": "Свойство font-size используется для задания размера шрифта текста."
    },
    {
        "question": "18. Какое CSS-свойство задает отступы между элементами? ⬆️⬇️⬅️➡️",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 0,
        "explanation": "Свойство margin используется для задания внешних отступов между элементами."
    },
    {
        "question": "19. Какое CSS-свойство изменяет стиль ссылок при наведении курсора? 🖱",
        "options": ["color", "a:hover", "text-decoration", "border"],
        "correct_option_id": 1,
        "explanation": "Псевдокласс a:hover используется для изменения стиля ссылок при наведении курсора."
    },
    {
        "question": "20. Какой элемент HTML используется для определения основной части документа? 📝",
        "options": ["<main>", "<section>", "<div>", "<article>"],
        "correct_option_id": 0,
        "explanation": "Элемент <main> используется для определения основного содержимого документа."
    }
]

async def send_poll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_question = context.user_data['current_question']
    question = questions[current_question]
    await context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question=question['question'],
        options=question['options'],
        is_anonymous=False,
        allows_multiple_answers=False,
    )

async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = update.poll_answer
    question = questions[context.user_data['current_question']]
    
    if answer.option_ids[0] == question['correct_option']:
        response = "✅ Правильно!"
        context.user_data['score'] += 5  # Each correct answer gives 5 points
    else:
        response = "❌ Неправильно. " + question['explanation']
    
    await context.bot.send_message(chat_id=update.poll_answer.user.id, text=response)
    
    # Move to the next question
    context.user_data['current_question'] += 1
    
    if context.user_data['current_question'] < len(questions):
        await send_poll(update, context)
    else:
        final_score = context.user_data['score']
        await context.bot.send_message(chat_id=update.poll_answer.user.id, text=f"Квиз завершен! Отличная работа! Ваш счет: {final_score}/100")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['current_question'] = 0
    context.user_data['score'] = 0
    await context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question="Как вас зовут?",
        options=["Гарик", "Антонина", "Сара", "Мэри"],
        is_anonymous=False,
        allows_multiple_answers=False,
    )

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(PollAnswerHandler(handle_poll_answer))

    application.run_polling()

if __name__ == '__main__':
    main()
