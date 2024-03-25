from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()

    questionnarie_button = InlineKeyboardButton(
        "Опросник",
        callback_data="start_questionnarire"
    )
    ban_check_button = InlineKeyboardButton(
        "Проверка бана",
        callback_data="ban_checker"
    )
    registration_button = InlineKeyboardButton(
        "регистрация",
        callback_data="registration"
    )
    markup.add(questionnarie_button)
    markup.add(ban_check_button)
    markup.add(registration_button)
    return markup
