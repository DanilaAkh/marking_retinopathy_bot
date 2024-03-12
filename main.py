import asyncio
from dotenv import load_dotenv
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from handlers import photo_commands, user_commands
from data import db_connection


async def main():
    load_dotenv()
    token = os.getenv('TOKEN_BOT')
    bot = Bot(token, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    
    #db_connection.create_table(db_connection.connection)

    dp.include_routers(photo_commands.router,
                       user_commands.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())
