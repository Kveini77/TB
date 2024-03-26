from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def profile_keyboard(tg_id):
    markup = InlineKeyboardMarkup()

    like_button = InlineKeyboardButton(
        "🥰",
        callback_data=f"like_{tg_id}"
    )
    dislike_button = InlineKeyboardButton(
        "👎",
        callback_data=f"likedis_{tg_id}"
    )

    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()

    update_profile_button = InlineKeyboardButton(
        "Обновить",
        callback_data="registration"
    )
    delite_profile_button = InlineKeyboardButton(
        "Удалить",
        callback_data="delete_profile"
    )

    markup.add(update_profile_button)
    markup.add(delite_profile_button)
    return markup
