from pymongo import MongoClient
from utils.database.database_config import DatabaseConfig
from utils.log import logger


class ExtendsMongo(DatabaseConfig):
    def __init__(self, _logger=None):
        DatabaseConfig.__init__(self)
        if _logger is None:
            self.logger = logger.setup_logger("[mongodb]")
        else:
            self.logger = _logger
        self.database_config = DatabaseConfig()
        self.client = MongoClient(
            host=self.database_config.MONGODB_URL,
            port=self.database_config.MONGODB_PORT,
            username=self.database_config.MONGODB_ID,
            password=self.database_config.MONGODB_PW
        )

