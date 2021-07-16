#  Copyright (c) 2021.
#  Created by Zhbert.
#  Licensed by GPLv3.
import configparser

from services.settngs_file_service import get_settings_file_path


def get_driver_path():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("DRIVER", "Path", "NONE")
