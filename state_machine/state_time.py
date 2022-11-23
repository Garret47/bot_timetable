from aiogram.dispatcher.filters.state import StatesGroup, State


class FSMTime(StatesGroup):
    date_timetable = State()
