from aiogram import executor, Dispatcher
from config import dp
from handlers import (
    start,
    questionnarie,
    group_actions,
    ban_checker,
    registration,
    profile,
    reference,
    scraper
)
from database import bot_db


async def on_startup(_):
    db = bot_db.Database()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)
questionnarie.register_questionnaire_handlers(dp=dp)
group_actions.register_group_actions_handlers(dp=dp)
ban_checker.register_ban_checker_handlers(dp=dp)
registration.register_registration_handlers(dp=dp)
profile.register_profile_handlers(dp=dp)
reference.register_reference_menu_handlers(dp=dp)
scraper.register_scraper_handlers(dp=dp)

if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup,
        skip_updates=True
    )
