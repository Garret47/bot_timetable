from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
port = os.getenv('port')
url_id = 'https://rasp.omgtu.ru/api/search'
url_group = 'https://rasp.omgtu.ru/api/schedule/group/'
bot = Bot(token=f'{os.getenv("BOT_TOKEN")}')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
