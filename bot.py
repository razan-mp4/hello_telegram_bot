import telebot

# Токен бота
TOKEN = '6955486188:AAFFThQtrFOmY9mvDhxLFaUMOAC25pkxrPA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я бот. Я можу вітати тебе і відповідати на повідомлення 'Привіт'.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() == 'привіт':
        bot.reply_to(message, "Привіт!")
    else:
        bot.reply_to(message, "Я не розумію тебе. Я просто вітаю та реагую на 'Привіт'.")

bot.polling()
