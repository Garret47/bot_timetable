from aiogram import Dispatcher
from aiogram.types import BotCommand


async def set_default_command(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [BotCommand('start', 'Запуск Бота'),
         BotCommand('help', 'Список комманд'),
         BotCommand('descr', 'Описание')]
    )
