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
            if text.lower() == "game":
                bot_dice = await bot.send_dice(chat_id=message.chat.id, emoji='🎲')
                user_dice = await message.answer_dice(emoji='🎲')
                await bot.send_message(chat_id=message.chat.id, text=f"Результат бота: {bot_dice.dice.value}")
                await bot.send_message(chat_id=message.chat.id, text=f"Ваш результат: {user_dice.dice.value}")
                if bot_dice.dice.value > user_dice.dice.value:
                    await bot.send_message(chat_id=message.chat.id, text="Бот победил!")
                elif bot_dice.dice.value < user_dice.dice.value:
                    await bot.send_message(chat_id=message.chat.id, text="Вы победили!")
                else:
                    await bot.send_message(chat_id=message.chat.id, text="Ничья!")
            else:
                game = random.choice(games)
                await bot.send_dice(chat_id=message.chat.id, emoji=game)
        else:
            await message.answer(text)

def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(message_handler)
