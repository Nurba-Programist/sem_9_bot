
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def log(message):
    file = open('db.csv','a')
    file.write(f'{message.text} = {eval(message.text)}\n')
    file.close()