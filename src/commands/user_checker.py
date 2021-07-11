#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def check_user_status():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options, executable_path="/Users/zhbert/chromedriver")
    browser.get("https://linux.org.ru")
    print(browser.page_source)
