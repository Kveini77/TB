from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()

    reference_link_button = InlineKeyboardButton(
        "Получить реферальную ссылку",
        callback_data="reference_link"
    )
    list_reference_link_button = InlineKeyboardButton(
        "Список моих рефералов",
        callback_data="list_reference_link"
    )
    markup.add(reference_link_button)
    markup.add(list_reference_link_button)
    return markup


