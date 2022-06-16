from src.core.core_export import CoreExport
from utils.database.database_config import DatabaseConfig
from utils.log import logger


class ExtendsExport(CoreExport):
    def __init__(self, _logger=None, extends_sqlalchemy=None):
        if _logger is None:
            self.logger = logger.setup_logger("[Export]")
        else:
            self.logger = _logger
        super().__init__(extends_sqlalchemy)
        self.database_config = DatabaseConfig()

    def call_export_data_to_elasticsearch(self, index_nm, mapping, csv, target):
        self.logger.info(f"Import {target} Data")
        self.export_elasticsearch_func(index_nm, mapping, csv, target)

    def call_remove_export_data_to_mongo(self, input_type, csv_file):
        db = self.mg.client[self.database_config.MONGODB_DB]
        self.remove_collection_mongo_func(db, input_type)
        self.export_collection_mongo_func(db, input_type, csv_file)

    def call_export_data_to_mongo(self, input_type, csv_file):
        db = self.mg.client[self.database_config.MONGODB_DB]
        self.export_collection_mongo_func(db, input_type, csv_file)
