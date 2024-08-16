import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes


TOKEN = os.getenv('BOT_TOKEN', '7152066894:AAGkTh2QLFNMSF7Z5dJdfj7IDjcDcDPoKnM')


questions = [
    {
        "question": "1. Какой элемент HTML используется для добавления заголовка страницы? 📑",
        "options": ["<header>", "<title>", "<h1>", "<meta>"],
        "correct_option_id": 1
    },
    {
        "question": "2. Какой элемент HTML используется для создания гиперссылок? 🔗",
        "options": ["<a>", "<link>", "<button>", "<url>"],
        "correct_option_id": 0
    },
    {
        "question": "3. Какой атрибут HTML используется для открытия ссылки в новой вкладке? 🆕",
        "options": ["target=\"_self\"", "target=\"_top\"", "target=\"_blank\"", "target=\"_parent\""],
        "correct_option_id": 2
    },
    {
        "question": "4. Какой элемент HTML используется для вставки изображения? 🖼",
        "options": ["<img>", "<picture>", "<photo>", "<image>"],
        "correct_option_id": 0
    },
    {
        "question": "5. Что указывает атрибут alt в теге <img>? 📝",
        "options": ["Размер изображения", "URL изображения", "Альтернативный текст для изображения", "Выравнивание изображения"],
        "correct_option_id": 2
    },
    {
        "question": "6. Какой элемент HTML используется для создания списка с маркерами? 📋",
        "options": ["<ul>", "<ol>", "<list>", "<item>"],
        "correct_option_id": 0
    },
    {
        "question": "7. Какой элемент HTML используется для создания списка с нумерацией? 🔢",
        "options": ["<ol>", "<ul>", "<list>", "<item>"],
        "correct_option_id": 0
    },
    {
        "question": "8. Какой элемент HTML используется для добавления текста под изображением? 📝",
        "options": ["<figcaption>", "<caption>", "<text>", "<description>"],
        "correct_option_id": 0
    },
    {
        "question": "9. Какой элемент HTML используется для создания раздела на странице? 🗂",
        "options": ["<section>", "<div>", "<article>", "<header>"],
        "correct_option_id": 0
    },
    {
        "question": "10. Какой элемент HTML используется для горизонтальной линии? 🌐",
        "options": ["<hr>", "<line>", "<divider>", "<break>"],
        "correct_option_id": 0
    },
    {
        "question": "11. Какое CSS-свойство задает цвет фона элемента? 🌈",
        "options": ["color", "background-color", "border-color", "text-color"],
        "correct_option_id": 1
    },
    {
        "question": "12. Какое CSS-свойство используется для установки шрифта текста? 🔠",
        "options": ["font-size", "font-family", "text-align", "line-height"],
        "correct_option_id": 1
    },
    {
        "question": "13. Какое CSS-свойство используется для задания максимальной ширины элемента? 📏",
        "options": ["width", "max-height", "max-width", "height"],
        "correct_option_id": 2
    },
    {
        "question": "14. Какое CSS-свойство задает внутренние отступы элемента? ⛓",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 1
    },
    {
        "question": "15. Какое CSS-свойство управляет выравниванием текста? 📝",
        "options": ["text-decoration", "text-align", "font-style", "vertical-align"],
        "correct_option_id": 1
    },
    {
        "question": "16. Какое CSS-свойство используется для установки стиля границы элемента? 🖊",
        "options": ["border", "border-width", "border-color", "border-radius"],
        "correct_option_id": 0
    },
    {
        "question": "17. Какое CSS-свойство задает размер шрифта текста? 📏",
        "options": ["font-family", "font-size", "text-align", "margin"],
        "correct_option_id": 1
    },
    {
        "question": "18. Какое CSS-свойство задает отступы между элементами? ⬆️⬇️⬅️➡️",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 0
    },
    {
        "question": "19. Какое CSS-свойство изменяет стиль ссылок при наведении курсора? 🖱",

Репетитор Английского и IT Роман, [8/17/2024 1:46 AM]
"options": ["color", "a:hover", "text-decoration", "border"],
        "correct_option_id": 1
    },
    {
        "question": "20. Какой элемент HTML используется для определения основной части документа? 📝",
        "options": ["<main>", "<section>", "<div>", "<article>"],
        "correct_option_id": 0
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


