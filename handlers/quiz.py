
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, PollType
from config import bot

quiz_data = {
    "question1": {
        "question": "BMW or Mercedes?",
        "options": ["BMW", "Mercedes"],
        "correct_option_id": 1,
        "next_question": "question2"
    },
    "question2": {
        "question": "Messi or Ronaldo?",
        "options": ["Messi", "Ronaldo", "Я"],
        "correct_option_id": 2,
        "next_question": "question3"
    },
    "question3": {
        "question": "Сколько месяцев в году?",
        "options": ["10", "11", "12"],
        "correct_option_id": 2,
        "next_question": None
    }
}

async def start_quiz(message: types.Message):
    first_question = quiz_data["question1"]
    markup = InlineKeyboardMarkup()
    for idx, option in enumerate(first_question["options"]):
        markup.add(InlineKeyboardButton(option, callback_data=f"question1:{idx}"))
    await message.answer(first_question["question"], reply_markup=markup)

async def quiz_callback_handler(callback_query: types.CallbackQuery):
    question_id, option_id = callback_query.data.split(":")
    option_id = int(option_id)
    question = quiz_data[question_id]

    if option_id == question["correct_option_id"]:
        await bot.answer_callback_query(callback_query.id, text="Правильно!")
        next_question_id = question["next_question"]
        if next_question_id:
            next_question = quiz_data[next_question_id]
            markup = InlineKeyboardMarkup()
            for idx, option in enumerate(next_question["options"]):
                markup.add(InlineKeyboardButton(option, callback_data=f"{next_question_id}:{idx}"))
            await bot.send_message(callback_query.from_user.id, next_question["question"], reply_markup=markup)
        else:
            await bot.send_message(callback_query.from_user.id, "Викторина завершена!")
    else:
        await bot.answer_callback_query(callback_query.id, text="Неправильно, попробуйте снова!")

def register_quiz_handlers(dp: Dispatcher):
    dp.register_message_handler(start_quiz, commands=['quiz'])
    dp.register_callback_query_handler(quiz_callback_handler, lambda c: ':' in c.data)
