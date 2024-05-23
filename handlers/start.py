from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message


from app.config import bot, dp

from database.users import UserDataBase

@dp.message(CommandStart())
async def start(msg: Message):
    __object = UserDataBase().get(
        obj="chat_id",
        value=msg.from_user.id
        )
    if __object:
        await msg.answer("Сообщение")
    else:
        # Тут процесс регистрации
        await msg.answer("Требуется регистрация")
