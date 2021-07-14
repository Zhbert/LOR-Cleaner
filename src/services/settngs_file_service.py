#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.
import os
import configparser


def check_settings_file():
    settings_path = get_home_path() + "/.lor_cleaner"
    if os.path.exists(settings_path):
        print("Найден каталог настроек. Читаю параметры логина...")
    else:
        print("Каталог настроек не найден: " + settings_path)
        set_user_data()


def get_home_path():
    home_path = (os.getenv('HOME'))
    if home_path == "None":
        home_path = os.getenv('USERPROFILE')
    return home_path


def set_user_data():
    settings_path = get_home_path() + "/.lor_cleaner"
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info",
               "You are using %(font)s at %(font_size)s pt")
    if os.path.exists(settings_path + "/lorcleaner.conf"):
        with open(settings_path + "/lorcleaner.conf", "w") as config_file:
            config.write(config_file)
    else:
        os.mkdir(settings_path)
        with open(settings_path + "/lorcleaner.conf", "x") as config_file:
            config.write(config_file)
