from aiogram import types, Dispatcher
from config import dp
from assist_func import appeals_server, response_processing_user
from state_machine import FSMTime
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
import datetime

dp: Dispatcher


@dp.message_handler(Text(equals='Расписание на сегодня'), state=FSMTime.date_timetable)
async def today_timetable(message: types.Message, state: FSMContext):
    date_start = datetime.datetime.today()
    date_finish = date_start
    await response_processing_user(message, state, date_start, date_finish)


@dp.message_handler(Text(equals='Расписание на завтра'), state=FSMTime.date_timetable)
async def tomorrow_timetable(message: types.Message, state: FSMContext):
    date_start = datetime.datetime.today() + datetime.timedelta(days=1)
    date_finish = date_start
    await response_processing_user(message, state, date_start, date_finish)


@dp.message_handler(Text(equals='Расписание на эту неделю'), state=FSMTime.date_timetable)
async def week_timetable(message: types.Message, state: FSMContext):
    today = datetime.datetime.today()
    date_start = today-datetime.timedelta(days=today.isoweekday()-1)
    date_finish = date_start + datetime.timedelta(days=6)
    await response_processing_user(message, state, date_start, date_finish)


@dp.message_handler(Text(equals='Расписание на следующую неделю'), state=FSMTime.date_timetable)
async def next_week_timetable(message: types.Message, state: FSMContext):
    today = datetime.datetime.today()
    date_start = today+datetime.timedelta(days=7 - (today.isoweekday()-1))
    date_finish = date_start + datetime.timedelta(days=6)
    await response_processing_user(message, state, date_start, date_finish)


@dp.message_handler(content_types=types.ContentType.ANY, state=FSMTime.date_timetable)
async def empty_key(message: types.Message, state: FSMContext):
    await message.answer(text='Отмена', reply_markup=ReplyKeyboardRemove())
    await state.finish()

