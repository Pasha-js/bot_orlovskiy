import logging
from typing import Union
from aiogram import types
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery, Message
from loader import dp, bot, db
from keyboards.inline.menu_keyboards import start_keyboard, next_btn, choice_keyboard, sign_btn, detail_keyboard,\
    additional_keyboard, descr_keyboard, adress_keyboard, get_keyboard, reason_keyboard
from keyboards.inline.callback_datas import menu_callback, support_callback
import sqlite3
import emoji
from data.config import admin_id
from asyncpg.exceptions import UniqueViolationError
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink


@dp.callback_query_handler(menu_callback.filter(item_name='cancel'))
async def cancel(call: CallbackQuery):
    await call.answer("Відміна", show_alert=True)
    await call.message.edit_reply_markup()
    await call.message.delete()



@dp.message_handler(CommandStart())
async def show_menu(message: types.Message):
    markup = await start_keyboard()
    await message.answer(text=f"Доброго дня <b>{message.from_user.full_name}</b>!\n"
                         f"Мене звати Ірина і я ваш онлайн асистент. {emoji.emojize(':fire:')}\n"
                              f"Спершу перейдіть по посиланню та ближче познайомтесь з Іриною Орловською",

                         reply_markup=markup)




@dp.callback_query_handler(menu_callback.filter(item_name="next"))
async def show_items(call: CallbackQuery):
    markup = await next_btn()
    await call.message.answer(text="Дякуємо, що переглянули відео, тепер точно у вашому арсеналі +1 зачіска.\n"
                                   "Ви отримали багато інформаціїї безкоштовно, а уявіть скільки буде коли завітаєте на наші курси",
                                                       reply_markup=markup)




@dp.callback_query_handler(menu_callback.filter(item_name="next_btn"))
async def choice_items(call: CallbackQuery):
    markup = await choice_keyboard()
    await call.message.answer(text='Продовжити' + emoji.emojize(":next_track_button:"),
                              reply_markup=markup
                              )




@dp.callback_query_handler(menu_callback.filter(item_name="sign_btn"))
async def sign(message: Union[CallbackQuery, Message]):
    markup = await sign_btn()
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    count = db.count_users()[0]
    call = message
    await call.message.answer(text=f"Вітаємо {message.from_user.full_name}!\n"
                         f"Ви записалися на курс.\n"
                                   f'Записалось <b>{count}</b> користувачів',
                              reply_markup=markup
                         )


@dp.callback_query_handler(menu_callback.filter(item_name="detail"))
async def detail_course(call: CallbackQuery):
    markup = await detail_keyboard()
    await call.message.answer(text='HAIR STYLIST/ Перукар - модельєр\n'
                                   '\n'
                                   'Оголошено набір на  авторський курс навчального центру ORLOVSKYH\n'
                                   '\n'
                                   'HAIR STYLIST / Перукар - модельєр\n '
                                   '\n'
                                   'Навчальний центр ORLOVSKYH запрошує вас на курси, розроблені спеціально для новачків «з нуля».\n '
                                   'За підсумком ви успішно зможете працювати в салонах краси, перукарнях або вести приватну практику. '
                                   'Ми готуємо практиків, а не теоретиків!\n'
                                   '\n'
                                   'Однією з основних переваг нашої програми є кількість практичних занять.\n'
                                   'Багато практики не буває, тому перш ніж відправитись в самостійну подорож,'
                                   'ви зможете освоїти і вдосконалити майстерність під керівництвом досвідчених викладачів.\n'
                                   'В кінці навчання вас чекає кваліфікаційний іспит і вручення диплому навчального центру «ORLOVSKYH» \n'
                                   '\n'
                                   '⚠️не втрачай свій шанс навчайся разом з нами ⚠ \n'
                                   '\n'
                                   '- опис курсу 👇\n',

                              reply_markup=markup)


@dp.callback_query_handler(menu_callback.filter(item_name="additional"))
async def additional_info(call: CallbackQuery):
    markup = await additional_keyboard()
    await call.message.answer(text='Додаткові питання\n',
                                 reply_markup=markup)


@dp.callback_query_handler(menu_callback.filter(item_name="descr"))
async def descr_info(call: CallbackQuery):
    markup = await descr_keyboard()
    await call.message.answer(text='Курс перукар - модельєр "HAIR STYLIST" від школи краси ОРЛОВСЬКИХ триває 3,5 місяці, '
                                   'навчання проводиться 5-ть днів на тиждень. До п’яти людей у практичній групі. \n'
                                   '\n'
                                   '    ⏰ Уроки у нас тривають в 2 зміни'
                                   '- (1-ша зміна) з 10:00 до 13:30'
                                   '- (2-га зміна) з 14:30 до 17:30'
                                   '\n'
                                   '✏️ Навчальна програма включає в себе, як теоретичні так і практичні уроки.'
                                   ' На практичні уроки кожному учневі буде виданий тренувальний манекен для відпрацювання практичних навиків👌🏽'
                                   '❗️❗️❗️Частково надаємо моделей, допомагаємо з пошуком.'
                                   '\n'
                                   '📎 У навчальну програму входять такі предмети:\n'
                                   '_______________________________________________\n'
                                   '🔻(Теорія)🔻 🔻(Практика)🔻'
                                   '\n'
                                   '▪️ Етика і культура обслуговування:\n'
                                   '    -  основи етики в спілкуванні з колективом та клієнтами;\n'
                                   '    -  естетика зовнішнього вигляду;\n'
                                   '    -  психологія обслуговування.\n',
                                 reply_markup=markup)



@dp.callback_query_handler(menu_callback.filter(item_name="adress"))
async def adress_info(call: CallbackQuery):
    await call.answer("Тут буде адресса", show_alert=True)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(menu_callback.filter(item_name="get"))
async def get_info(call: CallbackQuery):
    markup = await get_keyboard()
    await call.message.answer(text='тут буде текст \n',
                              reply_markup=markup)


@dp.callback_query_handler(menu_callback.filter(item_name="reason"))
async def reason_info(call: CallbackQuery):
    markup = await reason_keyboard()
    await call.message.answer(text='тут буде текст\n',
                              reply_markup=markup)








@dp.message_handler(user_id=admin_id, commands=['check_subs'])
async def check_referrals(message: types.Message):
    referrals = db.count_users()
    text = f"Ваші участники:\n{referrals}"

    await message.answer(text)

















