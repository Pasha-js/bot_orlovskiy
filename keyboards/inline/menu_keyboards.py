from aiogram.utils.callback_data import CallbackData
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, user
from loader import dp, bot
from keyboards.inline.callback_datas import menu_callback, support_callback, cancel_support
from data.config import supports_ids
import random

import emoji



async def start_keyboard():
    initial_keyboard = InlineKeyboardMarkup()
    COURSE_LINK = "https://www.instagram.com/orlovskairyna/"
    start_link = InlineKeyboardButton(text='Посилання на відео' + emoji.emojize(":dvd:"), url=COURSE_LINK)
    start_next = InlineKeyboardButton(text='Продовжити' + emoji.emojize(":next_track_button:"), callback_data=menu_callback.new(item_name='next'))
    initial_keyboard.insert(start_link)
    initial_keyboard.insert(start_next)

    return initial_keyboard




async def next_btn():
    initial_keyboard = InlineKeyboardMarkup()
    next = InlineKeyboardButton(text='Продовжити' + emoji.emojize(":next_track_button:"), callback_data=menu_callback.new(item_name='next_btn'))
    initial_keyboard.insert(next)

    return initial_keyboard


async def choice_keyboard():
    initial_keyboard = InlineKeyboardMarkup(row_width=3)
    INSTA_LINK = "https://www.instagram.com/orlovskairyna/"
    choice_detail = InlineKeyboardButton(text='Детальніше' + emoji.emojize(":detective:"), callback_data=menu_callback.new(item_name='detail'))
    choice_sign = InlineKeyboardButton(text='Запис' + emoji.emojize(":heavy_dollar_sign:"), callback_data=menu_callback.new(item_name='sign_btn'))
    choice_link = InlineKeyboardButton(text='Інстаграм ірини' + emoji.emojize(":peace_symbol:"), url=INSTA_LINK)
    cancel_btn = InlineKeyboardButton(text='Назад' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(choice_detail)
    initial_keyboard.insert(choice_sign)
    initial_keyboard.insert(choice_link)
    initial_keyboard.insert(cancel_btn)
    return initial_keyboard


async def sign_btn():
    initial_keyboard = InlineKeyboardMarkup()
    pay_btn = InlineKeyboardButton(text='Реквізити', callback_data='pay')
    cancel_btn = InlineKeyboardButton(text='Відміна' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(pay_btn)
    initial_keyboard.insert(cancel_btn)

    return initial_keyboard


async def detail_keyboard():
    initial_keyboard = InlineKeyboardMarkup(row_width=2)
    descr_btn = InlineKeyboardButton(text='Опис', callback_data=menu_callback.new(item_name='descr'))
    additional_btn = InlineKeyboardButton(text='Додаткові питання', callback_data=menu_callback.new(item_name='additional'))
    cancel_btn = InlineKeyboardButton(text='Назад' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(descr_btn)
    initial_keyboard.insert(additional_btn)
    initial_keyboard.insert(cancel_btn)
    return initial_keyboard




async def descr_keyboard():
    INSTA_LINK = "https://www.instagram.com/orlovskairyna/"
    initial_keyboard = InlineKeyboardMarkup(row_width=3)
    additional_btn = InlineKeyboardButton(text='Додаткові питання',
                                          callback_data=menu_callback.new(item_name='additional'))
    choice_link = InlineKeyboardButton(text='Інстаграм ірини', url=INSTA_LINK)
    choice_sign = InlineKeyboardButton(text='Запис', callback_data=menu_callback.new(item_name='sign_btn'))
    cancel_btn = InlineKeyboardButton(text='Назад' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(additional_btn)
    initial_keyboard.insert(choice_sign)
    initial_keyboard.insert(choice_link)
    initial_keyboard.insert(cancel_btn)

    return initial_keyboard


async def additional_keyboard():
    initial_keyboard = InlineKeyboardMarkup()
    adress_btn = InlineKeyboardButton(text='Адресса проведення', callback_data=menu_callback.new(item_name='adress'))
    choice_sign = InlineKeyboardButton(text='Запис', callback_data=menu_callback.new(item_name='sign_btn'))
    get_btn = InlineKeyboardButton(text='Що я отримаю', callback_data=menu_callback.new(item_name='get'))
    reason_course = InlineKeyboardButton(text='Для чого мені цей курс', callback_data=menu_callback.new(item_name='reason'))
    cancel_btn = InlineKeyboardButton(text='Назад' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(reason_course)
    initial_keyboard.insert(cancel_btn)
    initial_keyboard.insert(adress_btn)
    initial_keyboard.insert(choice_sign)
    initial_keyboard.insert(get_btn)

    return initial_keyboard

async def adress_keyboard():
    initial_keyboard = InlineKeyboardMarkup()
    cancel_btn = InlineKeyboardButton(text='Назад' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(cancel_btn)

    return initial_keyboard

async def get_keyboard():
    initial_keyboard = InlineKeyboardMarkup()

    cancel_btn = InlineKeyboardButton(text='Назад' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(cancel_btn)

    return initial_keyboard

async def reason_keyboard():
    initial_keyboard = InlineKeyboardMarkup()

    cancel_btn = InlineKeyboardButton(text='Назад' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(cancel_btn)

    return initial_keyboard


