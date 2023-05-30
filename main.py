import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup

response1 = requests.get("https://minfin.com.ua/ua/currency/usd/")
if response1.status_code == 200:
    soup = BeautifulSoup(response1.text, features = "html.parser")
    for i1 in soup.find('div', {'class': "sc-1x32wa2-9 bKmKjX"}):
        i1.extract()
        print(i1, "USD")
else:
    print(f"Немає підключення {response1.status_code}")
response2 = requests.get("https://minfin.com.ua/ua/currency/eur/")
if response2.status_code == 200:
    soup = BeautifulSoup(response2.text, features = "html.parser")
    for i2 in soup.find('div', {'class': "sc-1x32wa2-9 bKmKjX"}):
        i2.extract()
        print(i2, "EUR")
else:
    print(f"Немає підключення {response2.status_code}")
response3 = requests.get("https://minfin.com.ua/ua/currency/pln/")
if response3.status_code == 200:
    soup = BeautifulSoup(response3.text, features = "html.parser")
    for i3 in soup.find('div', {'class': "sc-1x32wa2-9 bKmKjX"}):
        i3.extract()
        print(i3, "PLN")
else:
    print(f"Немає підключення {response3.status_code}")

bot = telebot.TeleBot("6227885520:AAE-isFe3KqNyd7yq8O04Ug2FRNU-wVj9dc")

@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Курс Долара")
    item2 = types.KeyboardButton("Курс Євро")
    item3 = types.KeyboardButton("Курс Злотих")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(m.chat.id, "Це конвертор валют, яку валюту хочете дізнатися?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == "Курс Долара":
        answer = f"Курс Долара становить {i1}"
    elif message.text.strip() == "Курс Євро":
        answer = f"Курс Євро становить {i2}"
    elif message.text.strip() == "Курс Злотих":
        answer = f"Курс Злотих становить {i3}"
    bot.send_message(message.chat.id, answer)

bot.polling()