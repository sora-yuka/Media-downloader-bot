import asyncio
from decouple import config
from aiogram import Router, Bot, Dispatcher

from handlers.user_handler import router as user_router
from handlers.action_handler import router as action_router

router = Router()

@router.startup()
async def on_startup() -> None:
    print("Bot has been started")
    
@router.shutdown()
async def on_shutdown() -> None:
    print("Bot has been shuted")

async def main() -> None:
    bot = Bot(token=config("TOKEN"))
    dispatcher = Dispatcher()
    
    # dispatcher.include_router(router)
    dispatcher.include_routers(router, user_router, action_router)

    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())