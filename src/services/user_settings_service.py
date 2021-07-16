#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.
import configparser

from services.settngs_file_service import get_settings_file_path


def get_username():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("USER", "Username", "NONE")


def get_password():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("USER", "Password", "NONE")