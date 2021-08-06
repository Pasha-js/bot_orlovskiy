from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("support_call", "Поспілкуватись з техпідтримкою"),
            types.BotCommand("support", "Написати в техпідтримку"),
            
        ]
    )
