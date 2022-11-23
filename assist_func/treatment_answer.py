from functools import reduce


async def sort_answer(timetable_group, group):
    date = None
    arr = []
    for item in timetable_group:
        if date != item['date']:
            date = item['date']
            day = item['dayOfWeekString']
            filter_timetable_date = reduce(lambda ans, i: ans + f'Группа: {i["subGroup"] if i["subGroup"] else group}\n'
                                                                f'<b>Время: {i["beginLesson"]} - {i["endLesson"]}</b>\n'
                                                                f'Название дисциплины: <b>{i["discipline"]}</b>\n'
                                                                f'Преподаватель: <em>{i["lecturer"]}</em>\n'
                                                                f'Тип занятия: <em>{i["kindOfWork"]}</em>\n'
                                                                f'Аудитория: {i["auditorium"]}\n'
                                                                f'--------------------------------\n',
                                           filter(lambda i: i['date'] == date, timetable_group),
                                           f'День недели: {day}\n'
                                           f'--------------------------------\n')
            arr.append(filter_timetable_date)
    return arr
