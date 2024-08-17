import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv('BOT_TOKEN', '7152066894:AAGkTh2QLFNMSF7Z5dJdfj7IDjcDcDPoKnM')

cat_photo_questions = [
    {
        "question": "1. Какой элемент используется для добавления заголовка страницы? 📑",
        "options": ["<header>", "<h1>", "<title>", "<h2>"],
        "correct_option_id": 2,
        "explanation": "Элемент <title> используется для добавления заголовка страницы. Это как название книги - оно отображается в заголовке вкладки браузера и помогает пользователям понять, о чем эта страница."
    },
    {
        "question": "2. Какой тег используется для создания гиперссылки? 🔗",
        "options": ["<link>", "<a>", "<button>", "<url>"],
        "correct_option_id": 1,
        "explanation": "Тег <a> (anchor) используется для создания гиперссылок. Это как дорожный указатель в интернете - он позволяет пользователям переходить с одной страницы на другую."
    },
    {
        "question": "3. Какой атрибут используется для открытия ссылки в новой вкладке? 🆕",
        "options": ["target=\"_self\"", "target=\"_top\"", "target=\"_blank\"", "target=\"_parent\""],
        "correct_option_id": 2,
        "explanation": "Атрибут target=\"_blank\" говорит браузеру открыть ссылку в новой вкладке. Это как открыть новое окно, чтобы посмотреть что-то интересное, не закрывая текущую страницу."
    },
    {
        "question": "4. Какой элемент используется для вставки изображения? 🖼",
        "options": ["<img>", "<picture>", "<image>", "<photo>"],
        "correct_option_id": 0,
        "explanation": "Элемент <img> используется для вставки изображения. Это как вклеить фотографию в альбом - он позволяет показать картинку на вашей веб-странице."
    },
    {
        "question": "5. Что указывает атрибут alt в теге <img>? 📝",
        "options": ["Размер изображения", "URL изображения", "Альтернативный текст для изображения", "Выравнивание изображения"],
        "correct_option_id": 2,
        "explanation": "Атрибут alt указывает альтернативный текст для изображения. Это как подпись под фотографией - она описывает, что на изображении, если оно не может быть показано."
    },
    {
        "question": "6. Какой элемент используется для создания списка с маркерами? 📋",
        "options": ["<ol>", "<ul>", "<list>", "<item>"],
        "correct_option_id": 1,
        "explanation": "Элемент <ul> (unordered list) используется для создания списка с маркерами. Это как список покупок, где порядок пунктов не имеет значения."
    },
    {
        "question": "7. Какой элемент используется для создания списка с нумерацией? 🔢",
        "options": ["<ol>", "<ul>", "<list>", "<item>"],
        "correct_option_id": 0,
        "explanation": "Элемент <ol> (ordered list) используется для создания списка с нумерацией. Это как список инструкций, где порядок шагов важен."
    },
    {
        "question": "8. Какой тег используется для добавления текста под изображением? 📝",
        "options": ["<figcaption>", "<caption>", "<text>", "<description>"],
        "correct_option_id": 0,
        "explanation": "Тег <figcaption> используется для добавления текста под изображением. Это как подпись под фотографией в альбоме - она дает дополнительную информацию о картинке."
    },
    {
        "question": "9. Какой элемент используется для группировки связанных элементов формы? 🧩",
        "options": ["<fieldset>", "<form-group>", "<group>", "<container>"],
        "correct_option_id": 0,
        "explanation": "Элемент <fieldset> используется для группировки связанных элементов формы. Это как создать отдельную секцию в анкете для связанных вопросов."
    },
    {
        "question": "10. Какой тег используется для добавления заголовка в форме? 📝",
        "options": ["<legend>", "<header>", "<title>", "<label>"],
        "correct_option_id": 0,
        "explanation": "Тег <legend> используется для добавления заголовка в форме. Это как название раздела в анкете - он описывает группу полей в форме."
    },
    {
        "question": "11. Какой атрибут у тега <input> определяет текстовое поле для ввода? ✏️",
        "options": ["type=\"text\"", "type=\"input\"", "type=\"field\"", "type=\"textarea\""],
        "correct_option_id": 0,
        "explanation": "Атрибут type=\"text\" у тега <input> определяет текстовое поле для ввода. Это как линия в бумажной форме, куда вы можете вписать текст."
    },
    {
        "question": "12. Какой элемент используется для создания группы радиокнопок? 🎛",
        "options": ["<checkbox>", "<radio>", "<input type=\"radio\">", "<select>"],
        "correct_option_id": 2,
        "explanation": "Элемент <input type=\"radio\"> используется для создания группы радиокнопок. Это как вопрос с вариантами ответов, где можно выбрать только один вариант."
    },
    {
        "question": "13. Какой элемент используется для создания списка с множественным выбором? 📋",
        "options": ["<select>", "<input type=\"checkbox\">", "<textarea>", "<list>"],
        "correct_option_id": 1,
        "explanation": "Элемент <input type=\"checkbox\"> используется для создания списка с множественным выбором. Это как список дел, где вы можете отметить несколько пунктов."
    },
    {
        "question": "14. Какой тег используется для создания кнопки отправки формы? 🖱",
        "options": ["<input type=\"submit\">", "<button>", "<submit>", "<form-button>"],
        "correct_option_id": 0,
        "explanation": "Тег <input type=\"submit\"> используется для создания кнопки отправки формы. Это как кнопка 'Отправить' на бумажной анкете - она говорит браузеру, что пора отправить данные формы."
    },
    {
        "question": "15. Какой тег используется для добавления параграфа текста? 🗒",
        "options": ["<p>", "<paragraph>", "<text>", "<section>"],
        "correct_option_id": 0,
        "explanation": "Тег <p> используется для добавления параграфа текста. Это как новый абзац в книге - он отделяет одну мысль или часть текста от другой."
    },
    {
        "question": "16. Какой тег используется для создания основной секции на странице? 🗂",
        "options": ["<section>", "<main>", "<article>", "<div>"],
        "correct_option_id": 1,
        "explanation": "Тег <main> используется для создания основной секции на странице. Это как главная комната в доме - здесь находится основное содержимое страницы."
    },
    {
        "question": "17. Какой элемент используется для вставки комментариев в HTML коде? 💬",
        "options": ["<!-- Комментарий -->", "/* Комментарий */", "// Комментарий", "<comment>"],
        "correct_option_id": 0,
        "explanation": "Элемент <!-- Комментарий --> используется для вставки комментариев в HTML коде. Это как заметки на полях - они помогают разработчикам, но не видны пользователям на странице."
    },
    {
        "question": "18. Какой тег используется для добавления нижнего колонтитула на страницу? 📜",
        "options": ["<footer>", "<bottom>", "<footer-section>", "<end>"],
        "correct_option_id": 0,
        "explanation": "Тег <footer> используется для добавления нижнего колонтитула на страницу. Это как подпись в конце письма - здесь обычно размещается контактная информация или ссылки на разделы сайта."
    },
    {
        "question": "19. Какой элемент определяет заголовок секции? 🏷",
        "options": ["<h1>", "<header>", "<title>", "<section-header>"],
        "correct_option_id": 1,
        "explanation": "Элемент <header> определяет заголовок секции. Это как заголовок главы в книге - он содержит вводную информацию для определенной части страницы."
    },
    {
        "question": "20. Какой тег используется для создания ссылки на внешние ресурсы в нижнем колонтитуле? 🔗",
        "options": ["<a>", "<link>", "<url>", "<reference>"],
        "correct_option_id": 0,
        "explanation": "Тег <a> используется для создания ссылки на внешние ресурсы в нижнем колонтитуле. Это как указатель на другие интересные места - он позволяет пользователям перейти на другие связанные страницы или сайты."
    }
]

cafe_menu_questions = [
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
        "explanation": "Элемент <a> (от слова 'anchor' - якорь) используется для создания ссылок. Это как дверь, которая ведет на другие веб-страницы!"
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
        [InlineKeyboardButton("Гарик", callback_data='name:Гарик')],
        [InlineKeyboardButton("Антонина", callback_data='name:Антонина')],
        [InlineKeyboardButton("Сара", callback_data='name:Сара')],
        [InlineKeyboardButton("Мэри", callback_data='name:Мэри')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Как тебя зовут?', reply_markup=reply_markup)

async def choose_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Cat Photo🐱", callback_data='quiz:Cat Photo')],
        [InlineKeyboardButton("Cafe Menu☕️", callback_data='quiz:Cafe Menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет, {context.user_data['name']}! Какое повторение ты хочешь пройти?",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data.startswith('name:'):
        context.user_data['name'] = query.data.split(':')[1]
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Привет, {context.user_data['name']}! Сейчас выбери повторение.")
        await choose_quiz(update, context)
    elif query.data.startswith('quiz:'):
        context.user_data['quiz'] = query.data.split(':')[1]
        context.user_data['current_question'] = 0
        context.user_data['score'] = 0
        context.user_data['answers'] = []
        
        if context.user_data['quiz'] == 'Cat Photo':
            context.user_data['questions'] = cat_photo_questions
        else:
            context.user_data['questions'] = cafe_menu_questions

        greeting = f"Отлично! Давай начнем повторение '{context.user_data['quiz']}'. Удачи!"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=greeting)
        await send_question(update, context)
    else:
        await handle_answer(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = context.user_data['questions'][context.user_data['current_question']]
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
    question = context.user_data['questions'][question_index]

    context.user_data['answers'].append((question['question'], question['options'][selected_option], question['options'][question['correct_option_id']]))

    if selected_option == question['correct_option_id']:
        context.user_data['score'] += 1
        feedback = "✅ Правильный ответ! Отлично!"
    else:
        feedback = f"❌ Неправильно. Правильный ответ: {question['options'][question['correct_option_id']]}"

    explanation = f"\n\n{question['explanation']}"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"{feedback}{explanation}"
    )

    context.user_data['current_question'] += 1

    if context.user_data['current_question'] < len(context.user_data['questions']): 
        await send_question(update, context)
    else:
        await send_final_report(update, context)

async def send_final_report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    score_percentage = (context.user_data['score'] / len(context.user_data['questions'])) * 100
    report = "\n\n".join(
        [f"Вопрос: {q[0]}\nТвой ответ: {q[1]}\nПравильный ответ: {q[2]}"
         for q in context.user_data['answers']]
    )
    
    if score_percentage == 100:
        comment = "Ты отлично справился, все ответы правильные! Это очень круто!"
    el
