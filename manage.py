from config import token, database_url
from general_code import Timetable
from display_cart import display_schedule
#from reply_keyboard_markups import Keyboard

from flask import Flask, request
import datetime
import telebot
import os


#server = Flask(__name__)

bot = telebot.TeleBot(token)
#keyboard = Keyboard(bot)

@bot.message_handler(commands=['start'])
def handle_text(message):
	user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
	user_markup.row('Получить расписание на сегодня')
	user_markup.row('Обратная связь')
	bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=user_markup)


@bot.message_handler(func=lambda mess: "Обратная связь" == mess.text, content_types=['text'])
def handle_text(message):
	bot.send_message(message.chat.id, 'По вопросам и предложениям:\n \n')


@bot.message_handler(func=lambda mess: 'Получить расписание на сегодня' == mess.text, content_types=['text'])
def handle_text(message):
	cartoons = Timetable(database_url).get_cartoons(datetime.date(2017, 10, 26))
	cartoons = [cartoons[key] for key in sorted(cartoons.keys())]
	bot.send_message(message.chat.id, display_schedule(cartoons), 'HTML')


@server.route('/' + token, methods=['POST'])
def get_message():
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	return "POST", 200


@server.route("/")
def web_hook():
	bot.remove_webhook()
	bot.set_webhook(url='https://lit-reaches-12820.herokuapp.com/' + token)
	return "CONNECTED", 200

if __name__ == '__main__':
	server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
	#cartoons = Timetable(database_url).get_cartoons(datetime.date(2017, 10, 26))
	#cartoons = [cartoons[key] for key in sorted(cartoons.keys())]
	#print(display_schedule(cartoons))