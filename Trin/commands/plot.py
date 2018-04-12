from pandas import DataFrame
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from utils import SaveLoadObj
from telegram import ParseMode
import datetime
from utils.VET import datetimeVen, horaVen
from telegram import ParseMode
import math

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
    if len(args) != 1 or args[0] not in ['day', 'week', 'month', 'year', 'all']:
        args = ['']
        args[0] = 'month'

    #Dark Background
    plt.style.use('dark_background')
    # https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python
    fig, ax = plt.subplots()

    if args[0] == 'day':
        datemin = datetimeVen() - datetime.timedelta(days=1)
        datemax = datetimeVen()
        ax.xaxis.set_major_locator(days)
        ax.xaxis.set_major_formatter(daysFmt)
        ax.xaxis.set_minor_locator(hours)
    elif args[0] == 'week':
        datemin = datetimeVen()- datetime.timedelta(days= 7)
        datemax = datetimeVen()
        ax.xaxis.set_major_locator(days)
        ax.xaxis.set_major_formatter(daysFmt)
    elif args[0] == 'month':
        datemin = datetimeVen()- datetime.timedelta(days=30)
        datemax = datetimeVen()
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(monthsFmt)
        ax.xaxis.set_minor_locator(days)
        ax.xaxis.set_minor_formatter(mdates.DateFormatter('%d'))
    elif args[0] == 'year':
        datemin = datetimeVen()- datetime.timedelta(days=365)
        datemax = datetimeVen()
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(yearsFmt)
        ax.xaxis.set_minor_locator(months)
        ax.xaxis.set_minor_formatter(monthsFmt)
    elif args[0] == 'all':
        datemin = datetime.date(2010, 6, 23)
        datemax = datetimeVen()
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(yearsFmt)
        ax.xaxis.set_minor_locator(months)
    else:
        wrongInput(bot, update)
        return

    # Enable Grid
    plt.grid(True, which="both", alpha=0.7)
    # Y-axis log scale
    plt.yscale('log')
    # Labels for the plot
    plt.xlabel("Date")
    plt.ylabel("VEF/USD")
    # Value limits of axis x
    ax.set_xlim(datemin, datemax)
    ax.format_xdata = mdates.DateFormatter('%Y/%m/%d')
    # Loading DolarToday data to plot
    toPlot = SaveLoadObj.load_obj("DTlist")
    df = DataFrame(toPlot)
    # Finding y lims
    indexOfDatemin = df[df['date'] == datemin].index[0]
    # indexOfDatemax = df[df['date'] == datemax].index[0]
    indexOfDatemax = len(df) - 1
    minV = -1
    maxV = -1
    vals = []
    for i in range(indexOfDatemin, indexOfDatemax + 1):
        vals.append(df.at[i, 'DolarToday'])
    # EJ: int(str(410543.45)[0] is simply 4. That times 10^: math.log10(410543.45) is 5.something. Floor it and you have 5; 10^5.
    # Therefore 4*10^5
    minV = int(str(min(vals))[0])*10**math.floor(math.log10(min(vals)))
    # EJ: 410543.45%10 is  4.1.... ceil it; 5. that times 10^: math.log10(410543.45) is 5.something. Floor it and you have 5; 10^5.
    # Therefore 5*10^5
    maxV = math.ceil(max(vals)%10)*10**math.floor(math.log10(max(vals)))
    # Value limits of axis y
    plt.ylim(minV, maxV)
    #Reformatting y axis value ticks
     #ax.ticklabel_format(style='plain', axis='y')
    # Plotting
    df.plot(x='date', y='DolarToday', ax=ax, color="yellow")
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
    #Sending it
    caption = "*BETA FEATURE: still in progress*\n" + horaVen()
    bot.send_photo(chat_id=update.message.chat_id, photo=open('data/plot.png', 'rb'), caption=caption, parse_mode=ParseMode.MARKDOWN, reply_to_message_id=update.message.message_id)

    # If len args is not 2 ej /plot or /plot dolar or /plot very long sentence
def wrongInput(bot, update):
    toPrint = "*Correct usage of /plot@trinbot is as follows:*\n\n" \
              "`/plot@trinbot <arg1> <arg2>` where `<arg1>` can be either `dolartoday` or `localbtc` and `<arg2>`" \
              " can be: `day`, `week`, `month`, `year` or `all`"
    bot.send_message(chat_id=update.message.chat_id, text=toPrint, parse_mode=ParseMode.MARKDOWN,
                     reply_to_message_id=update.message.message_id)

