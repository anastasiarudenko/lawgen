# -*- coding: utf-8 -*-

import telebot
from law_generator import *

bot = telebot.TeleBot("1044689502:AAE2Qtx0WoJC4QN6b_uCcIydA1VfLutF938")

keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('/gen', '/info')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.chat.first_name) + '\n\nЭто бот для генерации законов РФ\n(не настоящих)\n\nВ качестве основы были использованы:\n✓ Конституция\n✓ Уголовный кодекс\n✓ Семейный кодекс\n✓ Закон о СМИ\n✓ Федеральный закон о рекламе\n✓ Закон об оружии\n✓ Лесной кодекс\n✓ Закон о полиции\n✓ Федеральный закон о нацгвардии', reply_markup=keyboard1)

@bot.message_handler(commands=['gen'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, generate_sentence(model))
	
@bot.message_handler(commands=['info'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Данный бот выполнен в учебных целях студентами мехмата ЮФУ\n\nМы натренировали нейронную сеть для генерации законов на юридических текстах РФ\n\nРазмеченные данные для обучения Вы можете посмотреть здесь: https://drive.google.com/open?id=14MS5goZgfhP3lpJ3fQzJdI9nec9uTrFe\n\nВсё взято с сайта КонсультантПлюс: http://www.consultant.ru/popular/')
	
@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    bot.send_sticker(message.chat.id, 'CAADAgADDQADKA9qFEfZueCdJ1c-FgQ')
	
@bot.message_handler(content_types=['text'])
def send_text(message):
	bot.send_sticker(message.chat.id, 'CAADAgADmwkAAtV-vwG48op19XTYGBYE')

bot.polling()