from .func_request import request_id, request_timetable
from .treatment_answer import sort_answer
from aiogram.types import ReplyKeyboardRemove
from config import bot, url_id, url_group
import datetime
from aiogram import Bot
from keyboards import kb_main_group

bot: Bot


async def appeals_server(url_id, url_group, params_id, params_group):
    id_label_group = await request_id(url_id, params=params_id)
    if id_label_group is None:
        return None
    elif id_label_group == 'Лёг':
        return 'Лёг'
    elif id_label_group[1]:
        params_id['term'] = id_label_group[1]
    timetable_group = await request_timetable(f'{url_group}{id_label_group[0]}', params=params_group)
    arr = await sort_answer(timetable_group, params_id['term'])
    return arr


async def response_processing_user(message, state, date_start, date_finish):
    date_start = str(date_start).split(' ')[0]
    date_finish = str(date_finish).split(' ')[0]
    async with state.proxy() as data:
        arr = await appeals_server(url_id, url_group,
                                   {'term': data['group'], 'type': 'group'},
                                   {'start': date_start, 'finish': date_finish})
    if arr and arr != 'Лёг':
        for i in arr:
            await message.answer(i, parse_mode='HTML')
    elif arr == 'Лёг':
        await message.answer('Похоже сайт снова лёг')
        await bot.send_sticker(sticker='CAACAgIAAxkBAAEGh5xjfudBmql8bakFwcK37mN2P_E5igACDQEAAlKJkSMj1EWMeMTHeysE',
                               chat_id=message.chat.id)
    elif arr is None:
        await message.answer('Извините, но похоже вы ввели группу, которую невозможно распознать')
    await state.finish()