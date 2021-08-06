# -*- coding: utf-8 -*-

#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

from main import browser

from services.login_service import login
from services.webdriver_settings_service import get_driver_path


def check_user_status():
    if get_driver_path() != "NONE":
        browser.get("https://linux.org.ru")
        user_div = browser.find_element_by_id('loginGreating')
        if user_div.text == "Регистрация - Вход":
            print("Warning: you need to log in!")
            login()
            browser.get('https://linux.org.ru')
            user_div = browser.find_element_by_id('loginGreating')
            if user_div.text != "Регистрация - Вход":
                print("You are logged in as " + user_div.text)
            else:
                check_user_status()
    elif get_driver_path() == "NONE":
        print("You need to configure the path to the browser driver")
