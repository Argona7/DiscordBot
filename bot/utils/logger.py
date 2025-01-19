import sys
from loguru import logger

def logging_setup():
    format_info = (
        "<fg #E56BA3>TOWNS 1.0</fg #E56BA3>"
        " | <i><w>{time:HH:mm:ss}</w></i>"
        " | <level>{level}</level>"
        " | <b><w>{message}</w></b>"
    )

    logger.remove()

    logger.add(sink=sys.stdout, format=format_info)
    logger.add("../../logs/debug.log", level="TRACE",format=format_info, compression="zip", rotation="50 MB")
    logger.opt(colors=True)



logging_setup()