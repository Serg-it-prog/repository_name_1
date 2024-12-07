from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling
from aiogram.types.webhook_info import WebhookInfo

bot = Bot('7922260736:AAHFlqBOQ2HoZjEn1fI0LHHZoA1i-_fUE3Y')
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebhookInfo(url='https://google.ru')))
    await message.answer('Привет, мой друг', reply_markup=markup)
start_polling(dp)