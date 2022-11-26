from aiogram import types
from config import dp
from misc import create_btn

COMMAND_HELP = """
<b>/start</b> - <em>Запуск Бота</em>
<b>/help</b> - <em>Список комманд</em>
<b>/descr</b> - <em>Описание</em>
<b>/add</b> - <em>Добавить группу в избранное</em>
<b>/remove</b> - <em>Удалить избранную группу</em>
"""


@dp.message_handler(commands=['start'])
async def com_start(message: types.Message):
    kb_main_group = await create_btn(message.from_user.id)
    await message.answer(f'Привет <b><em>{message.from_user.username}</em></b>, бот готов к работе',
                         parse_mode='HTML', reply_markup=kb_main_group)


@dp.message_handler(commands=['help'])
async def com_start(message: types.Message):
    await message.answer(text=COMMAND_HELP, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['descr'])
async def com_start(message: types.Message):
    await message.answer('Бот работает с расписанием занятий ОмГТУ, всё просто присылай название группы, '
                         'затем время, а Бот всё сделает за тебя👍')
