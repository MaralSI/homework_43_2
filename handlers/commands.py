import glob
import random
import os
from aiogram.types import InputFile
from aiogram import types, Dispatcher
from config import bot

async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Привет! {message.from_user.first_name}')

async def mem(message: types.Message):
    path = 'media/'
    files = glob.glob(os.path.join(path, '*'))
    random_photo = random.choice(files)

    await bot.send_photo(chat_id=message.from_user.id,
                         photo=InputFile(random_photo))

    await message.answer_photo(photo=InputFile(random_photo))

async def message_handler(message: types.Message):
    text = message.text
    try:
        number = float(text)
        response = number ** 2
    except ValueError:
        response = text
    await message.answer(str(response))

async def send_file(message: types.Message):
    file_name = 'example.txt'
    content = 'Это является примером содержимого файла.'
    with open(file_name, 'w') as file:
        file.write(content)
    await message.reply_document(document=InputFile(file_name))

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'начало'])
    dp.register_message_handler(mem, commands=['mem', 'мем'])
    dp.register_message_handler(send_file, commands=['sendfile'])
    dp.register_message_handler(message_handler)


