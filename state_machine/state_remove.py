from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMRemove(StatesGroup):
    group_remove = State()