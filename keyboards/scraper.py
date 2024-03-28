from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def scraper_menu_keyboard():
    markup = InlineKeyboardMarkup()

    scrap_news_button = InlineKeyboardButton(
        "Показать и сохранить последние новости",
        callback_data="scrap_news"
    )
    scrap_news_24kg_button = InlineKeyboardButton(
        "Показать и сохранить последние 10 новостей с 24.kg",
        callback_data="scrap_news_24kg"
    )
    markup.add(scrap_news_button)
    markup.add(scrap_news_24kg_button)
    return markup
