from aiogram import types, Dispatcher
from config import bot
from keyboards.questionnarie import questionnaire_keyboard, questionnaire_keyboard2, questionnaire_keyboard3


async def questionnaire_start_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Какие новеллы тебе нравятся?",
        reply_markup=await questionnaire_keyboard()
    )


async def yes_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="вау мне тоже\n\n12 или 24",
        reply_markup=await questionnaire_keyboard2()
    )


async def no_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="ПОН\n\n12 или 24?",
        reply_markup=await questionnaire_keyboard2()
    )


async def num12_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="пон\n\nТебе нравится 'Initial D'?",
        reply_markup=await questionnaire_keyboard3()
    )


async def num24_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="пон\n\nТебе нравится 'Initial D'?",
        reply_markup=await questionnaire_keyboard3()
    )


async def love_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Спасибо за пройденный опросник"
    )



def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionnaire_start_call,
        lambda call: call.data == "start_questionnarire"
    )
    dp.register_callback_query_handler(
        yes_call,
        lambda call: call.data == "yes"
    )
    dp.register_callback_query_handler(
        no_call,
        lambda call: call.data == "no"
    )
    dp.register_callback_query_handler(
        num12_call,
        lambda call: call.data == "num12"
    )
    dp.register_callback_query_handler(
        num24_call,
        lambda call: call.data == "num24"
    )
    dp.register_callback_query_handler(
        love_call,
        lambda call: call.data == "love"
    )

