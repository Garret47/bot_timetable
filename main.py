from aiogram import executor
from config import dp
from misc import set_default_command


async def on_startup(dp):
    await set_default_command(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)