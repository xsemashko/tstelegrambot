#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
import config
import os
import dbworker
import requests
from telebot import types
import urllib.request
from os import path

bot = telebot.TeleBot(config.TOKEN)

user_final_data = ""

@bot.message_handler(commands=['start'])
@bot.message_handler(regexp="^Вернуться в главное меню.$")
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
    dbworker.set_state(message.chat.id, config.States.S_DISABLED.value)

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

@bot.message_handler(regexp="^IPTV приставки$")
def iptvconsole(message):

# keyboard
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("Redbox Mini 3L_")
    item2 = types.KeyboardButton("Redbox Mini 5PRO_")
    item3 = types.KeyboardButton("Назад в тех. документацию")

    markup.add(item1, item2, item3)
    
    bot.send_message(message.chat.id, "Выберите модель устройства:", reply_markup=markup)
    pass

@bot.message_handler(regexp="^Redbox Mini (3L_|5PRO_)$")
def myfunction(message):
    
    if message.text == 'Redbox Mini 3L_':
	    bot.send_message(message.chat.id, "Спецификация_3L_.pdf")
    if message.text == 'Redbox Mini 5PRO_':
	    bot.send_message(message.chat.id, "Спецификация_5PRO_.pdf")
    pass

@bot.message_handler(regexp="^Обновление и перепрошивка$")
def myfunction(message):
	bot.send_message(message.chat.id, "Как перепрошить.pdf")
	pass

@bot.message_handler(regexp="^Презентации и промо$")
def myfunction(message):
	bot.send_message(message.chat.id, "Файлы.rar")
	pass

@bot.message_handler(regexp="^Назад")
def backfunction(message):

    if message.text == 'Назад в гл.меню':
        welcome(message)
    if message.text == 'Назад в прошивки':
        software(message)
    if message.text == 'Назад в Порталы и платформы':
        portalsandplatforms(message)
    if message.text == 'Назад в тех. документацию':
        techdoc(message)
    pass
#Начало блока кастомизации
@bot.message_handler(commands=['customize'])
def cmd_start(message):
    global user_final_data
    user_final_data = ""
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Redbox Mini 3L.")
    item2 = types.KeyboardButton("Redbox Mini 5PRO.")
    item3 = types.KeyboardButton("Отменить кастомизацию.")
    keyboard.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выберите модель:", reply_markup=keyboard)
    dbworker.set_state(message.chat.id, config.States.S_SET_MAIN_APP.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SET_MAIN_APP.value)
def cmd_set_mainapp(message):
    global user_final_data
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("IPTVPORTAL.")
        item2 = types.KeyboardButton("24 ТВ.")
        item3 = types.KeyboardButton("СМОТРЕШКА.")
        item4 = types.KeyboardButton("MOOVIE TV.")
        item5 = types.KeyboardButton("MICROIM PULSE.")
        item6 = types.KeyboardButton("PEERS TV.")
        item7 = types.KeyboardButton("Используется плейлист.")
        item8 = types.KeyboardButton("Отменить кастомизацию.")
        keyboard.add(item1, item2, item3, item4, item5, item6, item7, item8)

        bot.send_message(message.chat.id, "Выберите основное приложени:", reply_markup=keyboard)
        user_final_data = user_final_data + "Модель: " + message.text.rstrip(".") + "\n"
        #Тут надо предусмотреть разветвление
        dbworker.set_state(message.chat.id, config.States.S_SET_LAUNCHE.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SET_LAUNCHE.value)
def cmd_set_launcher(message):
    global user_final_data
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        if message.text == "Используется плейлист.":
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("IPTV (Sofronov) Автозапуск.")
            item2 = types.KeyboardButton("IPTV (Sofronov) Рабочий стол.")
            item3 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1, item2, item3)
            bot.send_message(message.chat.id, "Выберите тип запуска приложения:", reply_markup=keyboard)
            user_final_data = user_final_data + "Основное приложение: " + message.text + "\n"
            dbworker.set_state(message.chat.id, config.States.S_SET_ONL_CINEMA.value)
        else:
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Лаучер.")
            item2 = types.KeyboardButton("Автозапуск.")
            item3 = types.KeyboardButton("Рабочий стол.")
            item4 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "Выберите тип запуска приложения:", reply_markup=keyboard)
            user_final_data = user_final_data + "Основное приложение: " + message.text.rstrip(".") + "\n"
            dbworker.set_state(message.chat.id, config.States.S_SET_ONL_CINEMA.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SET_ONL_CINEMA.value)
def cmd_set_online_cinema(message):
    global user_final_data
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("MEGOGO.")
        item2 = types.KeyboardButton("IVI.")
        item3 = types.KeyboardButton("TVZAVR.")
        item4 = types.KeyboardButton("START.")
        item5 = types.KeyboardButton("MEDIATEKA.")
        item6 = types.KeyboardButton("НЕ НУЖНО.")
        item7 = types.KeyboardButton("Отменить кастомизацию.")
        keyboard.add(item1, item2, item3, item4, item5, item6, item7)
        bot.send_message(message.chat.id, "Выберите онлайн-кинотеатр:", reply_markup=keyboard)
        user_final_data = user_final_data + "Тип запуска основного приложения: "  + message.text.rstrip(".") + "\n"
        dbworker.set_state(message.chat.id, config.States.S_SET_CINEMA_LAUNCH.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SET_CINEMA_LAUNCH.value)
def cmd_set_cinema_launch(message):
    global user_final_data
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        if message.text != "НЕ НУЖНО.":
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Рабочий стол.")
            item2 = types.KeyboardButton("Автозапуск.")
            item3 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1, item2, item3)
            bot.send_message(message.chat.id, "Выберите тип запуска:", reply_markup=keyboard)
            user_final_data = user_final_data + "Онлайн-кинотеатр: " + message.text.rstrip(".") + "\n"
            dbworker.set_state(message.chat.id, config.States.S_SET_ADD_APP.value)
        else:
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Далее")
            item2 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1, item2)
            user_final_data = user_final_data + "Онлайн-кинотеатр: " + message.text.rstrip(".") + "\n"
            bot.send_message(message.chat.id, "Онлайн-кинотеатр не будет включен в прошивку, нажмите далее", reply_markup=keyboard)
            dbworker.set_state(message.chat.id, config.States.S_SET_ADD_APP.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SET_ADD_APP.value)
def cmd_set_addon_app(message):
    global user_final_data
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("SMARTYOUTUBETV.")
        item2 = types.KeyboardButton("WEATHER.")
        item3 = types.KeyboardButton("OPERA.")
        item4 = types.KeyboardButton("НЕ НУЖНО.")
        item5 = types.KeyboardButton("Отменить кастомизацию.")
        keyboard.add(item1, item2, item3, item4, item5)
        bot.send_message(message.chat.id, "Выберите дополнительное приложение:", reply_markup=keyboard)
        if message.text != "Далее":
            user_final_data = user_final_data + "Метод запуска онлайн-кинотеатра: " + message.text.rstrip(".") + "\n"
        dbworker.set_state(message.chat.id, config.States.S_CUSTOMIZE_SETT.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_CUSTOMIZE_SETT.value)
def cmd_set_addon_app(message):
    global user_final_data
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("НЕ НУЖНЫ.")
        item2 = types.KeyboardButton("НУЖНЫ.")
        item3 = types.KeyboardButton("Отменить кастомизацию.")
        keyboard.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Нужны ли изменения настроек?", reply_markup=keyboard)
        user_final_data = user_final_data + "Дополнительные приложения: " + message.text.rstrip(".") + "\n"
        dbworker.set_state(message.chat.id, config.States.S_WRITE_ABOUT_CHANGES.value)
        if message.text != "НЕ НУЖНО.":
            dbworker.set_state(message.chat.id, config.States.S_WRITE_ABOUT_CHANGES.value)
        else:
            dbworker.set_state(message.chat.id, config.States.S_START_GRAPH.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_WRITE_ABOUT_CHANGES.value)
def cmd_write_about_changes(message):
    global user_final_data
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        if message.text != "НЕ НУЖНО.":
            bot.send_message(message.chat.id, "Напишите какие изменения необходимы.")
            #user_final_data = user_final_data + message.text
            dbworker.set_state(message.chat.id, config.States.S_START_GRAPH.value)
        else:
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Далее")
            item2 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1, item2)
            #user_final_data = user_final_data + message.text
            bot.send_message(message.chat.id, "Нажмите Далее, чтобы продолжить или Отменить", reply_markup=keyboard)
            dbworker.set_state(message.chat.id, config.States.S_START_GRAPH.value) 	

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_START_GRAPH.value)
def cmd_choose_start_graphic(message):
    global user_final_data
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("Логотип .png.")
        item2 = types.KeyboardButton("Анимация .mp4.")
        item3 = types.KeyboardButton("Отменить кастомизацию.")
        keyboard.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Выберите графику при включении приставки:", reply_markup=keyboard)
        if message.text != "Далее":
            user_final_data = user_final_data + "Необходимы следующие изменения: \n" + message.text + "\n"
        dbworker.set_state(message.chat.id, config.States.S_CHOOSE_DL_METH_GP.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_CHOOSE_DL_METH_GP.value)
def cmd_choose_start_graphic(message):
    global user_final_data
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Отменить кастомизацию.")
    keyboard.add(item1)
    bot.send_message(message.chat.id, "Пришлите документом файл в выбранном формате или нажмите Отмену", reply_markup=keyboard)
    user_final_data = user_final_data + "Графика при запуске приставки:" + message.text.rstrip(".") + "\n"
    dbworker.set_state(message.chat.id, config.States.S_WALLPAPER.value)

@bot.message_handler(content_types=['document'])
def cmd_choose_wallpaper(message):
    global user_final_data
    if dbworker.get_current_state(message.chat.id) == config.States.S_WALLPAPER.value:
        file_info = bot.get_file(message.document.file_id)
        #file_name = message.from_user.username + message.document.file_name
        #file_path = path.relpath("user_files/"+file_name)
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("Своя.")
        item2 = types.KeyboardButton("Стандартная.")
        item3 = types.KeyboardButton("Отменить кастомизацию.")
        keyboard.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Выберете заставку рабочего стола:", reply_markup=keyboard)
        url = 'https://api.telegram.org/file/bot{0}/{1}'.format(config.TOKEN, file_info.file_path)
        user_final_data = user_final_data + url + "\n"
        dbworker.set_state(message.chat.id, config.States.S_CHOOSE_DL_M_WALLPAPER.value)
        #file_url = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(config.TOKEN, file_info.file_path))
        #resource = urllib.request.urlopen('https://api.telegram.org/file/bot{0}/{1}'.format(config.TOKEN, file_info.file_path))
        #output = open(file_path, "wb")
        #output.write(resource.read())
        #output.close()
    if dbworker.get_current_state(message.chat.id) == config.States.S_DOWNLOAD_WALLPAPER.value:
        file_info = bot.get_file(message.document.file_id)
        url = 'https://api.telegram.org/file/bot{0}/{1}'.format(config.TOKEN, file_info.file_path)
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("Отменить кастомизацию.")
        keyboard.add(item1)
        bot.send_message(message.chat.id, "Оставьте контактные данные и нажмите Далее", reply_markup=keyboard)
        user_final_data = user_final_data + url + "\n"
        dbworker.set_state(message.chat.id, config.States.S_FINAL.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_CHOOSE_DL_M_WALLPAPER.value)
def cmd_choose_start_graphic(message):
    global user_final_data
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        if message.text == "Своя.":
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1)
            bot.send_message(message.chat.id, "Загрузите заставку 1920x1080 .png", reply_markup=keyboard)
            user_final_data = user_final_data + "Заставка для рабочего стола: " + message.text.rstrip(".") + "\n"
            dbworker.set_state(message.chat.id, config.States.S_DOWNLOAD_WALLPAPER.value)
        if message.text != "Своя.":
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Далее.")
            item2 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1, item2)
            bot.send_message(message.chat.id, "Оставьте контактные данные или нажмите Отменить", reply_markup=keyboard)
            user_final_data = user_final_data + "Заставка для рабочего стола: " + message.text.rstrip(".") + "\n"
            dbworker.set_state(message.chat.id, config.States.S_FINAL.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_FINAL.value)
def cmd_choose_start_graphic(message):
    global user_final_data
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("Вернуться в главное меню.")
        keyboard.add(item1)
        user_name = message.from_user.username
        user_final_data = user_final_data + "Имя пользователя: " + user_name + "\n" + "Контактные данные: " + message.text + "\n"
        bot.send_message(message.chat.id, "Вы завершили кастомизацию, в ближайшее время с Вами свяжутся",  reply_markup=keyboard)
        dbworker.set_state(message.chat.id, config.States.S_DISABLED.value)
        output = open("file01.txt", "w")
        output.write(user_final_data)
        output.close()

@bot.message_handler(commands=['reset'])
@bot.message_handler(regexp="^Отменить кастомизацию.$")
def cmd_reset(message):
    global user_final_data
    bot.send_message(message.chat.id, "Cancel")
    user_final_data = ""
    dbworker.set_state(message.chat.id, config.States.S_DISABLED.value)
    welcome(message)
#Конец блока кастомизации
# RUN
bot.polling(none_stop=True)