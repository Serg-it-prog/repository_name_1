import telebot
import webbrowser
from telebot.apihelper import send_message



bot = telebot.TeleBot('7922260736:AAHFlqBOQ2HoZjEn1fI0LHHZoA1i-_fUE3Y')


@bot.message_handler(commands=['site','website'])
def site(m):
    webbrowser.open('https://www.google.ru/')

@bot.message_handler(commands=['main'])
def main(t):
    bot.send_message(t.chat.id,'<b>Help</b> <em>information</em>', parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет' :
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Ваш id: {message.from_user.id}')




bot.polling(non_stop=True)