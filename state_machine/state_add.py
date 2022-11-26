from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMAdd(StatesGroup):
    group_add = State()
