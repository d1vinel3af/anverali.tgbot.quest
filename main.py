import asyncio
import logging
import sys

from app.config import dp, bot
from database.basic import BaseConfigurationDataBase


from handlers import start, add


"""
TODO: Добавить функцию автоматического создания необходимых таблиц для работы с бд (sqlite3)
"""

async def start_bot():
    logging.info("preparing the environment")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start_bot())