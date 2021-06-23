from datetime import datetime as dt
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Filters
from telegram.ext import MessageHandler
import logging
import settings

menu_keyboard = ReplyKeyboardMarkup(
                    [['timestamp', 'key']],
                    resize_keyboard=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def send_timestamp(update, context):
    timestamp = dt.utcnow().isoformat()
    update.message.reply_text(timestamp,
                              reply_markup=menu_keyboard)


def send_key(update, context):
    time_now = str(int(dt.utcnow().timestamp() * 1000) - int(dt(2021, 1, 1).timestamp() * 1000))
    update.message.reply_text(time_now,
                              reply_markup=menu_keyboard)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher

    dp.add_handler(MessageHandler(Filters.regex('key'), send_key))
    dp.add_handler(MessageHandler(Filters.regex('timestamp'), send_timestamp))
    print('Bot is now running')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
