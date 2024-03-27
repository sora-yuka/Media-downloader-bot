import os
from aiogram import F
from aiogram import Router, types
from aiogram.filters import CommandStart
from decouple import config

from utilities.tiktok import TikTok
from ext.keyboards.select_keyboard import create_select_keyboard

router = Router(name=__name__)

@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    await message.delete()
    await message.answer(
        text="Hey, I can download tiktok without watermark. Select what type of media you want.",
        reply_markup=create_select_keyboard()
    )