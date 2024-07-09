
import logging
from aiogram import Dispatcher
from aiogram.utils import executor
from config import dp
from handlers import commands, echo, quiz

# Регистрация всех обработчиков
commands.register_commands(dp)
quiz.register_quiz_handlers(dp)
echo.register_echo_handler(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
