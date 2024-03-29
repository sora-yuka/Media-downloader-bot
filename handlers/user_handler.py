import os
from decouple import config
from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold

from utilities.tiktok import TikTok
from ext.keyboards.select_keyboard import create_select_keyboard

router = Router(name=__name__)

@router.message(CommandStart())
async def start_handler(
        message: types.Message
) -> None:
    await message.delete()
    await message.answer(
        text=hbold("Hey, I can download tiktok without watermark. Select what type of media you want."),
        reply_markup=create_select_keyboard()
    )