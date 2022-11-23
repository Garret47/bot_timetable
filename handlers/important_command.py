from aiogram import types
from config import dp

COMMAND_HELP = """
<b>/start</b> - <em>Запуск Бота</em>
<b>/help</b> - <em>Список комманд</em>
<b>/descr</b> - <em>Описание</em>
"""


@dp.message_handler(commands=['start'])
async def com_start(message: types.Message):
    await message.answer(f'Привет <b><em>{message.from_user.username}</em></b>, бот готов к работе', parse_mode='HTML')


@dp.message_handler(commands=['help'])
async def com_start(message: types.Message):
    await message.answer(text=COMMAND_HELP, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['descr'])
async def com_start(message: types.Message):
    await message.answer('Бот работает с расписанием занятий ОмГТУ, всё просто присылай название группы, '
                         'затем время, а Бот всё сделает за тебя👍')
    await message.delete()