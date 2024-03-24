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
    ban_check_button = InlineKeyboardButton(
        "Проверка бана",
        callback_data="ban_checker"
    )
    markup.add(questionnarie_button)
    markup.add(ban_check_button)
    return markup
