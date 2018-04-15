# python libs
import datetime
import logging

# telegram python api wrapper
from telegram.ext import Updater, CommandHandler, InlineQueryHandler

# commands
from commands.Start import start
from commands.carlos import carlos
from commands.dolarBTC import dolarBTC
from commands.help import help
from commands.plot import plot
# jobs
from jobs.CalcDollar import setDollar
from jobs.updateDT import updateDT
from jobs.updateLBTC import updateLBTC
from noncommand.InlineQuery import inlinequery
# non-commands
from noncommand.error import error
# utils
from utils.TokenReader import readToken
from utils.VET import timeVen, datetimeVen

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# To fetch new updates for my bot and dispatch them in a queue
updater = Updater(readToken())
dispatcher = updater.dispatcher
jobQ = updater.job_queue
# # # # # # # # # # COMMAND HANDLER # # # # # # # # # #
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('dolarBTC', dolarBTC, pass_args=True))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('carlos', carlos))
dispatcher.add_handler(CommandHandler('plot', plot, pass_args=True))
# # # # # # # # # NON-COMMAND HANDLER # # # # # # # # #
dispatcher.add_handler(InlineQueryHandler(inlinequery))
dispatcher.add_error_handler(error)
# # # # # # # # # # JOBS FOR THE BOT # # # # # # # # # #
jobQ.run_repeating(setDollar, 600, first=0)
jobQ.run_daily(updateDT, datetime.time(hour=0, minute=0, second=0))
jobQ.run_daily(updateLBTC, datetime.time(hour=0, minute=0, second=0), context="24")
# first in this job basically just is the next hour from now on
jobQ.run_repeating(updateLBTC, 3600, first=datetime.time(hour=0, minute=0, second=5), context="1")
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
