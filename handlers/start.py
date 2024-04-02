import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link

from config import bot, MEDIA_DESTINATION
from const import START_MENU_TEXT
from database import bot_db, sql_queries
from keyboards.start_menu import start_menu_keyboard
from database.async_database import AsyncDatabase


async def start_menu(message: types.Message):
    db = AsyncDatabase()
    await db.execute_query(
        query=sql_queries.INSERT_USER_QUERY,
        params=(
            None,
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
            None,
            0
        ),
        fetch='none'
    )

    command = message.get_full_command()
    if command[1] != '':
        link = await _create_link("start", payload=command[1])
        owner = db.execute_query(
            query=sql_queries.SELECT_USER_BY_LINK_QUERY,
            params=(link,),
            fetch='one'
        )

        if owner['telegram_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text='Ты не пройдешь'
            )
            return

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

