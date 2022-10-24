from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
