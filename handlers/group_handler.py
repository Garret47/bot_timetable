from aiogram import types, Dispatcher
from config import dp
import aiohttp
from functools import reduce

dp: Dispatcher


async def request_timetable(url, params):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url, params=params)
        response_js = await response.json()
    return response_js


async def request_id(url, params):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url, params=params)
        response_js = await response.json()
    return response_js[0]['id']


async def sort_answer(timetable_group, group):
    date = None
    arr = []
    for item in timetable_group:
        if date != item['date']:
            date = item['date']
            day = item['dayOfWeekString']
            filter_timetable_date = reduce(lambda ans, i: ans + f'<b>Время: {i["beginLesson"]} - {i["endLesson"]}</b>\n'
                                                                f'Название дисциплины: <b>{i["discipline"]}</b>\n'
                                                                f'Преподаватель: <em>{i["lecturer"]}</em>\n'
                                                                f'Вид занятия: <em>{i["kindOfWork"]}</em>\n'
                                                                f'Аудитория: {i["auditorium"]}\n'
                                                                f'--------------------------------\n',
                                           filter(lambda i: i['date'] == date, timetable_group),
                                           f'Группа: {group}\n'
                                           f'День недели: {day}\n'
                                           f'--------------------------------\n')
            arr.append(filter_timetable_date)
    return arr


@dp.message_handler(content_types=['text'])
async def get_group(message: types.Message):
    id_group = await request_id('https://rasp.omgtu.ru/api/search', params={
        'term': f'{message.text.upper()}',
        'type': 'group'
    })
    timetable_group = await request_timetable(f'https://rasp.omgtu.ru/api/schedule/group/{id_group}',
                                              params={'start': '2022.11.14', 'finish': '2022.11.20'})
    arr = await sort_answer(timetable_group, message.text.upper())

    for i in arr:
        await message.answer(i, parse_mode='HTML')
