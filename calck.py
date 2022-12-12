import telebot
import json 
from   logger import *

API_TOKEN = '5578103165:AAHyR0AZbJEJiiPa6lD8FoFOnUeVAAeXgVM'
bot = telebot.TeleBot(API_TOKEN)

calc = False

films = []

@bot.message_handler(commands=['calc'])
def calc_message(message):
    global calc
    # eq = message.text.split()[1:]
    calc = True
    bot.send_message(message.chat.id, 'А теперь введите выражение')

@bot.message_handler(content_types='text')
def message_reply(message):
    log(message)
    global calc
    if calc :
       bot.send_message(message.chat.id, eval(message.text))

       calc = False

bot.polling()