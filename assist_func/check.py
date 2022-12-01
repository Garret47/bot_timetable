from .func_request import request_id


async def check_group_id(url, params):
    id_label_group = await request_id(url, params)
    if id_label_group == 'Лёг':
        return 'Лёг'
    return id_label_group


async def check_group_add(group, groups):
    if not groups:
        return 'insert'
    elif groups[0][1].find(group) == -1:
        return 'update'
    return ''


async def check_group_remove(group, groups):
    if groups and groups[0][1].find(group) != -1:
        return 'delete'
    return ''
