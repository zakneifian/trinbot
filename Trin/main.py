from commands.Start import start
from commands.dolarBTC import dolarBTC
from commands.help import help
from commands.carlos import carlos
from commands.plot import plot
from noncommand.error import error
from noncommand.InlineQuery import inlinequery
from jobs.CalcDollar import setDollar
from jobs.updateDT import updateDT
from utils.TokenReader import readToken
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
import logging
import datetime
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
jobQ.run_repeating(setDollar, 300, first=0)
jobQ.run_daily(updateDT, datetime.time(hour=19, minute=0, second=0))
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
