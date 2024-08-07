
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import dp


async def webapp_reply(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(KeyboardButton('Geeks online', web_app=types.WebAppInfo(url='https://online.geeks.kg')),
                    KeyboardButton('Kaktus Media', web_app=types.WebAppInfo(url='https://kaktus.media')),
                    KeyboardButton('Netflix', web_app=types.WebAppInfo(url='https://www.netflix.com/kg-ru/'))
                    KeyboardButton('Statdata', web_app=types.WebAppInfo(url='https://www.stat.gov.kg/'))
                    KeyboardButton('Research conference', web_app=types.WebAppInfo(url='https://centraleurasia.org/cess-fall-2024-conference/'))
                    KeyboardButton('Global Environment Facility', web_app=types.WebAppInfo(url='https://www.thegef.org/'))
                    KeyboardButton('Akipress', web_app=types.WebAppInfo(url='https://akipress.org/'))
                    KeyboardButton('Geeks Academy', web_app=types.WebAppInfo(url='https://geeks.kg/allcourses')))

    await message.answer('Нажми на кнопку ниже для перехода на сайты:', reply_markup=keyboard)


async def webapp_inline(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton('Geeks online', web_app=types.WebAppInfo(url='https://online.geeks.kg')),
                    InlineKeyboardButton('Kaktus Media', web_app=types.WebAppInfo(url='https://kaktus.media')),
                    InlineKeyboardButton('Netflix', web_app=types.WebAppInfo(url='https://www.netflix.com/kg-ru/'))
                    InlineKeyboardButton('Statdata', web_app=types.WebAppInfo(url='https://www.stat.gov.kg/'))
                    InlineKeyboardButton('Research conference', web_app=types.WebAppInfo(url='https://centraleurasia.org/cess-fall-2024-conference/'))
                    InlineKeyboardButton('Global Environment Facility', web_app=types.WebAppInfo(url='https://www.thegef.org/'))
                    InlineKeyboardButton('Akipress', web_app=types.WebAppInfo(url='https://akipress.org/'))
                    InlineKeyboardButton('Geeks Academy', web_app=types.WebAppInfo(url='https://geeks.kg/allcourses')))
    await message.answer('Нажми на кнопку ниже для перехода на сайты:', reply_markup=keyboard)


async def pin(ctx):
    if ctx.message.reference:
        referenced_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await referenced_message.pin()
        await ctx.send('Сообщение закреплено!', delete_after=3)
    else:
        await ctx.send('Ответьте на сообщение, которое хотите закрепить.', delete_after=3)


def register_webapp(db: Dispatcher):
    dp.register_message_handler(webapp_reply, commands=['webreply'])
    dp.register_message_handler(webapp_inline, commands=['webinline'])
    dp.register_message_handler(pin, commands=['!pin'])
    