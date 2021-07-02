import keyboard as kb
import settings


def main_menu(update, context):
    update.message.reply_text('Main menu',
                              reply_markup=kb.main_menu)
    return 'main_menu'


def dt_from_key(update, context):
    update.message.reply_text('Ok. Give me key value',
                              reply_markup=kb.post_task)
    return 'dt_from_key'


def dt_from_ts(update, context):
    update.message.reply_text('Ok. Give me timestamp (int/float)',
                              reply_markup=kb.post_task)
    return 'dt_from_ts'


def post_task(update, context):
    task_types = "\n".join(settings.TASK_TYPES)
    update.message.reply_text(f'select task type\n{task_types}',
                              reply_markup=kb.post_task)
    return 'post_task'
