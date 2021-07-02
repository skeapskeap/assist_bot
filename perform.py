import keyboard as kb


def post_task(update, context):
    task = update.message.text
    # POST HTTP here
    update.message.reply_text(f'Task posted\n{task}',
                              reply_markup=kb.post_task)
    return 'post_task'
