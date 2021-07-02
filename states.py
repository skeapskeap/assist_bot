from telegram.ext import Filters
from telegram.ext import MessageHandler
import call
import reply
import perform

entry_points = [
    MessageHandler(Filters.regex('^start$'), call.main_menu),
    MessageHandler(Filters.text, reply.start)
]

main_menu = [
    MessageHandler(Filters.regex('^task$'), reply.task_key_and_ts),
    MessageHandler(Filters.regex('^dt_from_key'), call.dt_from_key),
    MessageHandler(Filters.regex('^dt_from_ts'), call.dt_from_ts),
    MessageHandler(Filters.regex('^post_task$'), call.post_task)
]

post_task = [
    MessageHandler(Filters.regex('^task$'), reply.task_key_and_ts),
    MessageHandler(Filters.regex('^to_menu$'), call.main_menu),
    MessageHandler(Filters.command, reply.commands),
    MessageHandler(Filters.text, perform.post_task)
]

dt_from_key = [
    MessageHandler(Filters.regex('^to_menu$'), call.main_menu),
    MessageHandler(Filters.text, reply.dt_from_key)
]

dt_from_ts = [
    MessageHandler(Filters.regex('^to_menu$'), call.main_menu),
    MessageHandler(Filters.text, reply.dt_from_ts)
]

fallbacks = [
    MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, reply.wrong_input)
]
