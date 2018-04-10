# Handle the inline query to return the avg_12h dollar
from utils.VET import horaVen
from utils.USDVEF import getDollar
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent


def inlinequery(bot, update):
    display = horaVen()
    query = update.inline_query.query
    dol12 = getDollar('12')
    if len(query) > 0:
        try:
            price = dol12*float(query)
            results = [
                InlineQueryResultArticle(
                    id=uuid4(),
                    title="Price of USD to VEF: " + "$" + query + " = Bs. {:.2f}".format(price),
                    input_message_content=InputTextMessageContent(
                        "*$" + query + " = Bs. {:.2f}*\n{}".format(price, display),
                        parse_mode=ParseMode.MARKDOWN))]
            update.inline_query.answer(results)
        except:
            results = [
                InlineQueryResultArticle(
                    id=uuid4(),
                    title="Price of USD to VEF: " + "$1 = Bs. {:.2f}".format(dol12),
                    input_message_content=InputTextMessageContent(
                        "*$1 = Bs. {:.2f}*\n{}".format(dol12, display),
                        parse_mode=ParseMode.MARKDOWN))]
            update.inline_query.answer(results)
    else:
        results = [
            InlineQueryResultArticle(
                id=uuid4(),
                title="Price of USD to VEF: " + "$1 = Bs. {:.2f}".format(dol12),
                input_message_content=InputTextMessageContent(
                    "*$1 = Bs. {:.2f}*\n{}".format(dol12, display),
                    parse_mode=ParseMode.MARKDOWN))]
        update.inline_query.answer(results)