#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
import config
import dbworker
import requests
from telebot import types
import urllib.request
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3

bot = telebot.TeleBot(config.TOKEN)

sender_email = "telegrambottechsane"
receiver_email = "ollien_sk8@mail.ru"
password = config.E_PASSWD

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
    item5 = types.KeyboardButton("Удаленное управление")
    item6 = types.KeyboardButton("Техническая поддержка")
    item7 = types.KeyboardButton("Приобрести оборудование")
    item8 = types.KeyboardButton("Тестирование")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    
    bot.send_video(message.chat.id, FILEID, reply_markup=markup)
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
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("Redbox Mini 3L")
    item2 = types.KeyboardButton("Redbox Mini 5PRO")
    item3 = types.KeyboardButton("Назад в Порталы и платформы")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выберите модель устройства:", reply_markup=markup)
    pass

@bot.message_handler(regexp="^Redbox Mini 3L$")
def redboxminil(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("IPTVPORTAL")
    item2 = types.KeyboardButton("24 ТВ")
    item3 = types.KeyboardButton("СМОТРЕШКА")
    item4 = types.KeyboardButton("MOOVI TV")
    item5 = types.KeyboardButton("MICROIMPULS")
    item6 = types.KeyboardButton("PEERS TV")
    item7 = types.KeyboardButton("Назад в Порталы и платформы")
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.send_message(message.chat.id, "Выберите приложение:", reply_markup=markup)
    dbworker.set_state(message.chat.id, config.States.P_REDBOX3L_APP.value)
    pass

@bot.message_handler(regexp="^Redbox Mini 5PRO$")
def redboxminil(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("IPTVPORTAL")
    item2 = types.KeyboardButton("24 ТВ")
    item3 = types.KeyboardButton("СМОТРЕШКА")
    item4 = types.KeyboardButton("MOOVI TV")
    item5 = types.KeyboardButton("MICROIMPULS")
    item6 = types.KeyboardButton("PEERS TV")
    item7 = types.KeyboardButton("Назад в Порталы и платформы")
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.send_message(message.chat.id, "Выберите приложение:", reply_markup=markup)
    dbworker.set_state(message.chat.id, config.States.P_REDBOX5PRO_APP.value)
    pass

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.P_REDBOX3L_APP.value)
def cmd_choose_appforl(message):
    if message.text == "Назад в Порталы и платформы":
        portalsandplatforms(message)
        dbworker.set_state(message.chat.id, config.States.S_DISABLED.value)
    elif message.text == "IPTVPORTAL":
        bot.send_message(message.chat.id, "IPTVPORTAL Автозупуск Файл рар")
        bot.send_message(message.chat.id, "IPTVPORTAL Лаунчер Файл рар")
    elif message.text == "24 ТВ":
        bot.send_message(message.chat.id, "24 ТВ Автозупуск Файл рар")
        bot.send_message(message.chat.id, "24 ТВ Лаунчер Файл рар")
    elif message.text == "СМОТРЕШКА":
        bot.send_message(message.chat.id, "СМОТРЕШКА Автозупуск Файл рар")
        bot.send_message(message.chat.id, "СМОТРЕШКА Лаунчер Файл рар")
    elif message.text == "MOOVI TV":
        bot.send_message(message.chat.id, "MOOVI TV Автозупуск Файл рар")
        bot.send_message(message.chat.id, "MOOVI TV Лаунчер Файл рар")
    elif message.text == "MICROIMPULS":
        bot.send_message(message.chat.id, "MICROIMPULS Автозупуск Файл рар")
        bot.send_message(message.chat.id, "MICROIMPULS Лаунчер Файл рар")
    elif message.text == "PEERS TV":
        bot.send_message(message.chat.id, "PEERS TV Автозупуск Файл рар")
        bot.send_message(message.chat.id, "PEERS TV Лаунчер Файл рар")

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.P_REDBOX5PRO_APP.value)
def cmd_choose_appforl(message):
    if message.text == "Назад в Порталы и платформы":
        portalsandplatforms(message)
        dbworker.set_state(message.chat.id, config.States.S_DISABLED.value)
    elif message.text == "IPTVPORTAL":
        bot.send_message(message.chat.id, "2IPTVPORTAL Автозупуск Файл рар")
        bot.send_message(message.chat.id, "2IPTVPORTAL Лаунчер Файл рар")
    elif message.text == "24 ТВ":
        bot.send_message(message.chat.id, "224 ТВ Автозупуск Файл рар")
        bot.send_message(message.chat.id, "224 ТВ Лаунчер Файл рар")
    elif message.text == "СМОТРЕШКА":
        bot.send_message(message.chat.id, "2СМОТРЕШКА Автозупуск Файл рар")
        bot.send_message(message.chat.id, "2СМОТРЕШКА Лаунчер Файл рар")
    elif message.text == "MOOVI TV":
        bot.send_message(message.chat.id, "2MOOVI TV Автозупуск Файл рар")
        bot.send_message(message.chat.id, "2MOOVI TV Лаунчер Файл рар")
    elif message.text == "MICROIMPULS":
        bot.send_message(message.chat.id, "2MICROIMPULS Автозупуск Файл рар")
        bot.send_message(message.chat.id, "2MICROIMPULS Лаунчер Файл рар")
    elif message.text == "PEERS TV":
        bot.send_message(message.chat.id, "2PEERS TV Автозупуск Файл рар")
        bot.send_message(message.chat.id, "2PEERS TV Лаунчер Файл рар")

@bot.message_handler(regexp="^Кастомизация$")
def customizemenu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Варианты кастомизации")
    item2 = types.KeyboardButton("Собрать свой кастом")
    item3 = types.KeyboardButton("Назад в Порталы и платформы")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выберите приложение:", reply_markup=markup)
    #dbworker.set_state(message.chat.id, config.States.P_REDBOX5PRO_APP.value)
    pass

@bot.message_handler(regexp="^Стоковая прошивка$")
def stockfirmware(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("RedBox Mini 3L...")
    item2 = types.KeyboardButton("RedBox Mini 5PRO...")
    item3 = types.KeyboardButton("Назад в Порталы и платформы")
    #тут надо будет заменить на инлайн
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выберите устройство:", reply_markup=markup)

@bot.message_handler(regexp="^Прошивки для операторов$")
def operfirmware(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("RedBox Mini 3L:")
    item2 = types.KeyboardButton("RedBox Mini 5PRO:")
    item3 = types.KeyboardButton("Назад в Порталы и платформы")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выберите устройство:", reply_markup=markup)

#Блок Техническая документация
@bot.message_handler(regexp="^Техническая документация$")
def techdoc(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("IPTV приставки")
    item2 = types.KeyboardButton("Обновление и перепрошивка")
    item3 = types.KeyboardButton("Презентации и промо")
    item4 = types.KeyboardButton("Удалённое управление")
    item5 = types.KeyboardButton("Назад в гл.меню")
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, "Выберите интересующую категорию", reply_markup=markup)
    pass

@bot.message_handler(regexp="^IPTV приставки$")
def iptvconsole(message):
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

@bot.message_handler(regexp="^Удалённое управление$")
def myfunction(message):
    bot.send_message(message.chat.id, "Файлы.rar")
    pass
#Конец блока Техническая документация

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

@bot.message_handler(regexp="^Техническая поддержка")
def msgtosupport(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Вернуться в главное меню.")
    markup.add(item1)
    bot.send_message(message.chat.id, "Напишите одним сообщением текст обращения и Ваши контактные данные:", reply_markup=markup)
    dbworker.set_state(message.chat.id, config.States.T_SUPPORT_MSG.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.T_SUPPORT_MSG.value)
def mssgtosupport(message):
    user_msg_to_sup = ""
    global sender_email
    global receiver_email
    global password
    if message.from_user.username is None:
        user_name = "Имя пользователя неопределено"
    else:
        user_name = message.from_user.username
    user_msg_to_sup = user_msg_to_sup + user_name + "\n" + message.text
    messagetomail = MIMEMultipart("alternative")
    messagetomail["Subject"] = "Поступило обращение от: " + user_name
    messagetomail["From"] = sender_email
    messagetomail["To"] = receiver_email
    text = user_msg_to_sup
    part1 = MIMEText(text, "plain")
    messagetomail.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, messagetomail.as_string())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Вернуться в главное меню.")
    markup.add(item1)
    bot.send_message(message.chat.id, "Ваше обращение успешно принято, нажмите Вернуться в главное меню.:", reply_markup=markup)

#Начало блока кастомизации
@bot.message_handler(commands=['customize'])
@bot.message_handler(regexp="^Собрать свой кастом$")
def cmd_start(message):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    user_final_data = ""
    user_id = message.from_user.id
    sql = "select User_id from user_custom where user_id=?"
    a = cursor.execute(sql, [(user_id)]).fetchall()
    if a:
        sql = "UPDATE user_custom SET Model='Null', Main_application='Null', MA_launch_type='Null', Online_cinema='Null', OC_launch_type='Null', Additional_app='Null', Required_changes='Null', Box_start_graphic='Null', Wallpaper='Null', Username='Null', Contact_data='Null', Box_start_gr_type='Null' WHERE User_id=?"
        cursor.execute(sql, [(user_id)])
    else:
        sql = "INSERT INTO user_custom (User_id) VALUES (?)"
        cursor.execute(sql, [(user_id)])
    conn.commit()
    conn.close()
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Redbox Mini 3L.")
    item2 = types.KeyboardButton("Redbox Mini 5PRO.")
    item3 = types.KeyboardButton("Отменить кастомизацию.")
    keyboard.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выберите модель:", reply_markup=keyboard)
    dbworker.set_state(message.chat.id, config.States.S_SET_MAIN_APP.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SET_MAIN_APP.value)
def cmd_set_mainapp(message):
    datasql = (message.text, message.from_user.id)
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
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = "UPDATE user_custom SET Model='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        dbworker.set_state(message.chat.id, config.States.S_SET_LAUNCHE.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SET_LAUNCHE.value)
def cmd_set_launcher(message):
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
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            sql = "UPDATE user_custom SET Main_application='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            dbworker.set_state(message.chat.id, config.States.S_SET_ONL_CINEMA.value)
        else:
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Лаучер.")
            item2 = types.KeyboardButton("Автозапуск.")
            item3 = types.KeyboardButton("Рабочий стол.")
            item4 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "Выберите тип запуска приложения:", reply_markup=keyboard)
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            sql = "UPDATE user_custom SET Main_application='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            dbworker.set_state(message.chat.id, config.States.S_SET_ONL_CINEMA.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SET_ONL_CINEMA.value)
def cmd_set_online_cinema(message):
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
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = "UPDATE user_custom SET MA_launch_type='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        dbworker.set_state(message.chat.id, config.States.S_SET_CINEMA_LAUNCH.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SET_CINEMA_LAUNCH.value)
def cmd_set_cinema_launch(message):
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
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            sql = "UPDATE user_custom SET Online_cinema='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            dbworker.set_state(message.chat.id, config.States.S_SET_ADD_APP.value)
        else:
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Далее")
            item2 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1, item2)
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            sql = "UPDATE user_custom SET Online_cinema='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            bot.send_message(message.chat.id, "Онлайн-кинотеатр не будет включен в прошивку, нажмите далее", reply_markup=keyboard)
            dbworker.set_state(message.chat.id, config.States.S_SET_ADD_APP.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SET_ADD_APP.value)
def cmd_set_addon_app(message):
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
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            sql = "UPDATE user_custom SET OC_launch_type='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
            cursor.execute(sql)
            conn.commit()
            conn.close()
        dbworker.set_state(message.chat.id, config.States.S_CUSTOMIZE_SETT.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_CUSTOMIZE_SETT.value)
def cmd_set_addon_app(message):
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("НЕ НУЖНЫ.")
        item2 = types.KeyboardButton("НУЖНЫ.")
        item3 = types.KeyboardButton("Отменить кастомизацию.")
        keyboard.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Нужны ли изменения настроек?", reply_markup=keyboard)
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = "UPDATE user_custom SET Additional_app='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        dbworker.set_state(message.chat.id, config.States.S_WRITE_ABOUT_CHANGES.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_WRITE_ABOUT_CHANGES.value)
def cmd_write_about_changes(message):
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        if message.text == "НУЖНЫ.":
            keyboard = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, "Напишите какие изменения необходимы.", reply_markup=keyboard)
            dbworker.set_state(message.chat.id, config.States.S_START_GRAPH.value)
        else:
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Далее")
            item2 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1, item2)
            bot.send_message(message.chat.id, "Нажмите Далее, чтобы продолжить или Отменить", reply_markup=keyboard)
            dbworker.set_state(message.chat.id, config.States.S_START_GRAPH.value) 	

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_START_GRAPH.value)
def cmd_choose_start_graphic(message):
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
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            sql = "UPDATE user_custom SET Required_changes='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
            cursor.execute(sql)
            conn.commit()
            conn.close()
        dbworker.set_state(message.chat.id, config.States.S_CHOOSE_DL_METH_GP.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_CHOOSE_DL_METH_GP.value)
def cmd_choose_start_graphic(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Отменить кастомизацию.")
    keyboard.add(item1)
    bot.send_message(message.chat.id, "Пришлите документом файл в выбранном формате или нажмите Отмену", reply_markup=keyboard)
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    sql = "UPDATE user_custom SET Box_start_gr_type='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    dbworker.set_state(message.chat.id, config.States.S_WALLPAPER.value)

@bot.message_handler(content_types=['document'])
def cmd_choose_wallpaper(message):
    if dbworker.get_current_state(message.chat.id) == config.States.S_WALLPAPER.value:
        file_info = bot.get_file(message.document.file_id)
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("Своя.")
        item2 = types.KeyboardButton("Стандартная.")
        item3 = types.KeyboardButton("Отменить кастомизацию.")
        keyboard.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Выберете заставку рабочего стола:", reply_markup=keyboard)
        url = 'https://api.telegram.org/file/bot{0}/{1}'.format(config.TOKEN, file_info.file_path)
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = "UPDATE user_custom SET Box_start_graphic='{0}' where user_id={1}".format(url, message.from_user.id)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        dbworker.set_state(message.chat.id, config.States.S_CHOOSE_DL_M_WALLPAPER.value)

    if dbworker.get_current_state(message.chat.id) == config.States.S_DOWNLOAD_WALLPAPER.value:
        file_info = bot.get_file(message.document.file_id)
        url = 'https://api.telegram.org/file/bot{0}/{1}'.format(config.TOKEN, file_info.file_path)
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("Отменить кастомизацию.")
        keyboard.add(item1)
        bot.send_message(message.chat.id, "Оставьте контактные данные и нажмите Далее", reply_markup=keyboard)
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = "UPDATE user_custom SET Wallpaper='{0}' where user_id={1}".format(url, message.from_user.id)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        dbworker.set_state(message.chat.id, config.States.S_FINAL.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_CHOOSE_DL_M_WALLPAPER.value)
def cmd_choose_start_graphic(message):
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        if message.text == "Своя.":
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1)
            bot.send_message(message.chat.id, "Загрузите заставку 1920x1080 .png", reply_markup=keyboard)
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            sql = "UPDATE user_custom SET Wallpaper='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            dbworker.set_state(message.chat.id, config.States.S_DOWNLOAD_WALLPAPER.value)
        if message.text != "Своя.":
            keyboard = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton("Отменить кастомизацию.")
            keyboard.add(item1)
            bot.send_message(message.chat.id, "Оставьте контактные данные или нажмите Отменить", reply_markup=keyboard)
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            sql = "UPDATE user_custom SET Wallpaper='{0}' where user_id={1}".format(message.text.rstrip("."), message.from_user.id)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            dbworker.set_state(message.chat.id, config.States.S_FINAL.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_FINAL.value)
def cmd_choose_start_graphic(message):
    global sender_email
    global receiver_email
    global password
    if message.text == "Отменить кастомизацию.":
        cmd_reset(message)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        item1 = types.KeyboardButton("Вернуться в главное меню.")
        keyboard.add(item1)

        if message.from_user.username is None:
        	user_name = "Имя пользователя неопределено"
        else:
            user_name = message.from_user.username
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = "UPDATE user_custom SET Username='{0}', Contact_data='{1}' where user_id={2}".format(user_name, message.text.rstrip("."), message.from_user.id)
        cursor.execute(sql)
        conn.commit()
        sql2 = "SELECT * FROM user_custom WHERE user_id={0}".format(message.from_user.id)
        a = cursor.execute(sql2).fetchone()
        conn.close()
        bot.send_message(message.chat.id, "Вы завершили кастомизацию, в ближайшее время с Вами свяжутся",  reply_markup=keyboard)
        dbworker.set_state(message.chat.id, config.States.S_DISABLED.value)
        message = MIMEMultipart("alternative")
        message["Subject"] = "Поступила кастомизация от: " + user_name
        message["From"] = sender_email
        message["To"] = receiver_email
        text = "Модель: " + a[1] + "\n" + "Главное приложение: " + a[2] + "\n" "Тип запуска главного приложения: " + a[3] + "\n" + "Онлайн-кинотеатр: " + a[4] + "\n" + "Тип запуска онлайн-кинотеатра: " + a[5] + "\n" + "Дополнительные приложения: " + a[6] + "\n" + "Необходимые изменения: " + a[7] + "\n" "Графика при запуске: " + a[8] + "\n" + "Основная заставка: " + a[9] + "\n" "Контактные данные: " + a[11] + "\n" + "Имя пользователя в Telegram: " + a[10]
        part1 = MIMEText(text, "plain")
        message.attach(part1)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

@bot.message_handler(commands=['reset'])
@bot.message_handler(regexp="^Отменить кастомизацию.$")
def cmd_reset(message):
    bot.send_message(message.chat.id, "Cancel")
    dbworker.set_state(message.chat.id, config.States.S_DISABLED.value)
    welcome(message)

@bot.message_handler(commands=['getuserdata'])
def cmd_get_usr_data(message):
	if message.from_user.id:
	    bot.send_message(message.chat.id, message.from_user.id)
	else:
		bot.send_message(message.chat.id, "No DATA about user")
#Конец блока кастомизации
# RUN
bot.polling(none_stop=True)