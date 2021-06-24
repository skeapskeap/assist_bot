from datetime import datetime as dt
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Filters
from telegram.ext import MessageHandler
import logging
import settings

menu_keyboard = ReplyKeyboardMarkup(
                    [['task']],
                    resize_keyboard=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def send_ts(update, context):
    timestamp = dt.utcnow().isoformat()
    time_now = str(int(dt.utcnow().timestamp() * 1000) - int(dt(2021, 1, 1).timestamp() * 1000))
    update.message.reply_text(f'{timestamp = !s}\nkey = {time_now}',
                              reply_markup=menu_keyboard)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher

    dp.add_handler(MessageHandler(Filters.regex('task'), send_ts))
    print('Bot is now running')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
