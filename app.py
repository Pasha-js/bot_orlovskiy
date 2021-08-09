from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import emoji

# async def on_startup(dispatcher):
#     # Устанавливаем дефолтные команды
#     await set_default_commands(dispatcher)
#
#     # Уведомляет про запуск
#     await on_startup_notify(dispatcher)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, on_startup=on_startup)

async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    import filters
    import middlewares
    # Уведомляет про запуск

    from utils.notify_admins import on_startup_notify
    print("Створюємо таблицю користувачів")
    try:
        await db.create_table_users()
    except Exception as err:
        print(err)
    print("Готово")

    print("Чистим таблицю користувачів")
    await db.delete_users()
    print('')
    # print(db.select_all_users())
    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)