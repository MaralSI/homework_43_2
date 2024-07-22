from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


Admin = [6703150919, ]

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

async def pin(ctx):
    if ctx.message.reference:
        referenced_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await referenced_message.pin()
        await ctx.send('Сообщение закреплено!', delete_after=3)
    else:
        await ctx.send('Ответьте на сообщение, которое хотите закрепить.', delete_after=3)
