from aiogram import F, Router, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
import os
import random
from config import TOKEN


bot = Bot(token = TOKEN) 
main_router = Router()

@main_router.message(CommandStart())  # Command "/start" handler. If user send "/start", this function will be called  Hendler.
async def start_command(message: Message): 
    await message.reply(f'Hi, {message.from_user.first_name}!')

@main_router.message(Command('help'))
async def help(message: Message):
    await message.answer('Help')

@main_router.message(Command('send_photo'))
async def send_photo(message: Message):
    await message.answer('Send your photo')
    @main_router.message(F.photo)
    
    async def get_id_photo(message: Message):
        await message.reply('Photo has been sent')
        photo_id = message.photo[-1].file_id # message.photo -  a list of PhotoSize objects   [-1] - get last photo in message.photo list (highest resolution)
        file = await bot.get_file(photo_id)
        local_file_path = f'C:\\Users\\admin\\Desktop\\python\\telegram_bot\\img_cat\\{str(message.photo[-1].file_id)} .jpg'
        with open(local_file_path, 'wb') as r:
            await bot.download_file(file.file_path, r)
        

@main_router.message(Command('get_photo'))
async def get_photo(message: Message):
    folder_path = 'C:\\Users\\admin\\Desktop\\python\\telegram_bot\\img_cat\\'
    image_files = os.listdir(folder_path)  # create list of image files in folder_path
    random_img = random.choice(image_files)
    img_path = os.path.join(folder_path, random_img)

    with open(img_path, 'rb') as photo:
        photo = FSInputFile(img_path)  # FSInputFile for local files
        await bot.send_photo(chat_id = message.chat.id, photo=photo)
