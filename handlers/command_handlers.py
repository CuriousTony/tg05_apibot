from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from movie_api import get_random_quote

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):
    await message.answer('Привет, я кинобот.')


@router.message(Command('help'))
async def handle_help(message: Message):
    await message.answer('Справка по командам:\n'
                         '/start - запуск бота;\n'
                         '/help - справка по доступным командам.')


@router.message(Command('random'))
async def handle_quote(message: Message):
    quote = get_random_quote()
    await message.answer(quote)
