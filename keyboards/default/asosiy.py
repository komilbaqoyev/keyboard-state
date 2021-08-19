from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

asos = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Aktivlash"),
         KeyboardButton(text="Ortga"),
         KeyboardButton(text='Bosh menu')

         ],
    ],
    resize_keyboard=True
)