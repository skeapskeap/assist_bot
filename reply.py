from datetime import datetime as dt
from tzlocal import get_localzone
import keyboard as kb
import settings


def start(update, context):
    update.message.reply_text('Press start to start',
                              reply_markup=kb.start)


def task_key_and_ts(update, context):
    timestamp = dt.utcnow().isoformat()
    time_now = str(int(dt.utcnow().timestamp() * 1000) - int(dt(2021, 1, 1).timestamp() * 1000))
    update.message.reply_text(f'{timestamp = !s}\nkey = {time_now}',
                              reply_markup=kb.main_menu)


def dt_from_ts(update, context):
    try:
        timestamp = float(update.message.text)
    except ValueError:
        update.message.reply_text('timestamp must be of type int',
                                  reply_markup=kb.post_task)
        return
    reply = dt.fromtimestamp(timestamp)
    update.message.reply_text(f'date of {timestamp} is {reply}',
                              reply_markup=kb.post_task)


def dt_from_key(update, context):
    try:
        key = int(update.message.text)
    except ValueError:
        update.message.reply_text('key must be of type int',
                                  reply_markup=kb.post_task)
        return
    task_ts = (key + int(dt(2021, 1, 1).timestamp() * 1000)) // 1000
    dt_utc = dt.fromtimestamp(task_ts)
    local_tz = get_localzone()
    offset = local_tz.utcoffset(dt_utc)
    dt_local = dt_utc + offset
    update.message.reply_text(f'task timestamp utc: {dt_utc}\ntask timestamp local: {dt_local}',
                              reply_markup=kb.post_task)


def commands(update, context):
    task_type = update.message.text.replace('/', '')
    value = settings.task_mapping.get(task_type)
    update.message.reply_text(f'Value for {task_type=}\n{value}',
                              reply_markup=kb.post_task)
    return 'post_task'


def wrong_input(update, context):
    update.message.reply_text('Invalid input')
