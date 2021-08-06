# -*- coding: utf-8 -*-

#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

from commands.commands_checker import *
from services.settings_file_service import *
from services.webdriver_settings_service import *

browser = get_browser()

if __name__ == '__main__':
    check_settings_file()
    check_driver_path()
    if len(sys.argv) > 1:
        for param in sys.argv:
            check_command(param)
    else:
        while 0 < 1:
            command = input("Please enter the command: ")
            check_command(command)
