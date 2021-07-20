#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.
import sys
from commands.user_checker import check_user_status
from services.settngs_file_service import set_driver_path


def check_command(command):
    if command == "exit":
        sys.exit()
    elif command == "get-tracker" or command == "g-t":
        check_user_status()
    elif command == "set-driver-path" or command == "s-d-p":
        set_driver_path()
    else:
        print("Command not found")
