from aiogram import types, Dispatcher
from config import bot
from keyboards.scraper import scraper_menu_keyboard
from scraper.news_scraper import NewsScraper
from scraper.news_24kg_scraper import NewsKGScraper
from database.bot_db import Database
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
    sc = NewsKGScraper()
    sc.scrape_data()
    db = Database()
    news_24kg = db.select_scrap_news_24kg()
    news_list = [f"{news['title']} ({news['time']}) - {news['link']}" for news in news_24kg]
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
