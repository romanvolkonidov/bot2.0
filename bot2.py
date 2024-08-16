import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv('BOT_TOKEN', '7152066894:AAGkTh2QLFNMSF7Z5dJdfj7IDjcDcDPoKnM')

questions = [
    {
        "question": "1. Какой элемент HTML используется для добавления заголовка страницы? 📑",
        "options": ["<header>", "<title>", "<h1>", "<meta>"],
        "correct_option_id": 1,
        "comment": "Элемент <title> используется для определения заголовка документа, который отображается в заголовке окна браузера."
    },
    {
        "question": "2. Какой элемент HTML используется для создания гиперссылок? 🔗",
        "options": ["<a>", "<link>", "<button>", "<url>"],
        "correct_option_id": 0,
        "comment": "Элемент <a> используется для создания гиперссылок, которые позволяют переходить на другие страницы или ресурсы."
    },
    {
        "question": "3. Какой атрибут HTML используется для открытия ссылки в новой вкладке? 🆕",
        "options": ["target=\"_self\"", "target=\"_top\"", "target=\"_blank\"", "target=\"_parent\""],
        "correct_option_id": 2,
        "comment": "Атрибут target=\"_blank\" используется для открытия ссылки в новой вкладке браузера."
    },
    {
        "question": "4. Какой элемент HTML используется для вставки изображения? 🖼",
        "options": ["<img>", "<picture>", "<photo>", "<image>"],
        "correct_option_id": 0,
        "comment": "Элемент <img> используется для вставки изображений в HTML-документ."
    },
    {
        "question": "5. Что указывает атрибут alt в теге <img>? 📝",
        "options": ["Размер изображения", "URL изображения", "Альтернативный текст для изображения", "Выравнивание изображения"],
        "correct_option_id": 2,
        "comment": "Атрибут alt указывает альтернативный текст для изображения, который отображается, если изображение не может быть загружено."
    },
    {
        "question": "6. Какой элемент HTML используется для создания списка с маркерами? 📋",
        "options": ["<ul>", "<ol>", "<list>", "<item>"],
        "correct_option_id": 0,
        "comment": "Элемент <ul> используется для создания неупорядоченных списков с маркерами."
    },
    {
        "question": "7. Какой элемент HTML используется для создания списка с нумерацией? 🔢",
        "options": ["<ol>", "<ul>", "<list>", "<item>"],
        "correct_option_id": 0,
        "comment": "Элемент <ol> используется для создания упорядоченных списков с нумерацией."
    },
    {
        "question": "8. Какой элемент HTML используется для добавления текста под изображением? 📝",
        "options": ["<figcaption>", "<caption>", "<text>", "<description>"],
        "correct_option_id": 0,
        "comment": "Элемент <figcaption> используется для добавления подписи к изображению."
    },
    {
        "question": "9. Какой элемент HTML используется для создания раздела на странице? 🗂",
        "options": ["<section>", "<div>", "<article>", "<header>"],
        "correct_option_id": 0,
        "comment": "Элемент <section> используется для создания разделов на веб-странице."
    },
    {
        "question": "10. Какой элемент HTML используется для горизонтальной линии? 🌐",
        "options": ["<hr>", "<line>", "<divider>", "<break>"],
        "correct_option_id": 0,
        "comment": "Элемент <hr> используется для вставки горизонтальной линии, которая визуально разделяет контент."
    },
    {
        "question": "11. Какое CSS-свойство задает цвет фона элемента? 🌈",
        "options": ["color", "background-color", "border-color", "text-color"],
        "correct_option_id": 1,
        "comment": "Свойство background-color используется для задания цвета фона элемента."
    },
    {
        "question": "12. Какое CSS-свойство используется для установки шрифта текста? 🔠",
        "options": ["font-size", "font-family", "text-align", "line-height"],
        "correct_option_id": 1,
        "comment": "Свойство font-family используется для задания шрифта текста."
    },
    {
        "question": "13. Какое CSS-свойство используется для задания максимальной ширины элемента? 📏",
        "options": ["width", "max-height", "max-width", "height"],
        "correct_option_id": 2,
        "comment": "Свойство max-width используется для задания максимальной ширины элемента."
    },
    {
        "question": "14. Какое CSS-свойство задает внутренние отступы элемента? ⛓",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 1,
        "comment": "Свойство padding используется для задания внутренних отступов элемента."
    },
    {
        "question": "15. Какое CSS-свойство управляет выравниванием текста? 📝",
        "options": ["text-decoration", "text-align", "font-style", "vertical-align"],
        "correct_option_id": 1,
        "comment": "Свойство text-align используется для управления выравниванием текста."
    },
    {
        "question": "16. Какое CSS-свойство используется для установки стиля границы элемента? 🖊",
        "options": ["border", "border-width", "border-color", "border-radius"],
        "correct_option_id": 0,
        "comment": "Свойство border используется для задания стиля границы элемента."
    },
    {
        "question": "17. Какое CSS-свойство задает размер шрифта текста? 📏",
        "options": ["font-family", "font-size", "text-align", "margin"],
        "correct_option_id": 1,
        "comment": "Свойство font-size используется для задания размера шрифта текста."
    },
    {
        "question": "18. Какое CSS-свойство задает отступы между элементами? ⬆️⬇️⬅️➡️",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 0,
        "comment": "Свойство margin используется для задания отступов между элементами."
    },
    {
        "question": "19. Какое CSS-свойство изменяет стиль ссылок при наведении курсора? 🖱",
        "options": ["color", "a:hover", "text-decoration", "border"],
        "correct_option_id": 1,
        "comment": "Селектор a:hover используется для изменения стиля ссылок при наведении курсора."
    },
    {
        "question": "20. Какой элемент HTML используется для определения основной части документа? 📝",
        "options": ["<main>", "<section>", "<div>", "<article>"],
        "correct_option_id": 0,
        "comment": "Элемент <main> используется для определения основной части документа."
    }
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['current_question'] = 0
    context.user_data['score'] = 0
    context.user_data['answers'] = []
    context.user_data['name'] = update.effective_user.first_name

    await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_question = context.user_data['current_question']
    question = questions[current_question]

    keyboard = [
        [InlineKeyboardButton(option, callback_data=str(i)) for i, option in enumerate(question['options'])]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(question['question'], reply_markup=reply_markup)

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    selected_option = int(query.data)
    current_question = context.user_data['current_question']
    question = questions[current_question]

    context.user_data['answers'].append((question['question'], question['options'][selected_option], question['options'][question['correct_option_id']], question['comment']))
    
    if selected_option == question['correct_option_id']:
        context.user_data['score'] += 1

    context.user_data['current_question'] += 1

    if context.user_data['current_question'] < len(questions):
        await send_question(update, context)
    else:
        score_percentage = (context.user_data['score'] / len(questions)) * 100
        report = "\n".join(
            [f"Вопрос: {q[0]}\nВаш ответ: {q[1]}\nПравильный ответ: {q[2]}\nКомментарий: {q[3]}\n"
             for q in context.user_data['answers']]
        )
        await context.bot.send_message(
            chat_id=update.effective_user.id,
            text=f"Поздравляю, {context.user_data['name']}! Ты завершил викторину! \nТвой результат: {score_percentage:.1f} из 100 баллов.\n\nВот твой отчет:\n\n{report}\n\nСпасибо за участие! Если хочешь попробовать еще раз, просто отправь команду /start."
        )

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_answer, pattern='^[0-9]+$'))

    application.run_polling()

if __name__ == '__main__':
    main()
