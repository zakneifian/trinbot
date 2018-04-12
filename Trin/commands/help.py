# TODO improve help command
from telegram import ParseMode

toPrint = "*Available Commands:*" \
          "\n• /start@trinbot - Starts the bot" \
          "\n• /help@trinbot - Sends help message with avaible commands and descriptions" \
          "\n• /dolarBTC@trinbot `<arg1> <arg2>` - if no arguments are passed, returns the localbitcoins 12h average of the price of the VEF." \
          "\n`/dolarBTC@trinbot <arg1>` - returns one or all of the values for that argument, where `<arg1>` can be either: `1`, `6`, `12`, `24` or `all`." \
          "\n`/dolarBTC@trinbot <arg1> <arg2>` - same as the previous example except that the value will not reference $1 but the amount in `<arg2>`. For example: `/dolarBTC all 100`. This will return `$100 = Bs. ...` for all averages." \
          "\n• /plot@trinbot `<arg1> <arg2>` - plots the historical data of `<arg1>` in the interval `<arg2>` valid values for `<arg1>` are: `dolartoday`. Valid values for `<arg2>` are: `day`, `week`, `month`, `year` or `all`" \
          "\n\n• Inline Query usage: if no query is passed, returns the value of the dollar, if number is passed, returns the number times the value of the dollar."

def help(bot, update):
	update.message.reply_text(text=toPrint, parse_mode=ParseMode.MARKDOWN)