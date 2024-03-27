from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class SelectCallback(CallbackData, prefix="select"):
    value: str
    

def create_select_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="VIDEO",
        callback_data=(SelectCallback(value="video"))
    )
    builder.button(
        text="PHOTO",
        callback_data=(SelectCallback(value="photo"))
    )
    builder.button(
        text="AUDIO",
        callback_data=(SelectCallback(value="audio"))
    )
    return builder.as_markup()