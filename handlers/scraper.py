from aiogram import types, Dispatcher
from config import bot
from keyboards.scraper import scraper_menu_keyboard
from scraper.news_scraper import NewsScraper
from scraper.async_news_24kg_scraper import AsyncNewsKGScraper
from database.bot_db import Database
from database.async_database import AsyncDatabase
from database import sql_queries
import const


async def scraper_menu_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Выберите один из варинатов",
        reply_markup=await scraper_menu_keyboard()
    )


async def scrap_news_call(call: types.CallbackQuery):
    sc = NewsScraper()
    db = Database()

    links = sc.scrape_data()[:5]
    for link in links:
        db.insert_scrap_news(link)
    await bot.send_message(
        chat_id=call.from_user.id,
        text='\n\n'.join(links)
    )


async def scrap_news_24kg_call(call: types.CallbackQuery):
    sc = AsyncNewsKGScraper()
    await sc.get_pages()
    db = AsyncDatabase()
    db = AsyncDatabase()

    news_24kg = await db.execute_query(
        query=sql_queries.SELECT_SCRAP_NEWS_24KG_QUERY,
        fetch='all'
    )
    news_list = [f"{news['NEWS_TITLE']} ({news['NEWS_TIME']}) - {news['NEWS_LINK']}" for news in news_24kg]
    await bot.send_message(
        chat_id=call.from_user.id,
        text="\n".join(news_list[:5])
        )


def register_scraper_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        scraper_menu_call,
        lambda call: call.data == "scraper_menu"
    )
    dp.register_callback_query_handler(
        scrap_news_call,
        lambda call: call.data == "scrap_news"
    )
    dp.register_callback_query_handler(
        scrap_news_24kg_call,
        lambda call: call.data == "scrap_news_24kg"
    )
