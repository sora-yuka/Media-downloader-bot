import sys
import asyncio
import logging
from decouple import config
from aiogram import Router, Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.user_handler import router as user_router
from handlers.action_handler import router as action_router
from handlers.tiktok_handler import router as tiktok_router


async def main() -> None:
    bot = Bot(
        token=config("TOKEN"), 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    
    dispatcher = Dispatcher()
    dispatcher.include_routers(
        user_router, 
        tiktok_router,
        # action_router,
    )

    await dispatcher.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())