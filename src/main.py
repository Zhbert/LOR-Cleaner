#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.
import sys

from commands.commands_checker import check_command

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for param in sys.argv:
            check_command(param)
    else:
        while 0 < 1:
            command = input("Please enter the command: ")
            check_command(command)
