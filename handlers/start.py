import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link

from config import bot, MEDIA_DESTINATION
from const import START_MENU_TEXT
from database import bot_db
from keyboards.start_menu import start_menu_keyboard


async def start_menu(message: types.Message):
    print(message)
    db = bot_db.Database()
    db.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,

    )

    # with open(MEDIA_DESTINATION + "bot_pic.jpg", "rb") as photo:
    #     await bot.send_photo(
    #         chat_id=message.from_user.id,
    #         photo=photo,
    #         caption=START_MENU_TEXT.format(
    #             user=message.from_user.first_name,
    #             id=message.from_user.id
    #         ),
    #         reply_markup=await start_menu_keyboard()
    #     )
    command = message.get_full_command()
    if command[1] != '':
        link = await _create_link("start", payload=command[1])
        owner = db.select_user_by_link(link=link)
        if owner['telegram_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text='Ты не пройдешь'
            )
            return
        try:
            db.insert_reference_user(
                owner=owner['telegram_id'],
                reference=message.from_user.id
            )
            db.update_owner_balance(
                tg_id=owner['telegram_id']
            )
        except sqlite3.IntegrityError:
            await bot.send_message(
                chat_id=message.from_user.id,
                text='Ты уже использовал эту ссылку соррян'
            )

    with open(MEDIA_DESTINATION + "bot_gif.gif", "rb") as ani:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=ani,
            caption=START_MENU_TEXT.format(
                user=message.from_user.first_name,
                id=message.from_user.id
            ),
            reply_markup=await start_menu_keyboard()
        )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_menu,
        commands=["start"]
    )

