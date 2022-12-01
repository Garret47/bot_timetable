from keyboards import kb_main_group
from bd import choice_group_name
from aiogram.types import KeyboardButton


async def create_btn(id_user):
    arr = await choice_group_name(id_user)
    kb_main_group['keyboard'] = []
    if arr:
        group = arr[0][1].split(' ')
        btn = sum(kb_main_group['keyboard'], [])
        btn = list(map(lambda item: item['text'], btn))
        for i in group:
            if i not in btn:
                kb_main_group.insert(KeyboardButton(text=i))
        return kb_main_group
    else:
        return kb_main_group