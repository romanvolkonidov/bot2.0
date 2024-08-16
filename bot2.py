from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7373179644:AAGqYoumuur1CzrQ8s3I0geTlnj1IvgEHuI'

questions = [
    {"question": "Question 1?", "options": ["Option 1", "Option 2", "Option 3", "Option 4"], "correct_option_id": 0, "explanation": "Explanation for Question 1"},
    {"question": "Question 2?", "options": ["Option 1", "Option 2", "Option 3", "Option 4"], "correct_option_id": 1, "explanation": "Explanation for Question 2"},
    # Add more questions up to 20
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
    await query.edit_message_text(text=f"Приятно познакомиться, {query.data}! Давай начнем викторину.")
    await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = questions[context.user_data['current_question']]
    options = question['options']
    await context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question=question['question'],
        options=options,
        is_anonymous=False,
        allows_multiple_answers=False,
    )

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    name = context.user_data.get('name', 'друг')
    question = questions[context.user_data['current_question']]

    if update.poll_answer.option_ids[0] == question['correct_option_id']:
        context.user_data['score'] += 1
        await context.bot.send_message(
            chat_id=update.effective_user.id,
            text=f"Молодец, {name}! Это правильный ответ! \n\n{question['explanation']}"
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_user.id,
            text=f"Не расстраивайся, {name}! Ошибки помогают нам учиться. \n\n{question['explanation']}"
        )

    context.user_data['current_question'] += 1

    if context.user_data['current_question'] < len(questions):
        await context.bot.send_message(
            chat_id=update.effective_user.id,
            text=f"Давай продолжим, {name}! Следующий вопрос:"
        )
        await send_question(update, context)
    else:
        score_percentage = (context.user_data['score'] / len(questions)) * 100
        await context.bot.send_message(
            chat_id=update.effective_user.id,
            text=f"Поздравляю, {name}! Ты завершил викторину! \nТвой результат: {score_percentage:.1f} из 100 баллов.\n\nСпасибо за участие! Если хочешь попробовать еще раз, просто отправь команду /start."
        )

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(PollAnswerHandler(handle_answer))

    application.run_polling()

if __name__ == '__main__':
    main()
