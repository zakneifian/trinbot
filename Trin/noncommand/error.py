# Log Errors caused by Updates.
import logging
logger = logging.getLogger()


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)