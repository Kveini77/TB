from database.bot_db import Database
from aiogram import types, Dispatcher
from config import bot

from keyboards.reference import reference_menu_keyboard
from aiogram.utils.deep_linking import _create_link
import const
import binascii
import os


async def reference_menu_call(call: types.CallbackQuery):
    db = Database()
    user_info = db.select_reference_user_info(tg_id=call.from_user.id)
    await bot.send_message(
        chat_id=call.from_user.id,
        text=const.REFERENCE_MENU_TEXT.format(
            user=call.from_user.first_name,
            balance=user_info['balance'],
            count=user_info['count'],
        ),
        reply_markup=await reference_menu_keyboard()
    )


async def reference_link_call(call: types.CallbackQuery):
    db = Database()
    user = db.select_user(tg_id=call.from_user.id)

    if user['link']:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f'Твоя старая ссылка {user["link"]}'
        )
    else:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link("start", payload=token)
        db.update_user_link(link=link, tg_id=call.from_user.id)
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f'Твоя новая ссылка {link}'
        )


async def list_reference_link_call(call: types.CallbackQuery):
    db = Database()
    user_info = db.select_reference_users()
    print(user_info)
    if not user_info:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="У вас пока нет рефералов"
        )
        return

    names = [user['first_name'] for user in user_info]
    await bot.send_message(
        chat_id=call.from_user.id,
        text=const.REFERENCE_LIST_TEXT.format(
            users_list=',\n'.join(names)
        ),
    )


def register_reference_menu_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        reference_menu_call,
        lambda call: call.data == "reference_menu"
    )
    dp.register_callback_query_handler(
        reference_link_call,
        lambda call: call.data == "reference_link"
    )
    dp.register_callback_query_handler(
        list_reference_link_call,
        lambda call: call.data == "list_reference_link"
    )


