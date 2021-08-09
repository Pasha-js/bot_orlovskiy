from aiogram.utils.callback_data import CallbackData
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, user
from loader import dp, bot
from keyboards.inline.callback_datas import menu_callback, support_callback, cancel_support_callback
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
    initial_keyboard = InlineKeyboardMarkup(row_width=2)
    INSTA_LINK = "https://www.instagram.com/orlovskairyna/"
    choice_detail = InlineKeyboardButton(text='Детальніше' + emoji.emojize(":detective:"), callback_data=menu_callback.new(item_name='detail'))
    choice_sign = InlineKeyboardButton(text='Запис' + emoji.emojize(":fire:"), callback_data=menu_callback.new(item_name='sign_btn'))
    choice_link = InlineKeyboardButton(text='Інстаграм ірини' + emoji.emojize(":up-right_arrow:"), url=INSTA_LINK)
    initial_keyboard.insert(choice_detail)
    initial_keyboard.insert(choice_sign)
    initial_keyboard.insert(choice_link)
    return initial_keyboard


async def sign_btn():
    initial_keyboard = InlineKeyboardMarkup()
    pay_btn = InlineKeyboardButton(text='Реквізити' + emoji.emojize(":clipboard:"), callback_data='pay')
    cancel_btn = InlineKeyboardButton(text='Відміна' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(pay_btn)
    initial_keyboard.insert(cancel_btn)

    return initial_keyboard


async def detail_keyboard():
    initial_keyboard = InlineKeyboardMarkup(row_width=2)
    descr_btn = InlineKeyboardButton(text='Опис' + emoji.emojize(":wrapped_gift:"), callback_data=menu_callback.new(item_name='descr'))
    additional_btn = InlineKeyboardButton(text='Додаткові питання' + emoji.emojize(":red_question_mark:"), callback_data=menu_callback.new(item_name='additional'))
    # cancel_btn = InlineKeyboardButton(text='Назад' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(descr_btn)
    initial_keyboard.insert(additional_btn)
    # initial_keyboard.insert(cancel_btn)
    return initial_keyboard




async def descr_keyboard():
    INSTA_LINK = "https://www.instagram.com/orlovskairyna/"
    initial_keyboard = InlineKeyboardMarkup(row_width=1)
    additional_btn = InlineKeyboardButton(text='Додаткові питання' + emoji.emojize(":pill:"),
                                          callback_data=menu_callback.new(item_name='additional'))
    choice_link = InlineKeyboardButton(text='Інстаграм ірини' + emoji.emojize(":up-right_arrow:"), url=INSTA_LINK)
    choice_sign = InlineKeyboardButton(text='Запис' + emoji.emojize(":fire:"), callback_data=menu_callback.new(item_name='sign_btn'))
    cancel_btn = InlineKeyboardButton(text='Відміна' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(additional_btn)
    initial_keyboard.insert(choice_sign)
    initial_keyboard.insert(choice_link)
    initial_keyboard.insert(cancel_btn)

    return initial_keyboard


async def additional_keyboard():
    initial_keyboard = InlineKeyboardMarkup(2)
    adress_btn = InlineKeyboardButton(text='Адресса проведення' + emoji.emojize(":double_exclamation_mark:"), callback_data=menu_callback.new(item_name='adress'))
    choice_sign = InlineKeyboardButton(text='Запис' + emoji.emojize(":fire:"), callback_data=menu_callback.new(item_name='sign_btn'))
    get_btn = InlineKeyboardButton(text='Що я отримаю' + emoji.emojize(":file_folder:"), callback_data=menu_callback.new(item_name='get'))
    reason_course = InlineKeyboardButton(text='Для чого мені цей курс' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='reason'))
    cancel_btn = InlineKeyboardButton(text='Відміна' + emoji.emojize(":red_question_mark:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(reason_course)
    initial_keyboard.insert(cancel_btn)
    initial_keyboard.insert(adress_btn)
    initial_keyboard.insert(choice_sign)
    initial_keyboard.insert(get_btn)

    return initial_keyboard

async def adress_keyboard():
    initial_keyboard = InlineKeyboardMarkup()
    cancel_btn = InlineKeyboardButton(text='Відміна' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(cancel_btn)

    return initial_keyboard

async def get_keyboard():
    initial_keyboard = InlineKeyboardMarkup()

    cancel_btn = InlineKeyboardButton(text='Відміна' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(cancel_btn)

    return initial_keyboard

async def reason_keyboard():
    initial_keyboard = InlineKeyboardMarkup()

    cancel_btn = InlineKeyboardButton(text='Відміна' + emoji.emojize(":BACK_arrow:"), callback_data=menu_callback.new(item_name='cancel'))
    initial_keyboard.insert(cancel_btn)

    return initial_keyboard


