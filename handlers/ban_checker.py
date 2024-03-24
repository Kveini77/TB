from aiogram import types, Dispatcher
from config import bot
from database.bot_db import Database


async def ban_checker_call(message: types.Message):
    db = Database()
    ban_user = db.select_ban_user(
        tg_id=message.from_user.id
    )
    if not ban_user or ban_user["count"] <= 0:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"Ууузбагойзя, у тебя нет нарушений"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"У вас есть нарушения\n"
                 f"Их кол-во: {ban_user['count']}"
        )


def register_ban_checker_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        ban_checker_call,
        lambda call: call.data == "ban_checker")
