import asyncio
import sys
from contextlib import suppress

from loguru import logger
from bot.core import process


async def main():
    await process()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("Bot stopped by user...")
        sys.exit(2)
