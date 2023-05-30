import telebot
from telebot import types

f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

f = open('thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()

bot = telebot.TeleBot("5997345265:AAGIKOgSrFteKik36bXRaRmGhtAG7lpzGq4")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привіт, bro🥶🥶🥶")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, "Усі кажуть " + message.text + ', а ти купи слона')

bot.polling()