from .func_request import request_timetable
from .treatment_answer import sort_answer
from config import bot, url_id, url_group
from aiogram import Bot
from bd import choice_current_group_id

bot: Bot


async def appeals_server(url_group, group_name_id, params_group):
    timetable_group = await request_timetable(f'{url_group}{group_name_id[0]}', params=params_group)
    arr = await sort_answer(timetable_group, group_name_id[1])
    return arr


async def response_processing_user(message, state, date_start, date_finish):
    group_name_id = (await choice_current_group_id(message.chat.id))[0][0].split(" ")
    date_start = str(date_start).split(' ')[0]
    date_finish = str(date_finish).split(' ')[0]
    arr = await appeals_server(url_group, group_name_id, {'start': date_start, 'finish': date_finish})
    if arr:
        for i in arr:
            await message.answer(i, parse_mode='HTML')
    else:
        await message.answer('Возрадуйтесь пар нет)')
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker='CAACAgIAAxkBAAEGpPVjiWMxK3b9bLvluxHkaDj5Iq7ERwACNg8AAh4J8UlSVZzp6JZteysE')
    await state.finish()

