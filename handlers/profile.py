import re
from aiogram import types, Dispatcher
from config import bot
from keyboards.profile import profile_keyboard, my_profile_keyboard
from database.bot_db import Database
import const
import random


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.select_profile(tg_id=call.from_user.id)

    if profile:
        with open(profile["photo"], "rb") as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=profile["nickname"],
                    biography=profile["biography"],
                    age=profile["age"],
                    married=profile["married"],
                    gender=profile["gender"]
                ),
                reply_markup=await my_profile_keyboard()
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Заргайся"
        )


async def random_profile_call(call: types.CallbackQuery):
    if call.message.caption.startswith("Ник:"):
        await call.message.delete()
    db = Database()
    profiles = db.select_all_profile(
        tg_id=call.from_user.id
    )

    if profiles:
        random_profile = random.choice(profiles)

        with open(random_profile["photo"], "rb") as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=random_profile["nickname"],
                    biography=random_profile["biography"],
                    age=random_profile["age"],
                    married=random_profile["married"],
                    gender=random_profile["gender"]
                ),
                reply_markup=await profile_keyboard(tg_id=random_profile['telegram_id'])
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Ты просмотрел всех пользователей приходи позже"
        )


async def detect_like_call(call: types.CallbackQuery):
    await call.message.delete()
    owner = re.sub("like_", "", call.data)
    db = Database()

    db.insert_like_profile(
        owner=owner,
        liker=call.from_user.id
    )
    await random_profile_call(call=call)


async def delete_profile_call(call: types.CallbackQuery):
    await call.message.delete()
    db = Database()
    db.delete_profile(
        tg_id=call.from_user.id
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="АВСЕЕЕ ваша учетная запись удалена"
    )


def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        random_profile_call,
        lambda call: call.data == "random_profile"
    )
    dp.register_callback_query_handler(
        detect_like_call,
        lambda call: 'like_' in call.data
    )
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        delete_profile_call,
        lambda call: call.data == "delete_profile"
    )
