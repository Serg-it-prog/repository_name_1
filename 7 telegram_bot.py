from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling

bot = Bot('7922260736:AAHFlqBOQ2HoZjEn1fI0LHHZoA1i-_fUE3Y')
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])#commands=['start'])
async def start(message: types.Message):
   # await bot.send_message(message.chat.id, 'hello')
   # await message.answer('Hello')
    await message.reply('hello')
   # file= open('/some.png', 'rb')
   # await message.answer_photo(file)
@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup=types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://www.google.com/'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)




start_polling(dp)