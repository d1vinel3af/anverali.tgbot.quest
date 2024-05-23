from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.filters import CommandObject

from app.config import bot, dp

from database.users import UserDataBase

@dp.message(Command("add"))
async def add(msg: Message, command: CommandObject):
    """
    1. проверить аргументы
    2. проверить пользователя в бд
    3. записать задачу в бд
    4. отправить сообщение о задаче
    """
    __args = command.args

    if __args and __args.isdigit():
        await bot.send_message(__args, "Тут типа задание")
        
    elif __args and isinstance(__args, str):
        __id = UserDataBase().get(obj="username", value=__args)
        print(__id)
        if __id:
            await bot.send_message(__id, "Типа текст с заданием")
        else:
            await msg.answer("Пользователя с таким никнеймом нет")

    else:
        await msg.answer("Необходимо указать никнейм или id")