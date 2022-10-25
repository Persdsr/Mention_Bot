import datetime
import time
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
    while True:
        time_now = datetime.datetime.now()
        if time_now.hour == 10 and time_now.minute == 0 and time_now.second == 0:
            await bot.send_message(message.from_user.id, 'Утро')
        elif time_now.hour == 11 and time_now.minute == 30 and time_now.second == 0:
            await bot.send_message(message.from_user.id, 'Попить')
        elif time_now.hour == 12 and time_now.minute == 30 and time_now.second == 0:
            await bot.send_message(message.from_user.id, 'Обед')
        elif time_now.hour == 13 and time_now.minute == 20 and time_now.second == 0:
            await bot.send_message(message.from_user.id, 'Попить')
        elif time_now.hour == 16 and time_now.minute == 52 and time_now.second == 0:
            await bot.send_message(message.from_user.id, 'Попить')
        elif time_now.hour == 19 and time_now.minute == 20 and time_now.second == 0:
            await bot.send_message(message.from_user.id, 'Перекус и попить')
        elif time_now.hour == 21 and time_now.minute == 30 and time_now.second == 0:
            await bot.send_message(message.from_user.id, 'Ужин')
        elif time_now.hour == 23 and time_now.minute == 30 and time_now.second == 0:
            await bot.send_message(message.from_user.id, 'Перекус')
        elif time_now.hour == 0 and time_now.minute == 40 and time_now.second == 0:
            await bot.send_message(message.from_user.id, 'Готовься спать')
        time.sleep(1)

share.register_share_handler(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
