from bot_instance import bot, dp
from handlers import command_handlers
import asyncio
import logging

dp.include_routers(command_handlers.router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())