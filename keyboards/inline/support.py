from aiogram.utils.callback_data import CallbackData
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, user
from loader import dp, bot
from keyboards.inline.callback_datas import menu_callback, support_callback, cancel_support_callback
from data.config import supports_ids
import random

import emoji


async def check_support_available(support_id):
    state = dp.current_state(chat=support_id, user=support_id)
    state_str = str(
        await state.get_state()
    )
    if state_str == 'in_support':
        return
    else:
        return support_id


async def get_support_manager():
    random.shuffle(supports_ids)
    for support_id in supports_ids:
        support_id = await check_support_available(support_id)
        if support_id:
            return support_id
    else:
        return


async def support_keyboard(messages, user_id=None):
    if user_id:
        contact_id = int(user_id)
        as_user = "no"
        text = "Відповісти користовачу"
    else:
        contact_id = await get_support_manager()
        as_user = "yes"
        if messages == "many" and contact_id is None:
            return False
        elif messages == "one" and contact_id is None:
            contact_id = random.choice(supports_ids)

        if messages == "one":
            text = "Написати одне повідомлення в техпідтримку"
        else:
            text = "Написати опературу"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text=text,
            callback_data=support_callback.new(
                messages=messages,
                user_id=contact_id,
                as_user=as_user
            )
        )
    )

    if messages == "many":
        keyboard.add(
            InlineKeyboardButton(
                text="Завершити діалог",
                callback_data=cancel_support_callback.new(
                    user_id=contact_id
                )
            )
        )
    return keyboard