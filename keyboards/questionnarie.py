from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()

    questionnarie_button = InlineKeyboardButton(
        "Python",
        callback_data="python"
    )
    markup.add(questionnarie_button)
    return markup