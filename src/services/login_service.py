#  -*- coding: utf-8 -*-
#
#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.
#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from services.user_settings_service import get_password
from services.user_settings_service import get_username
from services.webdriver_settings_service import get_driver_path


def login():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options, executable_path=get_driver_path())
    username = get_username()
    print("Attempt to log in as " + username + " ...")
    browser.get("https://www.linux.org.ru/login.jsp")
    browser.find_element_by_name('nick').click().send_keys(username)
    passwd = get_password()
    browser.find_element_by_name('passwd').send_keys(passwd)
    browser.find_element_by_class_name('btn btn-primary').click()
