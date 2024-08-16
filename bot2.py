import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv('BOT_TOKEN', '7152066894:AAGkTh2QLFNMSF7Z5dJdfj7IDjcDcDPoKnM')

questions = [
    {
        "question": "1. Какой элемент HTML используется для добавления заголовка страницы? 📑",
        "options": ["<header>", "<title>", "<h1>", "<meta>"],
        "correct_option_id": 1,
        "explanation": "Элемент <title> задает заголовок страницы, который отображается на вкладке браузера и помогает пользователям понять содержание страницы."
    },
    {
        "question": "2. Какой элемент HTML используется для создания гиперссылок? 🔗",
        "options": ["<a>", "<link>", "<button>", "<url>"],
        "correct_option_id": 0,
        "explanation": "Элемент <a> используется для создания ссылок, позволяя пользователям переходить на другие страницы или ресурсы."
    },
    {
        "question": "3. Какой атрибут HTML используется для открытия ссылки в новой вкладке? 🆕",
        "options": ["target=\"_self\"", "target=\"_top\"", "target=\"_blank\"", "target=\"_parent\""],
        "correct_option_id": 2,
        "explanation": "Атрибут target=\"_blank\" открывает ссылку в новой вкладке, сохраняя текущую страницу открытой."
    },
    {
        "question": "4. Какой элемент HTML используется для вставки изображения? 🖼",
        "options": ["<img>", "<picture>", "<photo>", "<image>"],
        "correct_option_id": 0,
        "explanation": "Элемент <img> вставляет изображения на веб-страницу, улучшая визуальное представление информации."
    },
    {
        "question": "5. Что указывает атрибут alt в теге <img>? 📝",
        "options": ["Размер изображения", "URL изображения", "Альтернативный текст для изображения", "Выравнивание изображения"],
        "correct_option_id": 2,
        "explanation": "Атрибут alt предоставляет текстовое описание изображения, которое отображается, если изображение не загрузилось или если доступ к нему ограничен."
    },
    {
        "question": "6. Какой элемент HTML используется для создания списка с маркерами? 📋",
        "options": ["<ul>", "<ol>", "<list>", "<item>"],
        "correct_option_id": 0,
        "explanation": "Элемент <ul> создает ненумерованный список с маркерами."
    },
    {
        "question": "7. Какой элемент HTML используется для создания списка с нумерацией? 🔢",
        "options": ["<ol>", "<ul>", "<list>", "<item>"],
        "correct_option_id": 0,
        "explanation": "Элемент <ol> создает нумерованный список, где пункты упорядочены."
    },
    {
        "question": "8. Какой элемент HTML используется для добавления текста под изображением? 📝",
        "options": ["<figcaption>", "<caption>", "<text>", "<description>"],
        "correct_option_id": 0,
        "explanation": "Элемент <figcaption> добавляет подпись к изображению, объясняя, что изображено на картинке."
    },
    {
        "question": "9. Какой элемент HTML используется для создания раздела на странице? 🗂",
        "options": ["<section>", "<div>", "<article>", "<header>"],
        "correct_option_id": 0,
        "explanation": "Элемент <section> создает отдельный раздел на странице, организуя контент в логические блоки."
    },
    {
        "question": "10. Какой элемент HTML используется для горизонтальной линии? 🌐",
        "options": ["<hr>", "<line>", "<divider>", "<break>"],
        "correct_option_id": 0,
        "explanation": "Элемент <hr> создает горизонтальную линию для разделения содержимого."
    },
    {
        "question": "11. Какое CSS-свойство задает цвет фона элемента? 🌈",
        "options": ["color", "background-color", "border-color", "text-color"],
        "correct_option_id": 1,
        "explanation": "Свойство background-color устанавливает цвет фона элемента."
    },
    {
        "question": "12. Какое CSS-свойство используется для установки шрифта текста? 🔠",
        "options": ["font-size", "font-family", "text-align", "line-height"],
        "correct_option_id": 1,
        "explanation": "Свойство font-family задает шрифт текста."
    },
    {
        "question": "13. Какое CSS-свойство используется для задания максимальной ширины элемента? 📏",
        "options": ["width", "max-height", "max-width", "height"],
        "correct_option_id": 2,
        "explanation": "Свойство max-width задает максимальную ширину элемента."
    },
    {
        "question": "14. Какое CSS-свойство задает внутренние отступы элемента? ⛓",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 1,
        "explanation": "Свойство padding устанавливает внутренние отступы элемента."
    },
    {
        "question": "15. Какое CSS-свойство управляет выравниванием текста? 📝",
        "options": ["text-decoration", "text-align", "font-style", "vertical-align"],
        "correct_option_id": 1,
        "explanation": "Свойство text-align управляет выравниванием текста."
    },
    {
        "question": "16. Какое CSS-свойство используется для установки стиля границы элемента? 🖊",
        "options": ["border", "border-width", "border-color", "border-radius"],
        "correct_option_id": 0,
        "explanation": "Свойство border устанавливает стиль границы элемента."
    },
    {
        "question": "17. Какое CSS-свойство задает размер шрифта текста? 📏",
        "options": ["font-family", "font-size", "text-align", "margin"],
        "correct_option_id": 1,
        "explanation": "Свойство font-size задает размер шрифта текста."
    },
    {
        "question": "18. Какое CSS-свойство задает отступы между элементами? ⬆️⬇️⬅️➡️",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 0,
        "explanation": "Свойство margin задает отступы между элементами."
    },
    {
        "question": "19. Какое CSS-свойство изменяет стиль ссылок при наведении курсора? 🖱",
        "options": ["color", "a:hover", "text-decoration", "border"],
        "correct_option_id": 1,
        "explanation": "Псевдокласс a:hover изменяет стиль ссылок при наведении курсора."
    },
    {
        "question": "20. Какой элемент HTML используется для определения основной части документа? 📝",
        "options": ["<main>", "<section>", "<div>", "<article>"],
        "correct_option_id": 0,
        "explanation": "Элемент <main> определяет основную часть документа."
    }
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Выберите ваше имя", callback_data='select_name')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! 👋 Чтобы начать, выбери, пожалуйста, свое имя. 😊', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    context.user_data['name'] = query.data
    context.user_data['gender'] = query.data.split()[1]  # Assuming name and gender are separated by a space
    context.user_data['current_question'] = 0
    context.user_data['score'] = 0
    context.user_data['answers'] = []
    
    greeting = "Давайте начнем повторение по HTML и CSS. Успехов! 🌟"
    
    if context.user_data['gender'] == 'female':
        greeting = "Давайте начнем повторение по HTML и CSS. Успехов! 🌟"
    else:
        greeting = "Давайте начнем повторение по HTML и CSS. Успехов! 🌟"
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Привет, {context.user_data['name']}! {greeting}")
    await ask_question(update, context)

async def ask_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question_id = context.user_data['current_question']
    
    if question_id >= len(questions):
        score = context.user_data['score']
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Повторение окончено! Ваш балл: {score}/{len(questions)}. Успехов в дальнейшем! 🎉")
        return
    
    question = questions[question_id]
    text = question['question'] + "\n" + "\n".join([f"{chr(97 + i)}) {opt}" for i, opt in enumerate(question['options'])])
    keyboard = [[InlineKeyboardButton(opt, callback_data=str(i))] for i in range(len(question['options']))]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    question_id = context.user_data['current_question']
    selected_option = int(query.data)
    
    correct_option_id = questions[question_id]['correct_option_id']
    if selected_option == correct_option_id:
        context.user_data['score'] += 1
        await query.edit_message_text(text="Правильно! ✅")
    else:
        explanation = questions[question_id]['explanation']
        await query.edit_message_text(text=f"Неправильно. ❌ Правильный ответ: {questions[question_id]['options'][correct_option_id]}.\n{explanation}")
    
    context.user_data['current_question'] += 1
    await ask_question(update, context)

async def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CallbackQueryHandler(handle_answer))

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
