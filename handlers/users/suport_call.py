from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.inline.support import support_keyboard, check_support_available, get_support_manager
from keyboards.inline.callback_datas import support_callback, cancel_support_callback
from

from loader import dp, bot





@dp.message_handler(Command("support_call"))
async def ask_support(message: types.Message):
    text = "Хочете написати в техпідтримку? Нажміть на кнопку нижче"
    keyboard = await support_keyboard(messages="many")
    await message.answer(text, reply_markup=keyboard)


@dp.callback_query_handler(support_callback.filter(messages="many", as_user="yes"))
async def send_to_support_call(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.message.edit_text("Ви звернулися в техпідтримку. Чекайте відповіді від оператора")

    user_id = int(callback_data.get("user_id"))
    if not await check_support_available(user_id):
        support_id = await get_support_manager()
    else:
        support_id = user_id

    if not support_id:
        await call.message.edit_text('Нажаль зараз немає вільних операторів. Спробуйте пізніше')
        await state.reset_state()
        return

    await state.set_state("wait_in_support")
    await state.update_data(second_id=support_id)

    keyboard = support_keyboard(messages="many", user_id=call.from_user.id)

    await bot.send_message(support_id,
                           f"З вами хоче звязатись користувач {call.from_user.full_name}",
                           reply_markup=keyboard
                           )


@dp.callback_query_handler(support_callback.filter(messages="many", as_user="no"))
async def send_support_call(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    second_id = int(callback_data.get("user_id"))
    user_state = dp.current_state(user=second_id, chat=second_id)

    if str(await user_state.get_state()) != "wait_in_support":
        await call.message.edit_text('Нажаль користувач втік)')
        return

    await state.set_state("in_support")
    await user_state.set_state("in_support")

    await state.update_data(second_id=second_id)

    keyboard = cancel_support(second_id)
    keyboard_second_user = cancel_support(call.from_user.id)

    await call.message.edit_text("Ви на звязку з користувачем!\n"
                                 "Щоби завершити діалог нажміть на кнопку",
                                 reply_markup=keyboard
                                 )
    await bot.send_message(second_id,
                           "Техпідтримка на звязку ! Можете писати сюди повідомлення \n"
                           "Щоби завершити діалог нажміть на кнопку",
                           reply_markup=keyboard_second_user
                           )

@dp.message_handler(state="wait_in_support", content_types=types.ContentTypes.ANY)
async def not_supported(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get("second_id")
    keyboard = cancel_support(second_id)
    await message.answer("Дочекайтесь відповіді від менеджера або відмініть сеанс", reply_markup=keyboard)

@dp.callback_query_handler(cancel_support_callback.filter(), state=["in_support", "wait_in_support", None])
async def exit_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    user_id = int(callback_data.get("user_id"))
    second_state = dp.current_state(user=user_id, chat=user_id)

    if await second_state.get_state() is not None:
        data_second = await second_state.get_data()
        second_id = data_second.get("user_id")
        if int(second_id) == call.from_user.id:
            await second_state.reset_state()
            await bot.send_message(user_id, "Користувач завершив сеанс")

    await call.message.edit_text("Ви завершили сеанс")
    await state.reset_state()