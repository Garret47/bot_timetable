from .func_request import request_id, request_timetable
from .treatment_answer import sort_answer


async def appeals_server(url_id, url_group, params_id, params_group):
    id_group = await request_id(url_id, params=params_id)
    timetable_group = await request_timetable(f'{url_group}{id_group}', params=params_group)
    arr = await sort_answer(timetable_group, params_id['term'])
    return arr