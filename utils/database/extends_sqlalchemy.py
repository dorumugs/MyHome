import pandas as pd
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import Session
from sqlalchemy.engine import create_engine
from pymongo import MongoClient
from utils.database.database_config import DatabaseConfig
from utils.log import logger


class ExtendsSqlalchemy(DatabaseConfig):
    def __init__(self, _logger):
        DatabaseConfig.__init__(self)
        if _logger is None:
            self.logger = logger.setup_logger("[sqlalchemy]")
        else:
            self.logger = _logger

    def create_session(self, session_type, url, db_name, verbose=False, username=None, password=None):
        self.logger.info(f"Set Session Params - session_type : {session_type}")
        self.logger.info(f"Set Session Params - url : {url}")
        self.logger.info(f"Set Session Params - db_name : {db_name}")
        if session_type == 'MYSQL':
            engine = create_engine(
                'mysql://'
                + username + ':'
                + password + '@'
                + url + '/'
                + db_name,
                echo=verbose,
                poolclass=NullPool
            )
            return Session(bind=engine)
        else:
            self.logger.critical("Select Session Type MYSQL or MONGODB")
            raise None