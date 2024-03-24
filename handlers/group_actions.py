from aiogram import types, Dispatcher
from config import bot
from profanity_check import predict, predict_prob
from database.bot_db import Database
from const import (
    FIRST_BAN_WARN_TEXT,
    BAN_WARN_TEXT,
    BAN_TEXT
)


async def chat_messages(message: types.Message):
    db = Database()
    ban_word_predict_prob = predict_prob([message.text])
    print(ban_word_predict_prob)

    if ban_word_predict_prob > 0.6:
        db.update_ban_count(
            tg_id=message.from_user.id
        )
        ban_user = db.select_ban_user(
            tg_id=message.from_user.id
        )

        if not ban_user:
            db.insert_ban_user(
                tg_id=message.from_user.id
            )
            await bot.send_message(
                chat_id=message.chat.id,
                text=FIRST_BAN_WARN_TEXT.format(
                    user=message.from_user.first_name,
                )
            )
        elif ban_user["count"] >= 3:
            await bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id
            )
            await bot.send_message(
                chat_id=message.chat.id,
                text=BAN_TEXT.format(
                    user=message.from_user.first_name,
                    ban_count=ban_user["count"]
                )
            )
        else:
            await bot.send_message(
                chat_id=message.chat.id,
                text=BAN_WARN_TEXT.format(
                    user=message.from_user.first_name,
                    ban_count=ban_user["count"]
                )
            )
        await message.delete()


def register_group_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(
        chat_messages
    )
