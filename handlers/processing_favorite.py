from aiogram import types
from config import dp, url_id
from bd import choice_group_name, change_bd
from state_machine import FSMAdd, FSMRemove
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.dispatcher import Dispatcher, FSMContext
from assist_func import func_request, misc_func
from misc import create_btn
from keyboards import kb_main_group

dp: Dispatcher
FSMTime: StatesGroup


@dp.message_handler(state=FSMAdd.group_add)
async def add_group(message: types.Message, state: FSMContext):
    arr = await func_request.request_id(url_id, {'term': message.text.upper(), 'type': 'group'})
    if arr:
        groups = await choice_group_name(message.from_user.id)
        flag = await misc_func.check_group_add(message.text.upper(), groups)
        if flag == 'insert':
            await change_bd.insert_group_name(message.from_user.id, message.text.upper())
        elif flag == 'update':
            await change_bd.update_group_name(message.from_user.id, groups, message.text.upper())
        else:
            await message.answer('Вы уже добавили эту группу в избранное')
            await state.finish()
            return
        await create_btn(message.from_user.id)
        await message.answer('Группа добавлена в избранное', reply_markup=kb_main_group)
    else:
        await message.answer('Извините, но похоже вы ввели группу, которую невозможно распознать')
    await state.finish()


@dp.message_handler(state=FSMRemove.group_remove)
async def remove_group(message: types.Message, state: FSMContext):
    pass
