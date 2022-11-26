import aiohttp


async def request_timetable(url, params):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url, params=params)
        response_js = await response.json()
    return response_js


async def request_id(url, params):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url, params=params)
        if response.status // 100 == 5:
            return 'Лёг'
        response_js = await response.json()
    if len(response_js) > 0:
        return [response_js[0]['id'], response_js[0]['label']] \
            if response_js[0]['label'] else [response_js[0]['id'], None]