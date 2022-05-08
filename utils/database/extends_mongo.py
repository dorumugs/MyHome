from pymongo import MongoClient
from utils.database.database_config import DatabaseConfig
from utils.log import logger


class ExtendsMongo(object):
    def __init__(self, _logger):
        DatabaseConfig.__init__(self)
        if _logger is None:
            self.logger = logger.setup_logger("[sqlalchemy]")
        else:
            self.logger = _logger
        self.database_config = DatabaseConfig()
        self.client = MongoClient(
            host=self.database_config.MONGODB_URL,
            port=27017,
            username=self.database_config.MONGODB_ID,
            password=self.database_config.MONGODB_PW
        )

    def create_session(self, session_type, url, db_name, username=None, password=None):
        self.logger.info(f"Set Session Params - session_type : {session_type}")
        self.logger.info(f"Set Session Params - url : {url}")
        self.logger.info(f"Set Session Params - db_name : {db_name}")
        if session_type == 'MYSQL':
            client = MongoClient(
                host=url,
                port=27017,
                username=username,
                password=password
            )
            return client[db_name]
        else:
            self.logger.critical("Select Session Type MYSQL or MONGODB")
            raise None