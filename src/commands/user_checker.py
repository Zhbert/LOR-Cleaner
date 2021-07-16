#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def check_user_status():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options, executable_path="/home/zhbert/chromedriver")
    browser.get("https://linux.org.ru")
    user_div = browser.find_element_by_id('loginGreating')
    if user_div.text == "Регистрация - Вход":
        print("Warning: you need to log in!")

