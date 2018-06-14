import os

from telegram.ext import Updater
from telegram.ext import CommandHandler

from create_exersise import create_ten_random_exercise


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=f"{create_ten_random_exercise()}")


def polling():
    updater = Updater(token=os.environ.get('TOKEN'))
    start_handler = CommandHandler('start', start) 
    updater.dispatcher.add_handler(start_handler) 
    updater.start_polling() 
