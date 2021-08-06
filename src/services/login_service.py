#  -*- coding: utf-8 -*-
#
#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.
#
from main import browser
from services.user_settings_service import get_password
from services.user_settings_service import get_username


def login():
    username = get_username()
    print("Attempt to log in as " + username + " ...")
    browser.get("https://www.linux.org.ru/login.jsp")
    form = browser.find_element_by_xpath("//form[@action='https://www.linux.org.ru/login_process']")
    form.find_element_by_name('nick').send_keys(get_username())
    pass_input = form.find_element_by_name('passwd')
    pass_input.send_keys(get_password())
    pass_input.submit()

