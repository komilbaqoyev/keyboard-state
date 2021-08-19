from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.menukeybord2 import menuu
from keyboards.default.asosiy import asos
from keyboards.default.startkey import startke
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states.startstate import shaxsiy


from loader import dp





@dp.message_handler(CommandStart())
async def bot_start(message:Message):
    await message.answer(
        f"Assalomu aleykum, Telefon raqamiongizni yuboring!",
            reply_markup=startke)
    await shaxsiy.Contact.set()

@dp.message_handler(state=shaxsiy.Contact,text='Contact')
async def name_go(message: types.Message,state:FSMContext):
    soxranitnomer=message.text
    await state.update_data({
        "name": soxranitnomer
    })
    await message.answer(
        f"Assalomu aleykum, {message.from_user.full_name}!  botga Xush kelipsiz!",
        reply_markup=menu)
    #await personalData.next()




@dp.message_handler(text='Uzmobile')
async def sentt(message:Message):
    await message.answer("UZTELECOM dan qulay va arzon oylik Internet-to‘plamlari!",reply_markup=menuu)

@dp.message_handler(text='1000MB')
async def sentt(message: Message):
    await message.answer("Yoqish uchun aktivlashtirish tugmasini bosing", reply_markup=asos)

@dp.message_handler(text='Aktivlash')
async def sentt(message: Message):
    await message.answer("Tabriklaymiz!", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text='Ortga')
async def sentt(message: Message):
    await message.answer("UZTELECOM dan qulay va arzon oylik Internet-to‘plamlari!",reply_markup=menuu)

@dp.message_handler(text='Bosh menu')
async def sentt(message: Message):
    await message.answer(
        f" Mobil aloqa kodlar boti!",
        reply_markup=menu)




