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
    random_profile_button = InlineKeyboardButton(
        "Профили",
        callback_data="random_profile"
    )
    my_profile_button = InlineKeyboardButton(
        "Мой профиль",
        callback_data="my_profile"
    )
    reference_menu_button = InlineKeyboardButton(
        "Реферальная ссылка",
        callback_data="reference_menu"
    )
    scraper_menu_button = InlineKeyboardButton(
        "Скрапер",
        callback_data="scraper_menu"
    )
    markup.add(questionnarie_button)
    markup.add(ban_check_button)
    markup.add(registration_button)
    markup.add(random_profile_button)
    markup.add(my_profile_button)
    markup.add(reference_menu_button)
    markup.add(scraper_menu_button)
    return markup
