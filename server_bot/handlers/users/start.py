import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.ConLOC import ContLoct

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)


    await message.answer("Xush kelibsiz!")
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi. \nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

    await message.answer("Telefon nomeringizni yuboring:", reply_markup=ContLoct)


@dp.message_handler(content_types='contact', is_sender_contact=True)
async def sender_contact_example(msg: types.Message):
    await msg.answer('Rahmat, kontaktingiz qabul qilindi!\n')

