#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

# -*- coding: utf-8 -*-

import configparser

from services.settings_file_service import get_settings_file_path


def get_username():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("USER", "Username")


def get_password():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("USER", "Password")


def set_login_parameters():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    username = input("Enter the user name: ")
    passwd = input("Enter your password: ")
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    config.set("USER", "Username", username)
    config.set("USER", "Password", passwd)
    with open(get_settings_file_path(), "w") as config_file:
        config.write(config_file)
        config_file.close()
