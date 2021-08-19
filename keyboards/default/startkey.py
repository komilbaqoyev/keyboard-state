from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

startke= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact",request_contact=True)
        ],
    ],
    resize_keyboard=False

)