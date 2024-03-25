import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import bot_db
import const
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    married = State()
    gender = State()
    photo = State()


async def register_start_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отправь мне свой ник"
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Расскажи о себе"
    )
    await RegistrationStates.next()


async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Сколько тебе лет?\n"
             "используй только числа\n"
             "например: 18, 27, 45, 57\n"
             "если ты не хочешь указывать свой возраст просто напши '-'"
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    if message.text == "-":
        pass
    else:
        try:
            int(message.text)
        except ValueError:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="Используй только НУМЕРИК\n\n"
                     "Ргистрация проваленна ❌\n"
                     "Перезапустите регистрацию!"
            )
            await state.finish()
            return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Ты женат?\n\n"
             "Да или нет?\n\n"
             "Если вы не хотите сообщаить то отправьте '-'"
    )
    await RegistrationStates.next()


async def load_married(message: types.Message,
                        state: FSMContext):
    if message.text == "-":
        pass
    elif message.text.lower() == "да" or message.text.lower() == "нет":
        pass
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Вводить можно только да или нет\n\n"
                 "Ргистрация проваленна ❌\n"
                 "Перезапустите регистрацию!"
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['married'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Какой ваш гендер?\n\n"
             "Если вы не хотите сообщаить то отправьте '-'"
    )
    await RegistrationStates.next()


async def load_gender(message: types.Message,
                         state: FSMContext):
    if message.text == "-":
        pass
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Отправьте свое фото"
    )
    await RegistrationStates.next()


async def load_photo(message: types.Message,
                         state: FSMContext):
    db = bot_db.Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )
    print(message.photo)
    async with state.proxy() as data:
        db.insert_profile(
            tg_id=message.from_user.id,
            nickname=data["nickname"],
            biography=data["biography"],
            age=data["age"],
            married=data["married"],
            gender=data["gender"],
            photo=path.name
        )

        with open(path.name, "rb") as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=const.PROFILE_TEXT.format(
                    nickname=data["nickname"],
                    biography=data["biography"],
                    age=data["age"],
                    married=data["married"],
                    gender=data["gender"]
                )
            )
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Ты молодчик"
    )
    await state.finish()



def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        register_start_call,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_married,
        state=RegistrationStates.married,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )

