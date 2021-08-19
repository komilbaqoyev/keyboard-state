from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import personalData


@dp.message_handler(Command('anketa'))
async def name_gt(message: types.Message):
    await message.answer("ismingizni kiriting!")
    await personalData.fullname.set()

@dp.message_handler(state=personalData.fullname)
async def name_go(message: types.Message,state:FSMContext):
    soxranitism=message.text
    await state.update_data({
        "name": soxranitism
    })
    await message.answer("Emailingizni yuboring!")
    await personalData.next()
@dp.message_handler(state=personalData.email)
async def email_go(message: types.Message,state:FSMContext):
    email=message.text
    await state.update_data({
        'email':email
    })
    await message.answer("Telizni yuboring")
    await personalData.next()
@dp.message_handler(state=personalData.tel)
async def tel_go(message: types.Message,state:FSMContext):
    tel=message.text
    await state.update_data({
        "tel":tel
    })
    #makumotlani qayta oqiymiz
    data=await state.get_data()
    name=data.get('name')
    email=data.get('email')
    tel=data.get('tel')

    msg=f"Sizning malumotlaringiz:\n"
    msg+=f"Ismingiz: {name}\n"
    msg+=f"Emailingiz: {email}\n"
    msg+=f"Telefoningiz: {tel}"

    await message.answer(msg)
    await state.finish()
