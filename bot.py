from telegram.ext import Updater
from telegram.ext import ConversationHandler
import logging
import settings
import states


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
conversation = ConversationHandler(
    entry_points=states.entry_points,
    states={
        'main_menu': states.main_menu,
        'post_task': states.post_task,
        'dt_from_key': states.dt_from_key,
        'dt_from_ts': states.dt_from_ts
    },
    fallbacks=states.fallbacks
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
