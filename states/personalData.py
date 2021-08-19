
from aiogram.dispatcher.filters.state import StatesGroup, State

class personalData(StatesGroup):
                fullname=State()
                email=State()
                tel=State()
