
import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database.db import create_tables
from handlers.start_menu import start_menu_router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    await create_tables()

    dp.include_router(start_menu_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
