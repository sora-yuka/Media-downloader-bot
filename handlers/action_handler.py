import os
from aiogram import F
from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from ext.fsm import GetUrl
from ext.keyboards.select_keyboard import SelectCallback
from utilities.tiktok import TikTok

router = Router(name=__name__)
    
    # aiovideo = types.FSInputFile(result["path"])
    
    # await message.answer_video(
    #     video=video
        # aiovideo,
        # caption=f"Author: {result['author']}\n"
        #         f"Description: {result['description']}\n"
        #         f"Tags: {result['tags']}"
    # )
    # os.remove(video)
    # os.remove(result["path"])

@router.callback_query(SelectCallback.filter())
async def select_handler(callback_query: types.CallbackQuery, callback_data: SelectCallback, state: FSMContext) -> None:
    await callback_query.answer(None)
    await state.set_state(GetUrl.url)
    await callback_query.message.answer(
        text="Now, send me tiktok url"
    )
    
@router.message(GetUrl.url)
async def process_url(message: types.Message, state: FSMContext) -> None:
    data = await state.update_data(url = message.text)
    await message.answer(text="Preparing for senidng...")
    await state.clear()
    
    tiktok = TikTok(data["url"])
    video_link = tiktok.download_tiktok(selected_value="video")
    video = types.FSInputFile(path=video_link)
    await message.answer_video(video=video)
    
    os.remove(video_link)