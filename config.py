# -*- coding: utf-8 -*-

from enum import Enum

TOKEN = '1126792603:AAF0XMgLYgbQ8Zznp275qQPJiTODCEezHzc'
db_file = "database.vdb"
database_name = 'database.db'
E_PASSWD = 'Rtybvc-764'

class States(Enum):

    S_START = "0"
    S_SET_MAIN_APP = "1"
    S_SET_LAUNCHE = "2"
    S_SET_ONL_CINEMA = "3"
    S_SET_CINEMA_LAUNCH = "4"
    S_SET_ADD_APP = "5"
    S_CUSTOMIZE_SETT = "6"
    S_WRITE_ABOUT_CHANGES = "7"
    S_START_GRAPH = "8"
    S_CHOOSE_DL_METH_GP = "9"
    S_WALLPAPER = "10"
    S_CHOOSE_DL_M_WALLPAPER = "11"
    S_DOWNLOAD_WALLPAPER = "12"
    S_FINAL = "13"
    S_DISABLED = "X"
    P_REDBOX3L_APP = "20"
    P_REDBOX5PRO_APP = "21"
    T_SUPPORT_MSG = "30"