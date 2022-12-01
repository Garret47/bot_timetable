from aiogram import types, Dispatcher
from config import dp, url_id, bot
from assist_func import check_group_id
from keyboards import ikb
from bd import change_bd

dp: Dispatcher


@dp.message_handler(content_types=['text'], state=None)
async def get_group(message: types.Message):
    id_label_group = await check_group_id(url_id, {'term': message.text.upper(), 'type': 'group'})
    if id_label_group is None:
        await message.answer('Извините, но похоже вы ввели группу, которую невозможно распознать')
    elif id_label_group == 'Лёг':
        await message.answer('Похоже сайт снова лёг')
        await bot.send_sticker(sticker='CAACAgIAAxkBAAEGh5xjfudBmql8bakFwcK37mN2P_E5igACDQEAAlKJkSMj1EWMeMTHeysE',
                               chat_id=message.from_user.id)
    else:
        await change_bd.update_group_current_id(message.from_user.id, id_label_group[0], id_label_group[1]
                                                if id_label_group[1] else message.text.upper())
        await message.answer('Пожалуйста, укажите время', reply_markup=ikb)