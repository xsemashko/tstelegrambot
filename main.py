#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import config
import os

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

# keyboard
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Прошивки")
    item2 = types.KeyboardButton("Спецификации")
    item3 = types.KeyboardButton("Программы и утилиты")
    item4 = types.KeyboardButton("Приложения и кинотеатры")
    item5 = types.KeyboardButton("Удаленное управлене")
    item6 = types.KeyboardButton("Техническая поддержка")
    item7 = types.KeyboardButton("Приобрести оборудование")
    item8 = types.KeyboardButton("Тестирование")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

    bot.send_message(message.chat.id, "Выберите интересующий Вас раздел:", reply_markup=markup)

# RUN
bot.polling(none_stop=True)