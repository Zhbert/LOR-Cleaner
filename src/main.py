#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.

from commands.commands_checker import check_command

if __name__ == '__main__':
    while 0 < 1:
        command = input("Please enter the command: ")
        check_command(command)
