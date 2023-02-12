from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ContLoct = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Contact", request_contact=True),
        ],

    ],
    resize_keyboard=True
)