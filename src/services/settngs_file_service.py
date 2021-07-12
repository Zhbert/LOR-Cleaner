#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.
import os


def check_settings_file():
    home_path = (os.getenv('HOME'))
    if home_path == "None":
        home_path = os.getenv('USERPROFILE')
    print(home_path)
