from aiogram import executor, Dispatcher
from config import dp
from handlers import (
    start,
    questionnarie,
    group_actions,
    ban_checker
)
from database import bot_db


async def on_startup(_):
    db = bot_db.Database()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)
questionnarie.register_questionnaire_handlers(dp=dp)
group_actions.register_group_actions_handlers(dp=dp)
ban_checker.register_ban_checker_handlers(dp=dp)


if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup,
        skip_updates=True
    )
