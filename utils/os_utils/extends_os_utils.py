from utils.log import logger
from config.project_env.directory_config import *
import os


class ExtendsOsUtils(object):
    def __init__(self, _logger=None):
        if _logger is None:
            self.logger = logger.setup_logger("[OS]")
        else:
            self.logger = _logger

    def create_init_data_directories(self):
        paths = [
            INIT_DIRECTORY,
            REGION_CODE_DIRECTORY,
            REGION_CODE_SUB_DIRECTORY,
            CSV_DIRECTORY,
            CSV_ADD_DIRECTORY,
            TX_DIRECTORY,
            ACTUAL_TX_DIRECTORY,
            ACTUAL_TX_DIRECTORY_CSV,
            CHARTERED_RENT_DIRECTORY,
            CHARTERED_RENT_DIRECTORY_CSV,
            AC_CH_FINAL_DIRECTORY
        ]

        for path in paths:
            # Check whether the specified path exists or not
            is_exist = os.path.exists(path)

            if not is_exist:
                # Create a new directory because it does not exist
                os.makedirs(path)
                self.logger.info(f"{path} is created!")

