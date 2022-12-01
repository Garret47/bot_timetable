from aiogram import types, Dispatcher
from config import dp
from state_machine import FSMTime
from aiogram.dispatcher.filters.state import StatesGroup
from keyboards import ikb

dp: Dispatcher
FSMTime: StatesGroup


@dp.message_handler(content_types=['text'], state=None)
async def get_group(message: types.Message, state):
    await message.answer('Пожалуйста, укажите время', reply_markup=ikb)
    await state.set_state(FSMTime.date_timetable)
    async with state.proxy() as data:
        data['group'] = message.text.upper()