from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMTimer(StatesGroup):
    timer = State()