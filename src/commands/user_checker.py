#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from services.webdriver_settings_service import get_driver_path


def check_user_status():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    if get_driver_path() != "NONE":
        browser = webdriver.Chrome(options=chrome_options, executable_path=get_driver_path())
        browser.get("https://linux.org.ru")
        user_div = browser.find_element_by_id('loginGreating')
        if user_div.text == "Регистрация - Вход":
            print("Warning: you need to log in!")
    elif get_driver_path() == "NONE":
        print("You need to configure the path to the browser driver")
