from telegram import ReplyKeyboardMarkup

start = ReplyKeyboardMarkup(keyboard=[['start']],
                            resize_keyboard=True)
main_menu = ReplyKeyboardMarkup(keyboard=[['task', 'post_task', 'dt_from_key', 'dt_from_ts']],
                                resize_keyboard=True)
post_task = ReplyKeyboardMarkup(keyboard=[['to_menu']],
                                resize_keyboard=True)
