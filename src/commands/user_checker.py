# -*- coding: utf-8 -*-

#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

from services.login_service import login
from services.webdriver_settings_service import get_driver_path, get_browser


def check_user_status():
    if get_driver_path() != "NONE":
        browser = get_browser()
        browser.get("https://linux.org.ru")
        user_div = browser.find_element_by_id('loginGreating')
        if user_div.text == "Регистрация - Вход":
            print("Warning: you need to log in!")
            login()
    elif get_driver_path() == "NONE":
        print("You need to configure the path to the browser driver")
