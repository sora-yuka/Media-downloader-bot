import os
from aiogram import Router, types
from aiogram.utils.markdown import hbold

from utilities.tiktok import TikTok
from ext.keyboards.select_keyboard import SelectCallback, create_select_keyboard

router = Router(name=__name__)
    
    # await message.answer_video(
    #     video=video
        # aiovideo,
        # caption=f"Author: {result['author']}\n"
        #         f"Description: {result['description']}\n"
        #         f"Tags: {result['tags']}"
    # )
    
# @router.message()
# async def download_image(
#     message: types.Message
# ) -> None:
#     tiktok = TikTok(message.text)
#     await message.answer(
#         text=hbold("Preparing for sending..."),
#     )
    
    
    

# TODO: write audio function
# @router.message()
# async def process_audio_url(message: types.Message) -> None:
#     await message.answer("Closed for works")