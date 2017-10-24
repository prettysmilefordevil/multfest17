from config import token, database_url
from general_code import Timetable
from display_cart import display_schedule
#from reply_keyboard_markups import Keyboard

from flask import Flask, request
import datetime
import telebot
import os


server = Flask(__name__)

bot = telebot.TeleBot(token)
#keyboard = Keyboard(bot)

@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Получить расписание на сегодня')
    user_markup.row('Обратная связь')
    bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=user_markup)

@server.route('/' + token, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200


@server.route("/")
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url='https://lit-reaches-12820.herokuapp.com/' + token)
    return "CONNECTED", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))