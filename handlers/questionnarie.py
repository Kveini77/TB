from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from config import bot


async def questionnaire_start_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Python or Mojo?"
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start_call,
        lambda call: call.data == "start_questionnarire"
    )