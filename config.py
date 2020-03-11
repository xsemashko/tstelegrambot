# -*- coding: utf-8 -*-

from enum import Enum

TOKEN = '1126792603:AAF0XMgLYgbQ8Zznp275qQPJiTODCEezHzc'
db_file = "database.vdb"
database_name = 'database.db'
shelve_name = 'shelve.db'

class States(Enum):

    S_START = "0"  # Начало нового диалога
    S_SET_MAIN_APP = "1"
    S_SET_LAUNCHE = "2"
    S_SET_ONL_CINEMA = "3"
    S_SET_ADD_APP = "4"
    S_CUSTOMIZE_SETT = "5"
    S_START_GRAPH = "6"
    S_CHOOSE_DL_METH_GP = "7"
    S_WALLPAPER = "8"
    S_CHOOSE_DL_M_WALLPAPER = "9"