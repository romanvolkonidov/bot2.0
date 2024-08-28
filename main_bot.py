import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import threading
import calendar
import bot2

# Replace 'YOUR_MAIN_BOT_TOKEN' with your actual main bot token
MAIN_TOKEN = '7539049313:AAHGLl8wGMdwG18sUQjjmi0SFUBbWgmZ0R0'
# Replace these with the actual tokens used in calendar.py and bot2.py
CALENDAR_TOKEN = '7214117585:AAHmN7Sjl12RVnj19fB-atkG19R8UmKxo-Q'
BOT2_TOKEN = '7373179644:AAGqYoumuur1CzrQ8s3I0geTlnj1IvgEHuI'

main_bot = telebot.TeleBot(MAIN_TOKEN)
calendar_bot = telebot.TeleBot(CALENDAR_TOKEN)
bot2_bot = telebot.TeleBot(BOT2_TOKEN)

def create_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton('Бронирование уроков'), KeyboardButton('Повторение'))
    return keyboard

@main_bot.message_handler(commands=['start'])
def start(message):
    main_bot.send_message(message.chat.id, "Выберите действие:", reply_markup=create_keyboard())

@main_bot.message_handler(func=lambda message: True)
def handle_choice(message):
    if message.text == 'Бронирование уроков':
        # Forward the message to calendar bot
        calendar_bot.process_new_messages([message])
    elif message.text == 'Повторение':
        # Forward the message to bot2
        bot2_bot.process_new_messages([message])
    else:
        main_bot.reply_to(message, "Пожалуйста, выберите одно из предложенных действий.", reply_markup=create_keyboard())

def run_bot(bot):
    bot.polling(none_stop=True)

if __name__ == '__main__':
    # Start calendar bot in a separate thread
    calendar_thread = threading.Thread(target=calendar.main)
    calendar_thread.start()

    # Start bot2 in a separate thread
    bot2_thread = threading.Thread(target=bot2.main)
    bot2_thread.start()

    # Run the main bot
    run_bot(main_bot)
