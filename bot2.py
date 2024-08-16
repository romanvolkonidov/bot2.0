import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes


TOKEN = os.getenv('BOT_TOKEN', '7152066894:AAGkTh2QLFNMSF7Z5dJdfj7IDjcDcDPoKnM')


questions = [
    {
        "question": "1. Какой элемент HTML используется для добавления заголовка страницы? 📑",
        "options": ["<header>", "<title>", "<h1>", "<meta>"],
        "correct_option_id": 1,
        "explanation": "Тег <title> используется для определения заголовка страницы, который отображается на вкладке браузера."
    },
    {
        "question": "2. Какой элемент HTML используется для создания гиперссылок? 🔗",
        "options": ["<a>", "<link>", "<button>", "<url>"],
        "correct_option_id": 0,
        "explanation": "Тег <a> создает гиперссылки, которые могут ссылаться на другие страницы или ресурсы."
    },
    {
        "question": "3. Какой атрибут HTML используется для открытия ссылки в новой вкладке? 🆕",
        "options": ["target=\"_self\"", "target=\"_top\"", "target=\"_blank\"", "target=\"_parent\""],
        "correct_option_id": 2,
        "explanation": "Атрибут target=\"_blank\" открывает ссылку в новой вкладке или окне браузера."
    },
    {
        "question": "4. Какой элемент HTML используется для вставки изображения? 🖼",
        "options": ["<img>", "<picture>", "<photo>", "<image>"],
        "correct_option_id": 0,
        "explanation": "Тег <img> используется для вставки изображений на веб-страницу."
    },
    {
        "question": "5. Что указывает атрибут alt в теге <img>? 📝",
        "options": ["Размер изображения", "URL изображения", "Альтернативный текст для изображения", "Выравнивание изображения"],
        "correct_option_id": 2,
        "explanation": "Атрибут alt задает альтернативный текст, который отображается, если изображение не может быть загружено."
    },
    {
        "question": "6. Какой элемент HTML используется для создания списка с маркерами? 📋",
        "options": ["<ul>", "<ol>", "<list>", "<item>"],
        "correct_option_id": 0,
        "explanation": "Тег <ul> используется для создания ненумерованных списков с маркерами."
    },
    {
        "question": "7. Какой элемент HTML используется для создания списка с нумерацией? 🔢",
        "options": ["<ol>", "<ul>", "<list>", "<item>"],
        "correct_option_id": 0,
        "explanation": "Тег <ol> используется для создания упорядоченных списков с нумерацией."
    },
    {
        "question": "8. Какой элемент HTML используется для добавления текста под изображением? 📝",
        "options": ["<figcaption>", "<caption>", "<text>", "<description>"],
        "correct_option_id": 0,
        "explanation": "Тег <figcaption> добавляет описание или подпись к изображению."
    },
    {
        "question": "9. Какой элемент HTML используется для создания раздела на странице? 🗂",
        "options": ["<section>", "<div>", "<article>", "<header>"],
        "correct_option_id": 0,
        "explanation": "Тег <section> используется для группировки связанных элементов и разделов на странице."
    },
    {
        "question": "10. Какой элемент HTML используется для горизонтальной линии? 🌐",
        "options": ["<hr>", "<line>", "<divider>", "<break>"],
        "correct_option_id": 0,
        "explanation": "Тег <hr> создает горизонтальную линию, которая часто используется для разделения контента."
    },
    {
        "question": "11. Какое CSS-свойство задает цвет фона элемента? 🌈",
        "options": ["color", "background-color", "border-color", "text-color"],
        "correct_option_id": 1,
        "explanation": "Свойство background-color задает цвет фона элемента."
    },
    {
        "question": "12. Какое CSS-свойство используется для установки шрифта текста? 🔠",
        "options": ["font-size", "font-family", "text-align", "line-height"],
        "correct_option_id": 1,
        "explanation": "Свойство font-family устанавливает шрифт, используемый для текста."
    },
    {
        "question": "13. Какое CSS-свойство используется для задания максимальной ширины элемента? 📏",
        "options": ["width", "max-height", "max-width", "height"],
        "correct_option_id": 2,
        "explanation": "Свойство max-width задает максимальную ширину элемента, которая не будет превышена."
    },
    {
        "question": "14. Какое CSS-свойство задает внутренние отступы элемента? ⛓",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 1,
        "explanation": "Свойство padding устанавливает внутренние отступы внутри элемента, создавая пространство между содержимым и границей."
    },
    {
        "question": "15. Какое CSS-свойство управляет выравниванием текста? 📝",
        "options": ["text-decoration", "text-align", "font-style", "vertical-align"],
        "correct_option_id": 1,
        "explanation": "Свойство text-align управляет выравниванием текста по левому, правому краю или по центру."
    },
    {
        "question": "16. Какое CSS-свойство используется для установки стиля границы элемента? 🖊",
        "options": ["border", "border-width", "border-color", "border-radius"],
        "correct_option_id": 0,
        "explanation": "Свойство border задает стиль, ширину и цвет границы элемента."
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
        "explanation": "Свойство margin задает внешние отступы, создавая пространство вокруг элемента."
    },
    {
        "question": "19. Какое CSS-свойство изменяет стиль ссылок при наведении курсора? 🖱",
        "options": ["color", "a:hover", "text-decoration", "border"],
        "correct_option_id": 1,
        "explanation": "Селектор a:hover позволяет изменять стиль ссылки при наведении курсора мыши."
    },
    {
        "question": "20. Какой элемент HTML используется для определения основной части документа? 📝",
        "options": ["<main>", "<section>", "<div>", "<article>"],
        "correct_option_id": 0,
        "explanation": "Тег <main> определяет основную часть контента документа, исключая заголовки, футеры и навигацию."
    }
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Гарик", callback_data='Гарик')],
        [InlineKeyboardButton("Антонина", callback_data='Антонина')],
        [InlineKeyboardButton("Сара", callback_data='Сара')],
        [InlineKeyboardButton("Мэри", callback_data='Мэри')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Как вас зовут?', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    context.user_data['name'] = query.data
    context.user_data['current_question'] = 0
    context.user_data['score'] = 0
    context.user_data['answers'] = []
    await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = questions[context.user_data['current_question']]
    options = question['options']
    keyboard = [[InlineKeyboardButton(option, callback_data=str(i))] for i, option in enumerate(options)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=question['question'],
        reply_markup=reply_markup
    )

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    user_answer = int(query.data)
    current_question_index = context.user_data['current_question']
    correct_option_id = questions[current_question_index]['correct_option_id']
    explanation = questions[current_question_index]['explanation']
    
    if user_answer == correct_option_id:
        context.user_data['score'] += 4
        context.user_data['answers'].append({
            'question': questions[current_question_index]['question'],
            'user_answer': questions[current_question_index]['options'][user_answer],
            'correct_answer': questions[current_question_index]['options'][correct_option_id],
            'explanation': explanation
        })
    else:
        context.user_data['answers'].append({
            'question': questions[current_question_index]['question'],
            'user_answer': questions[current_question_index]['options'][user_answer],
            'correct_answer': questions[current_question_index]['options'][correct_option_id],
            'explanation': explanation
        })
    
    context.user_data['current_question'] += 1
    
    if context.user_data['current_question'] < len(questions):
        await send_question(update, context)
    else:
        score = context.user_data['score']
        report = f"Поздравляю, {context.user_data['name']}! Ты завершил викторину!\n\nТвой результат: {score:.1f} из 100 баллов.\n\nВот твой отчет:\n"
        for answer in context.user_data['answers']:
            report += f"Вопрос: {answer['question']}\nТвой ответ: {answer['user_answer']}\nПравильный ответ: {answer['correct_answer']}\nОбъяснение: {answer['explanation']}\n\n"
        report += "Спасибо за участие! Если хочешь попробовать еще раз, просто отправь команду /start."
        
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=report
        )

async def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CallbackQueryHandler(handle_answer))

    # Use existing event loop
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == '__main__':
    asyncio.run(main())


