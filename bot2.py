import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

logger = logging.getLogger(__name__)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a message to the user."""
    logger.error(f"Exception while handling an update: {context.error}")
    if update:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Произошла ошибка. Пожалуйста, попробуйте позже."
        )


TOKEN = os.getenv('BOT_TOKEN', '7373179644:AAGqYoumuur1CzrQ8s3I0geTlnj1IvgEHuI')

import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a message to the user."""
    logger.error(f"Exception while handling an update: {context.error}")
    if update:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Произошла ошибка. Пожалуйста, попробуйте позже."
        )


TOKEN = os.getenv('BOT_TOKEN', '7373179644:AAGqYoumuur1CzrQ8s3I0geTlnj1IvgEHuI')

# Ваш список вопросов остается прежним

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Давай познакомимся. Как тебя зовут?")
    context.user_data['waiting_for_name'] = True

async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data.get('waiting_for_name'):
        context.user_data['name'] = update.message.text
        context.user_data['waiting_for_name'] = False
        context.user_data['score'] = 0
        context.user_data['current_question'] = 0
        await update.message.reply_text(f"Приятно познакомиться, {context.user_data['name']}! Давай начнем нашу викторину по HTML и CSS. Удачи тебе!")
        await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = questions[context.user_data['current_question']]
    keyboard = []
    for i, option in enumerate(question['options']):
        keyboard.append([InlineKeyboardButton(option, callback_data=str(i))])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=question['question'],
        reply_markup=reply_markup
    )

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    name = context.user_data.get('name', 'друг')
    question = questions[context.user_data['current_question']]

    if int(query.data) == question['correct_option_id']:
        context.user_data['score'] += 1
        await query.edit_message_text(
            text=f"Молодец, {name}! Это правильный ответ! \n\n{question['explanation']}"
        )
    else:
        await query.edit_message_text(
            text=f"Не расстраивайся, {name}! Ошибки помогают нам учиться. \n\n{question['explanation']}"
        )

    context.user_data['current_question'] += 1

    if context.user_data['current_question'] < len(questions):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Давай продолжим, {name}! Следующий вопрос:"
        )
        await send_question(update, context)
    else:
        score_percentage = (context.user_data['score'] / len(questions)) * 100
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Поздравляю, {name}! Ты завершил викторину! \nТвой результат: {score_percentage:.1f} из 100 баллов.\n\nСпасибо за участие! Если хочешь попробовать еще раз, просто отправь команду /start."
        )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a message to the user."""
    print(f"An error occurred: {context.error}")
    if update:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Произошла ошибка. Пожалуйста, попробуйте позже."
        )

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name))
    application.add_handler(CallbackQueryHandler(handle_answer))
    application.add_error_handler(error_handler)
    
    application.run_polling()

if __name__ == '__main__':
    main()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Давай познакомимся. Как тебя зовут?")
    context.user_data['waiting_for_name'] = True

async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data.get('waiting_for_name'):
        context.user_data['name'] = update.message.text
        context.user_data['waiting_for_name'] = False
        context.user_data['score'] = 0
        context.user_data['current_question'] = 0
        await update.message.reply_text(f"Приятно познакомиться, {context.user_data['name']}! Давай начнем нашу викторину по HTML и CSS. Удачи тебе!")
        await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = questions[context.user_data['current_question']]
    keyboard = []
    for i, option in enumerate(question['options']):
        keyboard.append([InlineKeyboardButton(option, callback_data=str(i))])
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=question['question'],
        reply_markup=reply_markup
    )

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    name = context.user_data.get('name', 'друг')
    question = questions[context.user_data['current_question']]

    if int(query.data) == question['correct_option_id']:
        context.user_data['score'] += 1
        await query.edit_message_text(
            text=f"Молодец, {name}! Это правильный ответ! \n\n{question['explanation']}"
        )
    else:
        await query.edit_message_text(
            text=f"Не расстраивайся, {name}! Ошибки помогают нам учиться. \n\n{question['explanation']}"
        )

    context.user_data['current_question'] += 1

    if context.user_data['current_question'] < len(questions):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Давай продолжим, {name}! Следующий вопрос:"
        )
        await send_question(update, context)
    else:
        score_percentage = (context.user_data['score'] / len(questions)) * 100
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Поздравляю, {name}! Ты завершил викторину! \nТвой результат: {score_percentage:.1f} из 100 баллов.\n\nСпасибо за участие! Если хочешь попробовать еще раз, просто отправь команду /start."
        )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a message to the user."""
    print(f"An error occurred: {context.error}")
    if update:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Произошла ошибка. Пожалуйста, попробуйте позже."
        )

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name))
    application.add_handler(CallbackQueryHandler(handle_answer))
    application.add_error_handler(error_handler)
    
    application.run_polling()

if __name__ == '__main__':
    main()
