import logging
from typing import Union
from aiogram import types
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.types import CallbackQuery
from loader import dp, bot, db
from keyboards.inline.menu_keyboards import start_keyboard, next_btn, choice_keyboard, sign_btn, detail_keyboard,\
    additional_keyboard, descr_keyboard
from keyboards.inline.callback_datas import menu_callback
import sqlite3


@dp.callback_query_handler(menu_callback.filter(item_name='cancel'))
async def cancel(call: CallbackQuery):
    await call.answer("Ви нажали відміна", show_alert=True)
    await call.message.edit_reply_markup()




@dp.message_handler(CommandStart())
async def show_menu(message: types.Message):
    markup = await start_keyboard()
    await message.answer(f"Доброго дня {message.from_user.full_name}!\n"
                         f"Мене звати Ірина і я ваш онлайн асистент.\n"
                         f"Спершу перейдіть по посиланню та ближче познайомтесь з Іриною Орловською.",
                         reply_markup=markup)



@dp.callback_query_handler(menu_callback.filter(item_name="next"))
async def show_items(call: CallbackQuery):
    markup = await next_btn()
    await call.message.answer(text="Дякуємо, що переглянули відео, тепер точно у вашому арсеналі +1 зачіска.\n"
                              "Як що вам нічого не потрібно жміть відміна \n",
                         reply_markup=markup)


@dp.callback_query_handler(menu_callback.filter(item_name="next_btn"))
async def choice_items(call: CallbackQuery):
    markup = await choice_keyboard()
    await call.message.answer(text='Ви нажали продовжити\n',
                              reply_markup=markup)




@dp.callback_query_handler(menu_callback.filter(item_name="sign_btn"))
async def sign(message: types.Message):
    markup = await sign_btn()
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    count = db.count_users()[0]
    await message.answer(f"Вітаємо {message.from_user.full_name}!\n"
                         f"Ви записалися на курс.\n",
                         f'Записалось <b>{count}</b> користувачів',
                         )



@dp.callback_query_handler(menu_callback.filter(item_name="detail"))
async def detail_course(call: CallbackQuery):
    markup = await detail_keyboard()
    await call.message.answer(text='Ви нажали Детальніше про курс\n',
                              reply_markup=markup)


@dp.callback_query_handler(menu_callback.filter(item_name="additional"))
async def additional_info(call: CallbackQuery):
    markup = await additional_keyboard()
    await call.message.answer(text='Ви нажали додаткові питання\n',
                              reply_markup=markup)


@dp.callback_query_handler(menu_callback.filter(item_name="descr"))
async def descr_info(call: CallbackQuery):
    markup = await descr_keyboard()
    await call.message.answer(text='Ви нажали Опис\n',
                              reply_markup=markup)





# markup = await sign_btn()
#     if isinstance(message, types.Message):
#         name = message.from_user.full_name
#         try:
#             db.add_user(id=message.from_user.id,
#                         name=name)
#         except sqlite3.IntegrityError as err:
#             print(err)
#         await message.answer(text="Вітаємо {message.from_user.full_name}!\n"
#                                   f"Ви записалися на курс.\n",
#                              reply_markup=markup)
#
#     elif isinstance(message, types.CallbackQuery):
#             call = message
#         await call.message.edit_reply_markup(markup)