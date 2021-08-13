from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards import inline
from keyboards.inline.support import support_keyboard
from keyboards.inline.callback_datas import support_callback, cancel_support_callback, menu_callback
from typing import Union
from aiogram.types import CallbackQuery, Message

from loader import dp, bot





# @dp.message_handler(Command("support"))
@dp.callback_query_handler(menu_callback.filter(item_name="chat"))
async def ask_support(message: Union[CallbackQuery, Message]):
    text = "Хочете написати в техпідтримку? Нажміть на кнопку нижче"
    keyboard = await support_keyboard(messages="one")
    call = message
    await call.message.answer(text, reply_markup=keyboard)

@dp.callback_query_handler(support_callback.filter(messages="one"))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    user_id = int(callback_data.get("user_id"))
    
    await call.message.answer("Пришліть ваше повідомлення")
    await state.set_state("wait_for_support_message")
    await state.update_data(second_id=user_id)
    
    
@dp.message_handler(state="wait_for_support_message", content_types=types.ContentTypes.ANY)
async def get_support_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data["second_id"]
    
    await bot.send_message(second_id, 
                           f"Вам прийшло повідомлення! Ви можете відповісти нажавши кнопку нижче")
    
    keyboard = await support_keyboard(messages="one", user_id=message.from_user.id)
    await message.copy_to(second_id, reply_markup=keyboard)
    
    await message.answer("Ви відправили це повідомлення")
    await state.reset_state()
    

def cancel_support(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            InlineKeyboardButton(
                text="Завершити сеанс",
                callback_data=cancel_support_callback.new(user_id=user_id)
            )
        ]
    )