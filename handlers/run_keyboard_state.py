from aiogram import types, Dispatcher, Bot
from config import dp, bot
from assist_func import appeals_server, response_processing_user
from state_machine import FSMTime
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
import datetime

dp: Dispatcher
bot: Bot


@dp.callback_query_handler(Text(equals='today'), state=FSMTime.date_timetable)
async def today_timetable(cal: types.CallbackQuery, state: FSMContext):
    await cal.answer()
    date_start = datetime.datetime.today()
    date_finish = date_start
    await response_processing_user(cal.message, state, date_start, date_finish)


@dp.callback_query_handler(Text(equals='tomorrow'), state=FSMTime.date_timetable)
async def tomorrow_timetable(cal: types.CallbackQuery, state: FSMContext):
    await cal.answer()
    date_start = datetime.datetime.today() + datetime.timedelta(days=1)
    date_finish = date_start
    await response_processing_user(cal.message, state, date_start, date_finish)


@dp.callback_query_handler(Text(equals='week'), state=FSMTime.date_timetable)
async def week_timetable(cal: types.CallbackQuery, state: FSMContext):
    await cal.answer()
    today = datetime.datetime.today()
    date_start = today - datetime.timedelta(days=today.isoweekday() - 1)
    date_finish = date_start + datetime.timedelta(days=6)
    await response_processing_user(cal.message, state, date_start, date_finish)


@dp.callback_query_handler(Text(equals='next_week'), state=FSMTime.date_timetable)
async def next_week_timetable(cal: types.CallbackQuery, state: FSMContext):
    await cal.answer()
    today = datetime.datetime.today()
    date_start = today + datetime.timedelta(days=7 - (today.isoweekday() - 1))
    date_finish = date_start + datetime.timedelta(days=6)
    await response_processing_user(cal.message, state, date_start, date_finish)


@dp.callback_query_handler(state=None)
async def click_inline_no_state(cal: types.CallbackQuery):
    await cal.message.answer('По миллиону раз не тыкаем, а то сломается')
    await bot.send_sticker(chat_id=cal.from_user.id,
                           sticker='CAACAgIAAxkBAAEGjQljgXn1G59JHu5NM7xsrEBtXtyQngACXxkAAniOGEuPZfeHaDThMysE')
    await cal.answer()


@dp.message_handler(content_types=types.ContentType.ANY, state=FSMTime.date_timetable)
async def empty_key(message: types.Message, state: FSMContext):
    await message.answer(text='Отмена')
    await state.finish()
