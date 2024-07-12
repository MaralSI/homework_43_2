

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import buttons

class RegisterUser(StatesGroup):
    model = State()
    size = State()
    category = State()
    price = State()
    country_production = State()
    photo = State()
    submit = State()

async def start_model_creation(message: types.Message):
    await RegisterUser.model.set()
    await message.answer(text="Введите модель одежды:", reply_markup=buttons.cancel)

async def load_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model'] = message.text

    await RegisterUser.next()
    await message.answer(text='Введите размер одежды:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await RegisterUser.next()
    await message.answer(text='Введите категорию одежды:')


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await RegisterUser.next()
    await message.answer(text='Введите стоимость одежды:')

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await RegisterUser.next()
    await message.answer(text='Введите страну производства:')

async def load_country_production(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['country_production'] = message.text

    await RegisterUser.next()
    await message.answer(text='Отправьте фото модели:')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    keyboard = InlineKeyboardMarkup(row_width=2)
    yes_button = InlineKeyboardButton(text='Yes', callback_data='confirm_yes')
    no_button = InlineKeyboardButton(text='No', callback_data='confirm_no')
    keyboard.add(yes_button, no_button)

    await RegisterUser.next()
    await message.answer_photo(photo=data['photo'],
                               caption=f"Модель - {data['model']}\n"
                                       f"Размер - {data['size']}\n"
                                       f"Категория - {data['category']}\n"
                                       f"Стоимость - {data['price']}\n"
                                       f"Страна производства- {data['country_production']}\n\n"
                                       f'<b>Верные ли данные ?<b>',
                               reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


async def submit(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'confirm_yes':
        await callback_query.message.answer('Отлично! Регистрация пройдена.', reply_markup=None)
        await state.finish()
    elif callback_query.data == 'confirm_no':
        await callback_query.message.answer('Отменено!', reply_markup=None)
        await state.finish()

    else:
        await callback_query.message.answer(text='Нажмите на кнопку!', reply_markup=buttons.start_buttons)

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text='Отменено')

# Finite State Machine
def register_fsm_for_user(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',
                                                 ignore_case=True), state='*')
    dp.register_message_handler(start_model_creation, commands=['registration'])
    dp.register_message_handler(load_model, state=RegisterUser.model)
    dp.register_message_handler(load_size, state=RegisterUser.size)
    dp.register_message_handler(load_category, state=RegisterUser.category)
    dp.register_message_handler(load_price, state=RegisterUser.price)
    dp.register_message_handler(load_country_production, state=RegisterUser.country_production)
    dp.register_message_handler(load_photo, state=RegisterUser.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=RegisterUser.submit)

