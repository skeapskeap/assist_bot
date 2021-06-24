from datetime import datetime as dt
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Filters
from telegram.ext import MessageHandler, ConversationHandler
import logging
import settings

start_kb = ReplyKeyboardMarkup(keyboard=[['start']],
                               resize_keyboard=True)
main_menu_kb = ReplyKeyboardMarkup(keyboard=[['task', 'post_task']],
                                   resize_keyboard=True)
post_task_kb = ReplyKeyboardMarkup(keyboard=[['to_menu']],
                                   resize_keyboard=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
TASK_TYPES = ['/one', '/two']
task_mapping = {'one': 'value for task one',
                'two': 'value for task two'}


def send_ts(update, context):
    timestamp = dt.utcnow().isoformat()
    time_now = str(int(dt.utcnow().timestamp() * 1000) - int(dt(2021, 1, 1).timestamp() * 1000))
    update.message.reply_text(f'{timestamp = !s}\nkey = {time_now}',
                              reply_markup=main_menu_kb)


def select_task(update, context):
    task_types = "\n".join(TASK_TYPES)
    update.message.reply_text(f'select task type\n{task_types}',
                              reply_markup=post_task_kb)
    return 'post_task'


def wrong_input(update, context):
    update.message.reply_text('Invalid input')


def main_menu(update, context):
    update.message.reply_text(
        f"Main menu",
        reply_markup=main_menu_kb
    )
    return 'main_menu'


def start(update, context):
    update.message.reply_text('Press start to start',
                              reply_markup=start_kb)


def commands(update, context):
    task_type = update.message.text.replace('/', '')
    value = task_mapping.get(task_type)
    update.message.reply_text(f'Value for {task_type=}\n{value}',
                              reply_markup=post_task_kb)
    return 'post_task'


def post_task(update, context):
    task = update.message.text
    update.message.reply_text(f'Task posted\n{task}',
                              reply_markup=post_task_kb)
    return 'post_task'


conversation = ConversationHandler(
    entry_points=[
        MessageHandler(Filters.regex('^start$'), main_menu),
        MessageHandler(Filters.text, start)
    ],
    states={
        'main_menu': [
            MessageHandler(Filters.regex('^task$'), send_ts),
            MessageHandler(Filters.regex('^post_task$'), select_task)
        ],
        'post_task': [
            MessageHandler(Filters.regex('^task$'), send_ts),
            MessageHandler(Filters.regex('^to_menu$'), main_menu),
            MessageHandler(Filters.command, commands),
            MessageHandler(Filters.text, post_task)
        ]
    },
    fallbacks=[
        MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, wrong_input)
    ]
)


def main():
    bot = Updater(settings.API_KEY, use_context=True)
    dp = bot.dispatcher
    dp.add_handler(conversation)
    print('Bot is now running')
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
