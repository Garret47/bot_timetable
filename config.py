from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=f'{os.getenv("BOT_TOKEN")}')
dp = Dispatcher(bot)
