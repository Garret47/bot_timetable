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
