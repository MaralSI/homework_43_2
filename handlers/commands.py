from aiogram import types, Dispatcher
from config import bot

async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=f'Привет! {message.from_user.first_name}')

async def dice(message: types.Message):
    bot_dice = await bot.send_dice(chat_id=message.chat.id, emoji='🎲')
    await bot.send_message(chat_id=message.chat.id, text=f"Бот бросил кость и выпало: {bot_dice.dice.value}")

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'начало'])
    dp.register_message_handler(dice, commands=['dice'])
