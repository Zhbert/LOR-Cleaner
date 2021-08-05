#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.
import sys
from commands.user_checker import check_user_status
from services.webdriver_settings_service import set_driver_path


def check_command(command):
    if command == "exit":
        sys.exit()
    elif command == "scan-tracker" or command == "st":
        check_user_status()
    elif command == "set-driver-path" or command == "sdp":
        set_driver_path()
    else:
        print("Command not found")
