from aiogram import types, Dispatcher
from config import dp
from assist_func import appeals_server
from state_machine import FSMTime
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
import datetime

dp: Dispatcher


@dp.message_handler(Text(equals='Расписание на сегодня'), state=FSMTime.date_timetable)
async def today_timetable(message: types.Message, state: FSMContext):
    date_start = str(datetime.datetime.today()).split(' ')[0]
    date_finish = date_start
    async with state.proxy() as data:
        arr = await appeals_server('https://rasp.omgtu.ru/api/search', 'https://rasp.omgtu.ru/api/schedule/group/',
                                   {'term': data['group'], 'type': 'group'},
                                   {'start': date_start, 'finish': date_finish})
    for i in arr:
        await message.answer(i, parse_mode='HTML', reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(Text(equals='Расписание на завтра'), state=FSMTime.date_timetable)
async def tomorrow_timetable(message: types.Message, state: FSMContext):
    date_start = str(datetime.datetime.today() + datetime.timedelta(days=1)).split(' ')[0]
    date_finish = date_start
    async with state.proxy() as data:
        arr = await appeals_server('https://rasp.omgtu.ru/api/search', 'https://rasp.omgtu.ru/api/schedule/group/',
                                   {'term': data['group'], 'type': 'group'},
                                   {'start': date_start, 'finish': date_finish})
    for i in arr:
        await message.answer(i, parse_mode='HTML', reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(Text(equals='Расписание на эту неделю'), state=FSMTime.date_timetable)
async def week_timetable(message: types.Message, state: FSMContext):
    today = datetime.datetime.today()
    date_start = today-datetime.timedelta(days=today.isoweekday()-1)
    date_finish = date_start + datetime.timedelta(days=6)
    async with state.proxy() as data:
        arr = await appeals_server('https://rasp.omgtu.ru/api/search', 'https://rasp.omgtu.ru/api/schedule/group/',
                                   {'term': data['group'], 'type': 'group'},
                                   {'start': str(date_start).split(' ')[0], 'finish': str(date_finish).split(' ')[0]})
    for i in arr:
        await message.answer(i, parse_mode='HTML', reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(Text(equals='Расписание на следующую неделю'), state=FSMTime.date_timetable)
async def next_week_timetable(message: types.Message, state: FSMContext):
    today = datetime.datetime.today()
    date_start = today+datetime.timedelta(days=7 - (today.isoweekday()-1))
    date_finish = date_start + datetime.timedelta(days=6)
    async with state.proxy() as data:
        arr = await appeals_server('https://rasp.omgtu.ru/api/search', 'https://rasp.omgtu.ru/api/schedule/group/',
                                   {'term': data['group'], 'type': 'group'},
                                   {'start': str(date_start).split(' ')[0], 'finish': str(date_finish).split(' ')[0]})
    for i in arr:
        await message.answer(i, parse_mode='HTML', reply_markup=ReplyKeyboardRemove())
    await state.finish()

