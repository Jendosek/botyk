import telebot
bot = telebot.TeleBot("5997345265:AAGIKOgSrFteKik36bXRaRmGhtAG7lpzGq4")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привіт, bro🥶🥶🥶")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, "Усі кажуть " + message.text + ', а ти купи слона')

bot.polling()