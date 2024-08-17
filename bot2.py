import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, CallbackContext

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('BOT_TOKEN', '7152066894:AAGkTh2QLFNMSF7Z5dJdfj7IDjcDcDPoKnM')

# Replace these with your questions and options




# Global variable to store the current quiz state
quiz_state = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Cat Photo Quiz", callback_data='cat_photo')],
        [InlineKeyboardButton("Cafe Menu Quiz", callback_data='cafe_menu')],
        [InlineKeyboardButton("Exit", callback_data='exit')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Welcome! Choose a quiz below:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'cat_photo':
        quiz_state[query.from_user.id] = {'questions': cat_photo_questions, 'current_question': 0, 'score': 0}
        await query.edit_message_text(text="Cat Photo Quiz started! Here is your first question:")
        await send_question(update, context)
    elif data == 'cafe_menu':
        quiz_state[query.from_user.id] = {'questions': cafe_menu_questions, 'current_question': 0, 'score': 0}
        await query.edit_message_text(text="Cafe Menu Quiz started! Here is your first question:")
        await send_question(update, context)
    elif data == 'exit':
        await query.edit_message_text(text="Thank you for using the bot!")
    else:
        await query.edit_message_text(text="Unknown option selected.")

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    state = quiz_state.get(user_id)

    if state:
        questions = state['questions']
        current_question_index = state['current_question']

        if current_question_index < len(questions):
            question = questions[current_question_index]
            keyboard = [[InlineKeyboardButton(opt, callback_data=opt)] for opt in question['options']]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(question['question'], reply_markup=reply_markup)
        else:
            await update.message.reply_text(f"Quiz completed! Your score: {state['score']}/{len(questions)}")
            del quiz_state[user_id]
    else:
        await update.message.reply_text("Please start a quiz first using the /start command.")

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    answer = query.data
    user_id = query.from_user.id
    state = quiz_state.get(user_id)

    if state:
        questions = state['questions']
        current_question_index = state['current_question']
        correct_answer = questions[current_question_index]['answer']

        if answer == correct_answer:
            state['score'] += 1
            await query.edit_message_text("Correct!")
        else:
            await query.edit_message_text(f"Wrong! The correct answer was: {correct_answer}")

        state['current_question'] += 1
        await send_question(update, context)
    else:
        await query.edit_message_text("Please start a quiz first using the /start command.")

def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button, pattern='^(cat_photo|cafe_menu|exit)$'))
    app.add_handler(CallbackQueryHandler(handle_answer))

    logger.info("Bot started")
    app.run_polling()

if __name__ == '__main__':
    main()
