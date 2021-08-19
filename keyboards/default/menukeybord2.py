from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menuu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1000MB"),
            KeyboardButton(text="2000MB"),
            KeyboardButton(text="5000MB")

        ],

    ],
    resize_keyboard=True
)