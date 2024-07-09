import random
from aiogram import types, Dispatcher
from config import bot

games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

async def message_handler(message: types.Message):
    text = message.text
    try:
        number = float(text)
        response = number ** 2
        await message.answer(str(response))
    except ValueError:
        if "game" in text.lower():
            game = random.choice(games)
            await bot.send_dice(chat_id=message.chat.id, emoji=game)
        else:
            await message.answer(text)

def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(message_handler)
