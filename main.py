#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import config
import os

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    FILEID = 'BAACAgIAAxkDAAIBxl5lH2r1r05dKYn6CzQlrGMZVmvkAAIrBwAC81coSwEmYV_wTwp4GAQ'
    
# keyboard
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Прошивки")
    item2 = types.KeyboardButton("Техническая документация")
    item3 = types.KeyboardButton("Программы и утилиты")
    item4 = types.KeyboardButton("Приложения и кинотеатры")
    item5 = types.KeyboardButton("Удаленное управлене")
    item6 = types.KeyboardButton("Техническая поддержка")
    item7 = types.KeyboardButton("Приобрести оборудование")
    item8 = types.KeyboardButton("Тестирование")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    
    bot.send_video(message.chat.id, FILEID, reply_markup=markup)
    #bot.send_message(message.chat.id, "Выберите интересующий Вас раздел:", reply_markup=markup)

@bot.message_handler(regexp="^Прошивки$")
def software(message):

# keyboard
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Порталы и платформы")
    item2 = types.KeyboardButton("Прошивки для операторов")
    item3 = types.KeyboardButton("Стоковая прошивка")
    item4 = types.KeyboardButton("Кастомизация")
    item5 = types.KeyboardButton("Назад в гл.меню")

    markup1.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Выберите интересующую категорию", reply_markup=markup1)
    pass

@bot.message_handler(regexp="^Порталы и платформы$")
def portalsandplatforms(message):

# keyboard
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("Redbox")
    item2 = types.KeyboardButton("Назад в прошивки")

    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, "Выберите производителя:", reply_markup=markup)
    pass

@bot.message_handler(regexp="^Redbox$")
def redboxvendor(message):

# keyboard
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("Redbox Mini 3L")
    item2 = types.KeyboardButton("Redbox Mini 5PRO")
    item3 = types.KeyboardButton("Назад в Порталы и платформы")

    markup.add(item1, item2, item3)
    
    bot.send_message(message.chat.id, "Выберите модель устройства:", reply_markup=markup)
    pass


@bot.message_handler(regexp="^Техническая документация$")
def techdoc(message):

# keyboard
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("IPTV приставки")
    item2 = types.KeyboardButton("Обновление и перепрошивка")
    item3 = types.KeyboardButton("Презентации и промо")
    item4 = types.KeyboardButton("Назад в гл.меню")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Выберите интересующую категорию", reply_markup=markup)
    pass

@bot.message_handler(regexp="^Назад")
def backfunction(message):

    if message.text == 'Назад в гл.меню':
        welcome(message)
    if message.text == 'Назад в прошивки':
        software(message)
    if message.text == 'Назад в Порталы и платформы':
        portalsandplatforms(message)
    pass

# RUN
bot.polling(none_stop=True)