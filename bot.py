import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia
from wikipedia.exceptions import PageError
from dotenv import  load_dotenv
import os
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu aleykum,shohona botga xush kelibsiz!")



@dp.message_handler(commands=['buy'])
async def send_products_list(message: types.Message):
    """
    This handler will be called when user sends `/buy` 
    """
    await message.reply("Here should be list of products!")











    




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





    
