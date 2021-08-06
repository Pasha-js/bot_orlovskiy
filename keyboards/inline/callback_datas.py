from aiogram.utils.callback_data import CallbackData

menu_callback = CallbackData("course", "item_name")
support_callback = CallbackData("ask_support", "messages", "user_id", "as_user")
cancel_support_callback = CallbackData("cancel_support", "user_id")