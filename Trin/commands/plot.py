from pandas import DataFrame
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from utils import SaveLoadObj
from telegram import ParseMode
import datetime
from utils.VET import datetimeVen
from telegram import ParseMode
from PIL import Image
import PIL.ImageOps
import random

# Path of data to plot
path = ""
# Datetime objects
datemin = ""
datemax = ""
#Locator
years = mdates.YearLocator()    # every year
months = mdates.MonthLocator()  # every month
days = mdates.DayLocator()      # every day
hours = mdates.HourLocator()    #every hour
# Date formatter
yearsFmt = mdates.DateFormatter('%Y')
monthsFmt = mdates.DateFormatter('%b')
daysFmt = mdates.DateFormatter('%a')

def plot(bot, update, args):
    # if /plot has <arg1> and <arg2>
    if len(args) != 2:
        foo = ['day', 'week', 'month', 'year', 'all']
        plot(bot, update, ["dolartoday", random.choice(foo)])


    fig, ax = plt.subplots()
    #Tilting the x axis

    if args[0] == 'dolartoday':
        path = "DTlist"

    if args[1] == 'day':
        datemin = datetimeVen() - datetime.timedelta(days=1)
        datemax = datetimeVen()
        ax.xaxis.set_major_locator(days)
        ax.xaxis.set_major_formatter(daysFmt)
        ax.xaxis.set_minor_locator(hours)
    elif args[1] == 'week':
        datemin = datetimeVen()- datetime.timedelta(days= 7)
        datemax = datetimeVen()
        ax.xaxis.set_major_locator(days)
        ax.xaxis.set_major_formatter(daysFmt)
    elif args[1] == 'month':
        datemin = datetimeVen()- datetime.timedelta(days=30)
        datemax = datetimeVen()
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(monthsFmt)
        ax.xaxis.set_minor_locator(days)
        ax.xaxis.set_minor_formatter(mdates.DateFormatter('%d'))
    elif args[1] == 'year':
        datemin = datetimeVen()- datetime.timedelta(days=365)
        datemax = datetimeVen()
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(yearsFmt)
        ax.xaxis.set_minor_locator(months)
        ax.xaxis.set_minor_formatter(monthsFmt)
    elif args[1] == 'all':
        datemin = datetime.date(2010, 1, 1)
        datemax = datetimeVen()
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(yearsFmt)
        ax.xaxis.set_minor_locator(months)
    else:
        wrongInput(bot, update)
        return

    # Enable Grid
    plt.grid(True, which="both")
    # Y-axis log scale
    plt.yscale('log')
    # Labels for the plot
    plt.xlabel("Date")
    plt.ylabel("VEF/USD")
    #Value limits of axis
    ax.set_xlim(datemin, datemax)
    ax.format_xdata = mdates.DateFormatter('%Y/%m/%d')
    # Loading data to plot
    toPlot = SaveLoadObj.load_obj(path)
    df = DataFrame(toPlot)
    # Plotting
    df.plot(x='date', y='price', ax=ax)
    #Format and tilt x axis dates
    fig.autofmt_xdate(which='both', rotation=50)
    #Lower major formatter to not collide with the minor one
    for tick in ax.xaxis.get_major_ticks():
        tick.tick1line.set_markersize(2)
        tick.tick2line.set_markersize(2)
        tick.set_pad(4 * tick.get_pad())
    #Saving plot
    plt.savefig("data/plot.png", dpi=300, orientation='landscape', bbox_inches='tight', pad_inches=0.01)
    #Ensure that the fig is closed
    plt.close(fig)
    #Inverting the photo
    image = Image.open('data/plot.png')
    if image.mode == 'RGBA':
        r, g, b, a = image.split()
        rgb_image = Image.merge('RGB', (r, g, b))

        inverted_image = PIL.ImageOps.invert(rgb_image)

        r2, g2, b2 = inverted_image.split()

        inverted_image = Image.merge('RGBA', (r2, g2, b2, a))


    else:
        inverted_image = PIL.ImageOps.invert(image)
    #Sending it
    caption = "*BETA FEATURE: still in progress*\n"
    bot.send_photo(chat_id=update.message.chat_id, photo=inverted_image, caption=caption, parse_mode=ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

    # If len args is not 2 ej /plot or /plot dolar or /plot very long sentence
def wrongInput(bot, update):
    toPrint = "*Correct usage of /plot@trinbot is as follows:*\n\n" \
              "`/plot@trinbot <arg1> <arg2>` where `<arg1>` can be either `dolartoday` or `localbtc` and `<arg2>`" \
              " can be: `day`, `week`, `month`, `year` or `all`"
    bot.send_message(chat_id=update.message.chat_id, text=toPrint, parse_mode=ParseMode.MARKDOWN,
                     reply_to_message_id=update.message.message_id)

