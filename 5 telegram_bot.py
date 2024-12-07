import json

import telebot
import requests
bot = telebot.TeleBot('7922260736:AAHFlqBOQ2HoZjEn1fI0LHHZoA1i-_fUE3Y')

API='ffacba07c25cb03c96953d3716d45445'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}, рад тебя видеть! Напиши название города в котором хотите узнать погоду.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.send_message(message.chat.id, f'Сейчас погода в городе {city}: {data["main"]["temp"]} градусов цельсия')

        image = 'solnce.png' if temp > 5.0 else 'groza.png'
        file = open('./'+image,'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан неверно')















bot.polling(non_stop=True)