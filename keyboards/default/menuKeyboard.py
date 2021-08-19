from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Uzmobile'),
            KeyboardButton(text='Ucell'),
            KeyboardButton(text='Beeline'),
            KeyboardButton(text='Mobiuz')
        ],


    ],
    resize_keyboard=True
)

