from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()

    questionnarie_button = InlineKeyboardButton(
        "Questionnarire",
        callback_data="start_questionnarire"
    )
    markup.add(questionnarie_button)
    return markup