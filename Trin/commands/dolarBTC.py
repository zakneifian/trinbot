# TODO format better the message to be printed
# TODO think if keeping the if block or implementing other way (like loop for len(args[0]))
from utils.USDVEF import getDollar
from utils.VET import horaVen
from telegram import ParseMode

# Command to print the dollar value.
def dolarBTC(bot, update, args):

    # Venezuela's Standard Time (VET)
    display = horaVen()


    try:
        # if someone uses '/dolarBTC' return avg_12h.
        if len(args) == 0:
            toPrint = "*$1 = Bs. {0:.2f} \n{1}*".format(getDollar("12"), display)
        # if someone uses 'dolarBTC <arg1>' try to return <arg1>, else exception.
        elif len(args) == 1 and args[0] != "all":
            toPrint = "*$1 = Bs. {0:.2f} \n{1}*".format(getDollar(args[0]), display)
        elif len(args) == 1 and args[0] == "all":
            dolArr = getDollar("all")
            toPrint =   "*Average 1h:*  $1 = Bs. {0:.2f}" \
                      "\n*Average 6h:*  $1 = Bs. {1:.2f}" \
                      "\n*Average 12h:* $1 = Bs. {2:.2f}" \
                      "\n*Average 24h:* $1 = Bs. {3:.2f}" \
                      "\n{4}".format(dolArr[0], dolArr[1], dolArr[2], dolArr[3], display)
        # if someone uses 'dolarBTC <arg1> <arg2>' try to return <arg1> times <arg2>, else exception.
        elif len(args) == 2 and args[0] != "all":
            toPrint = "*${2} = Bs. {0:.2f}* " \
                      "\nUTC: {1}".format(getDollar(args[0]) * float(args[1]), display, float(args[1]))
        elif len(args) == 2 and args[0] == "all":
            dolArr = [i * float(args[1]) for i in getDollar("all")]
            toPrint =   "*Average 1h:*  ${5} = Bs. {0:.2f} " \
                      "\n*Average 6h:*  ${5} = Bs. {1:.2f} " \
                      "\n*Average 12h:* ${5} = Bs. {2:.2f} " \
                      "\n*Average 24h:* ${5} = Bs. {3:.2f} " \
                      "\n{4}".format(dolArr[0], dolArr[1], dolArr[2], dolArr[3], display, float(args[1]))

        bot.send_message(chat_id=update.message.chat_id, text=toPrint, parse_mode=ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

    except:
        toPrint = "The correct usage of the command is as follows:" \
                  "\n`/dolarBTC` - returns the localbitcoins 12h average of the price of the VEF" \
                  "\n`/dolarBTC <arg1>` - returns one or all of the values for that argument, where `<arg1>` can be either: `1`, `6`, `12`, `24` or `all`." \
                  "\n`/dolarBTC <arg1> <arg2>` - same as the previous example except that the value will not reference $1 but the amount in `<arg2>`. For example: `/dolarBTC all 100`. This will return `$100 = Bs. ...` " \
                  "for all averages"
        bot.send_message(chat_id=update.message.chat_id, text=toPrint, parse_mode=ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)