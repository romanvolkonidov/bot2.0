import os
from telegram import Update, Poll
from telegram.ext import Application, CommandHandler, PollAnswerHandler, ContextTypes, MessageHandler, filters

TOKEN = os.getenv('BOT_TOKEN', '7373179644:AAGqYoumuur1CzrQ8s3I0geTlnj1IvgEHuI')

# Your questions list remains the same

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
    await context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question=question['question'],
        options=question['options'],
        type=Poll.QUIZ,
        correct_option_id=question['correct_option_id'],
        is_anonymous=False
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
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_name))
    application.add_handler(PollAnswerHandler(handle_answer))
    application.run_polling()

if __name__ == '__main__':
    main()
