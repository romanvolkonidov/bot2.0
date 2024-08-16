import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv('BOT_TOKEN', '7152066894:AAGkTh2QLFNMSF7Z5dJdfj7IDjcDcDPoKnM')



questions = [
    {
        "question": "1. Какой элемент HTML используется для добавления заголовка страницы? 📑",
        "options": ["<header>", "<title>", "<h1>", "<meta>"],
        "correct_option_id": 1,
        "explanation": "Элемент <title> - это как имя для всей веб-страницы. Оно показывается на вкладке браузера и помогает понять, о чем эта страница."
    },
    {
        "question": "2. Какой элемент HTML используется для создания гиперссылок? 🔗",
        "options": ["<a>", "<link>", "<button>", "<url>"],
        "correct_option_id": 0,
        "explanation": "Элемент <a> (от слова 'anchor' - якорь) используется для создания ссылок. Это как волшебная дверь, которая ведет на другие веб-страницы!"
    },
    {
        "question": "3. Какой атрибут HTML используется для открытия ссылки в новой вкладке? 🆕",
        "options": ["target=\"_self\"", "target=\"_top\"", "target=\"_blank\"", "target=\"_parent\""],
        "correct_option_id": 2,
        "explanation": "Атрибут target=\"_blank\" говорит браузеру открыть ссылку в новой вкладке. Это как открыть новое окно, чтобы посмотреть что-то интересное, не закрывая текущую страницу."
    },
    {
        "question": "4. Какой элемент HTML используется для вставки изображения? 🖼",
        "options": ["<img>", "<picture>", "<photo>", "<image>"],
        "correct_option_id": 0,
        "explanation": "Элемент <img> используется для добавления картинок на веб-страницу. Это как приклеить фотографию в альбом - теперь все могут её увидеть!"
    },
    {
        "question": "5. Что указывает атрибут alt в теге <img>? 📝",
        "options": ["Размер изображения", "URL изображения", "Альтернативный текст для изображения", "Выравнивание изображения"],
        "correct_option_id": 2,
        "explanation": "Атрибут alt предоставляет текстовое описание изображения. Это как подпись под фотографией, которая объясняет, что на ней изображено, если картинка не загрузилась или человек не может её увидеть."
    },
    {
        "question": "6. Какой элемент HTML используется для создания списка с маркерами? 📋",
        "options": ["<ul>", "<ol>", "<list>", "<item>"],
        "correct_option_id": 0,
        "explanation": "Элемент <ul> (unordered list) создает список с маркерами. Это как список покупок, где каждый пункт отмечен точкой или другим символом."
    },
    {
        "question": "7. Какой элемент HTML используется для создания списка с нумерацией? 🔢",
        "options": ["<ol>", "<ul>", "<list>", "<item>"],
        "correct_option_id": 0,
        "explanation": "Элемент <ol> (ordered list) создает нумерованный список. Это как инструкция, где каждый шаг пронумерован по порядку."
    },
    {
        "question": "8. Какой элемент HTML используется для добавления текста под изображением? 📝",
        "options": ["<figcaption>", "<caption>", "<text>", "<description>"],
        "correct_option_id": 0,
        "explanation": "Элемент <figcaption> добавляет подпись к изображению. Это как подпись под фотографией в альбоме, объясняющая, что на ней изображено."
    },
    {
        "question": "9. Какой элемент HTML используется для создания раздела на странице? 🗂",
        "options": ["<section>", "<div>", "<article>", "<header>"],
        "correct_option_id": 0,
        "explanation": "Элемент <section> используется для создания отдельного раздела на странице. Это как разделить комнату на зоны - каждая зона для чего-то своего."
    },
    {
        "question": "10. Какой элемент HTML используется для горизонтальной линии? 🌐",
        "options": ["<hr>", "<line>", "<divider>", "<break>"],
        "correct_option_id": 0,
        "explanation": "Элемент <hr> (horizontal rule) создает горизонтальную линию на странице. Это как провести черту в тетради, чтобы разделить разные части текста."
    },
    {
        "question": "11. Какое CSS-свойство задает цвет фона элемента? 🌈",
        "options": ["color", "background-color", "border-color", "text-color"],
        "correct_option_id": 1,
        "explanation": "Свойство background-color задает цвет фона. Это как выбрать цвет стен для комнаты - он будет заполнять всё пространство за содержимым."
    },
    {
        "question": "12. Какое CSS-свойство используется для установки шрифта текста? 🔠",
        "options": ["font-size", "font-family", "text-align", "line-height"],
        "correct_option_id": 1,
        "explanation": "Свойство font-family устанавливает шрифт текста. Это как выбрать стиль почерка - он определяет, как будут выглядеть буквы."
    },
    {
        "question": "13. Какое CSS-свойство используется для задания максимальной ширины элемента? 📏",
        "options": ["width", "max-height", "max-width", "height"],
        "correct_option_id": 2,
        "explanation": "Свойство max-width задает максимальную ширину элемента. Это как установить ограничитель - элемент может быть уже, но не шире указанного значения."
    },
    {
        "question": "14. Какое CSS-свойство задает внутренние отступы элемента? ⛓",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 1,
        "explanation": "Свойство padding задает внутренние отступы. Это как пространство между рамкой картины и самой картиной - оно находится внутри элемента."
    },
    {
        "question": "15. Какое CSS-свойство управляет выравниванием текста? 📝",
        "options": ["text-decoration", "text-align", "font-style", "vertical-align"],
        "correct_option_id": 1,
        "explanation": "Свойство text-align управляет выравниванием текста. Это как решить, будет ли текст прижат к левому краю, правому, или расположен по центру."
    },
    {
        "question": "16. Какое CSS-свойство используется для установки стиля границы элемента? 🖊",
        "options": ["border", "border-width", "border-color", "border-radius"],
        "correct_option_id": 0,
        "explanation": "Свойство border устанавливает стиль границы элемента. Это как нарисовать рамку вокруг картины - можно выбрать её толщину, цвет и стиль."
    },
    {
        "question": "17. Какое CSS-свойство задает размер шрифта текста? 📏",
        "options": ["font-family", "font-size", "text-align", "margin"],
        "correct_option_id": 1,
        "explanation": "Свойство font-size задает размер шрифта. Это как выбрать, насколько большими или маленькими будут буквы в тексте."
    },
    {
        "question": "18. Какое CSS-свойство задает отступы между элементами? ⬆️⬇️⬅️➡️",
        "options": ["margin", "padding", "border", "spacing"],
        "correct_option_id": 0,
        "explanation": "Свойство margin задает отступы между элементами. Это как расстояние между фотографиями на стене - оно определяет, насколько далеко элементы находятся друг от друга."
    },
    {
        "question": "19. Какое CSS-свойство изменяет стиль ссылок при наведении курсора? 🖱",
        "options": ["color", "a:hover", "text-decoration", "border"],
        "correct_option_id": 1,
        "explanation": "Псевдокласс a:hover изменяет стиль ссылок при наведении курсора. Это как волшебство - когда вы подводите мышку к ссылке, она может изменить свой вид!"
    },
    {
        "question": "20. Какой элемент HTML используется для определения основной части документа? 📝",
        "options": ["<main>", "<section>", "<div>", "<article>"],
        "correct_option_id": 0,
        "explanation": "Элемент <main> определяет основную часть документа. Это как главная комната в доме - здесь находится самое важное содержимое страницы."
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
    await update.message.reply_text('Привет! Как тебя зовут?', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    context.user_data['name'] = query.data
    context.user_data['current_question'] = 0
    context.user_data['score'] = 0
    context.user_data['answers'] = []
    
    greeting = "Отлично! Давай начнем нашу веселую викторину по HTML и CSS. Удачи тебе!"
    if context.user_data['name'] == 'Гарик':
        greeting = f"Привет, {context.user_data['name']}! {greeting}"
    else:
        greeting = f"Привет, {context.user_data['name']}! {greeting}"
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=greeting)
    await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = questions[context.user_data['current_question']]
    options = question['options']
    keyboard = [[InlineKeyboardButton(option, callback_data=f"{i}:{context.user_data['current_question']}")] for i, option in enumerate(options)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=question['question'],
        reply_markup=reply_markup
    )

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    selected_option, question_index = map(int, query.data.split(':'))
    question = questions[question_index]

    context.user_data['answers'].append((question['question'], question['options'][selected_option], question['options'][question['correct_option_id']]))
    
    if selected_option == question['correct_option_id']:
        context.user_data['score'] += 1
        feedback = "✅ Правильно! Молодец!"
    else:
        feedback = f"❌ Не совсем так, но ничего страшного! Правильный ответ: {question['options'][question['correct_option_id']]}"

    explanation = f"\n\n{question['explanation']}"
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{feedback}{explanation}"
    )

    context.user_data['current_question'] += 1

    if context.user_data['current_question'] < len(questions):
        await send_question(update, context)
    else:
        await send_final_report(update, context)

async def send_final_report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    score_percentage = (context.user_data['score'] / len(questions)) * 100
    report = "\n\n".join(
        [f"Вопрос: {q[0]}\nТвой ответ: {q[1]}\nПравильный ответ: {q[2]}"
         for q in context.user_data['answers']]
    )
    
    if context.user_data['name'] == 'Гарик':
        congratulation = f"Поздравляю, {context.user_data['name']}! Ты молодец!"
    else:
        congratulation = f"Поздравляю, {context.user_data['name']}! Ты молодец!"
    
    await context.bot.send_message(
        chat_id=update.effective_user.id,
        text=f"{congratulation} Ты завершил викторину! \nТвой результат: {score_percentage:.1f} из 100 баллов.\n\nВот твой отчет:\n\n{report}\n\nСпасибо за участие! Ты отлично справился! Если хочешь попробовать еще раз, просто отправь команду /start."
    )

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button, pattern='^(Гарик|Антонина|Сара|Мэри)$'))
    application.add_handler(CallbackQueryHandler(handle_answer, pattern='^[0-9]+:[0-9]+$'))

    application.run_polling()

if __name__ == '__main__':
    main()
