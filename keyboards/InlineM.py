from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('Расписание на эту неделю', callback_data='week')],
    [InlineKeyboardButton('Расписание на следующую неделю', callback_data='next_week')],
    [InlineKeyboardButton('Расписание на сегодня', callback_data='today')],
    [InlineKeyboardButton('Расписание на завтра', callback_data='tomorrow')]
])