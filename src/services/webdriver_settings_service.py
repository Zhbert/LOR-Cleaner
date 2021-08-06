# -*- coding: utf-8 -*-

#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

import configparser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from services.settings_file_service import get_settings_file_path


def get_driver_path():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("DRIVER", "Path")


def check_driver_path():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    if config.get("DRIVER", "Path") == "NONE":
        set_driver_path()


def set_driver_path():
    path = input("Enter the path to the browser driver: ")
    ready = input("Check that the input is correct (y/n) - " + path + " : ")
    if ready == "y" or "Y":
        config = configparser.ConfigParser()
        config.read(get_settings_file_path())
        config.set("DRIVER", "Path", path)
        with open(get_settings_file_path(), "w") as config_file:
            config.write(config_file)
            config_file.close()
    elif ready == "n" or "N":
        set_driver_path()


def get_browser():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized");
    if get_driver_path() != "NONE":
        browser = webdriver.Chrome(options=chrome_options, executable_path=get_driver_path())
        return browser
    else:
        return None
