from aiogram import Bot, Dispatcher
from os import getenv

TOKEN = getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
