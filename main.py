from aiogram import types
from config import dp, Admin, bot
from aiogram.utils import executor
import logging
from handlers import commands, echo, quiz


async def on_startup(_):
    for i in Admin:
        await bot.send_message(chat_id=i, text='Bot started')
async def on_shutdown(_):
    for i in Admin:
        await bot.send_message(chat_id=i, text='Bot finished')


commands.register_commands(dp)
quiz.register_quiz_handlers(dp)

echo.register_echo_handler(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
