#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.
import sys
from commands.user_checker import check_user_status


def check_command(command):
    if command == "exit":
        sys.exit()
    if command == "get-tracker":
        check_user_status()
