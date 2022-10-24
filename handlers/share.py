from aiogram import types, Dispatcher

from create_bot import dp, bot
from data.db import Database

db = Database('data/database.db')


async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 890087678:
            text = message.text[9:]
            users = db.get_users()
            for user in users:
                try:
                    await bot.send_message(user[0], text)
                    if int(user[1]) != 1:
                        db.set_active(user[0], 1)
                except:
                    db.set_active(user[0], 0)

            await bot.send_message(message.from_user.id, 'Успешная рассылка')


def register_share_handler(dp: Dispatcher):
    dp.register_message_handler(sendall, commands=['sendall'])
