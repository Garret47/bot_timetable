from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('Расписание на эту неделю')],
    [KeyboardButton('Расписание на следующую неделю')],
    [KeyboardButton('Расписание на сегодня'), KeyboardButton('Расписание на завтра')]
])