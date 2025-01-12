import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN  
from hendlers import main_router


bot = Bot(token = TOKEN) 
dp = Dispatcher() # main router. processing incoming updates     processing - обработка


async def main():
    dp.include_router(main_router)  # tell dispatcher about router.
    await dp.start_polling(bot) # request to telegram API. If response is OK, bot start works


if __name__== '__main__':  # if this script is run in this directory
    try:
        asyncio.run(main())  
    except KeyboardInterrupt:
        print('Exit')
        