from aiogram import types, Dispatcher
from config import dp
from bd import choice_group_name
from state_machine import FSMAdd, FSMRemove
from aiogram.dispatcher.filters.state import StatesGroup

dp: Dispatcher
FSMTime: StatesGroup


@dp.message_handler(commands=['add'])
async def add_group(message: types.Message):
    arr = await choice_group_name(message.from_user.id)
    if arr and len(arr[0][1].split(' ')) >= 5:
        await message.answer('Извините, но больше невозможно добавить группы в избранное')
    else:
        await message.answer('Напишите пожалуйста название группы')
        await FSMAdd.group_add.set()


@dp.message_handler(commands=['remove'])
async def remove_group(message: types.Message):
    arr = await choice_group_name(message.from_user.id)
    if arr:
        await message.answer('Напишите пожалуйста название группы')
        await FSMRemove.group_remove.set()
    else:
        await message.answer('Извините, но избранных групп у вас нет')
