import datetime
from time import sleep

from aiogram import executor, types, Dispatcher

from create_bot import bot, dp
from data.db import Database
from handlers import share

db = Database('data/database.db')

async def on_startup(dp):
    print('Бот вышел в онлайн')


@dp.message_handler(commands=['start'])
async def start_test(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
            print(f'{message.from_user.id} - Зарегался')
        await bot.send_message(message.from_user.id, 'Добро пожаловать')

@dp.message_handler(commands=['mention'])
async def mention(message: types.Message):
    print(datetime.datetime.now().hour)
    if datetime.datetime.now().hour == 13:
        await bot.send_message(message.from_user.id, 'Утро')
    while True:
        if datetime.datetime.now().second == 20 or 30 or 40:
            await bot.send_message(message.from_user.id, 'кукукук')
    
share.register_share_handler(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
