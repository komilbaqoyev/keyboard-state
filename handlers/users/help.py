from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.personalData import personalData

from loader import dp


@dp.message_handler(CommandHelp(),state=personalData.fullname)
async def bot_help(message: types.Message):
    text = ("ism familyangizni kirirting")

    await message.reply(text)

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
