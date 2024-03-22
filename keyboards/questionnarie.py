from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()

    yes_button = InlineKeyboardButton(
        "Yes",
        callback_data="yes"
    )
    no_button = InlineKeyboardButton(
        "No",
        callback_data="no"
    )
    markup.add(yes_button)
    markup.add(no_button)
    return markup


async def questionnaire_keyboard2():
    markup = InlineKeyboardMarkup()

    num12_button = InlineKeyboardButton(
        "12",
        callback_data="num12"
    )
    num24_button = InlineKeyboardButton(
        "24",
        callback_data="num24"
    )
    markup.add(num12_button)
    markup.add(num24_button)
    return markup


async def questionnaire_keyboard3():
    markup = InlineKeyboardMarkup()

    love_button = InlineKeyboardButton(
        "Love",
        callback_data="love"
    )
    dont_love_button = InlineKeyboardButton(
        "Dont love",
        callback_data="dont_love"
    )
    markup.add(love_button)
    markup.add(dont_love_button)
    return markup
