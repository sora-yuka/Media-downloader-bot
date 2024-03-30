import os
from aiogram import Router, types
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext

from utilities.tiktok import TikTok
from ext.keyboards.select_keyboard import SelectCallback, create_select_keyboard
from ext.fsm import GetUrl

router = Router(name=__name__)

@router.callback_query(SelectCallback.filter())
async def select_callback_handler(
    callback: types.CallbackQuery,
    callback_data: SelectCallback,
) -> None:
    global select_result
    select_result = {"media": callback_data.value}
    
    await callback.answer(None)
    await callback.message.answer(
        text=hbold("Send me tiktok url")
    )
    
@router.message()
async def media_save_handler(
    message: types.Message,
) -> None:
    tiktok = TikTok(message.text)
    await message.answer(text=hbold("Preparing for sending..."))
    
    match select_result["media"]:
        case "video":
            response = tiktok.download_tiktok("video")
            video = types.FSInputFile(path=response["path"])
            await message.answer_video(
                video=video,
                caption=hbold(f"Author: {response['author']}\n"
                f"Description: {response['description']}\n"
                f"Tags: {response['tags']}")
            )
            os.remove(response["path"])
            
        case "photo":
            photo_links = tiktok.download_tiktok("photo")
            
            for photo_link in photo_links:
                photo = types.FSInputFile(path=photo_link)
                await message.answer_document(document=photo)
                os.remove(photo_link)