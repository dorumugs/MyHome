from utils.database.extends_elasticsearch import QelasticSearch
from utils.database.extends_mongo import ExtendsMongo
import pandas as pd
import numpy as np


class CoreExport(object):
    def __init__(self, extends_sqlalchemy=None):
        self.extends_sqlalchemy = extends_sqlalchemy
        self.qes = QelasticSearch()
        self.mg = ExtendsMongo()

    def export_elasticsearch_func(self, index_nm, mapping, csv_file, target):
        self.qes.overwrite_index(index_nm, mapping)
        df = pd.read_csv(csv_file, sep='|', encoding='utf-8', low_memory=False)
        df = df.dropna()
        df = df.replace([np.inf, -np.inf], 0)
        self.qes.parallel_bulk_insert(index_nm, self.qes.iter_source(target=target, index_nm=index_nm, dataframe=df))

    @staticmethod
    def remove_collection_mongo_func(db, collection):
        db[collection].drop()

    @staticmethod
    def export_collection_mongo_func(db, collection, csv_file):
        col = db[collection]
        df = pd.read_csv(csv_file, sep='|', encoding='utf-8', low_memory=False)
        df_dict = df.to_dict('records')

        df_dict_len = len(df_dict)
        multiple = 1000
        total_count = int(df_dict_len / multiple)
        remains = df_dict_len % multiple
        for i in range(total_count):
            if i+1 != total_count:
                col.insert_many(df_dict[i * multiple: (i * multiple) + multiple])
            else:
                col.insert_many(df_dict[i * multiple: (i * multiple) + multiple + remains])
