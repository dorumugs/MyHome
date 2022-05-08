from utils.log import logger
from elasticsearch import Elasticsearch
import json
from datetime import date
from elasticsearch import helpers
from utils.database.elasticsearch_mappings import *
from utils.database.elasticsearch_fields import *
from utils.database.database_config import DatabaseConfig


class QelasticSearch(object):
    def __init__(self, _logger=None):
        if _logger is None:
            self.logger = logger.setup_logger("ELASTIC")
        else:
            self.logger = _logger
        self.database_config = DatabaseConfig()
        conf = json.loads(str(self.database_config.ELASTICSEARCH_CONN).replace("'", '"'))
        hosts = conf["hosts"]
        self.es = Elasticsearch(hosts=hosts)

    def get_info(self):
        return self.es.info(pretty=True)

    def show_index(self):
        return self.es.cat.indices(pretty=True)

    def create_index(self, index, mapping=None):
        if not self.es.indices.exists(index=index):
            if mapping is None:
                return self.es.indices.create(index=index, pretty=True)
            else:
                return self.es.indices.create(index=index, body=mapping, pretty=True)

    def overwrite_index(self, index, mapping=None):
        if self.es.indices.exists(index=index):
            self.delete_index(index=index)
        else:
            if mapping is None:
                return self.es.indices.create(index=index, pretty=True)
            else:
                return self.es.indices.create(index=index, body=mapping, pretty=True)

    def delete_index(self, index):
        if self.es.indices.exists(index=index):
            return self.es.indices.delete(index=index, pretty=True)

    def count_doc(self, index):
        return self.es.count(index=index, pretty=True)

    def show_schema(self, index):
        return self.es.indices.get_mapping(index=index, pretty=True)

    def doc_insert(self, index, body):
        return self.es.index(index=index, body=body, pretty=True)

    def parallel_bulk_insert(self, index, json_func):
        for success, info in helpers.parallel_bulk(self.es, json_func):
            if not success:
                print("Document failed : ", info)
        self.es.indices.refresh(index=index)

    def search_doc(self, index, batch_size=10000, data=None):
        if data is None:
            data = {"match_all": {}}
        else:
            data = {"match": data}
        body = {"size": batch_size,
                "query": data}
        return self.es.search(index=index, body=body)

    def field_date(self, target):
        today = date.today()
        date_str = today.strftime("%Y.%m.%d")
        index_nm, mapping = '', ''
        if target == 'ACTUAL_DETAIL':
            index_nm = REAL_ESTATE_MAPPING_AC_DETAIL['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = REAL_ESTATE_MAPPING_AC_DETAIL['mapping']
        elif target == 'CHARTERED_RENT_DETAIL':
            index_nm = REAL_ESTATE_MAPPING_CH_DETAIL['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = REAL_ESTATE_MAPPING_CH_DETAIL['mapping']
        elif target == 'ACTUAL_MASTER':
            index_nm = REAL_ESTATE_MAPPING_AC_MASTER['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = REAL_ESTATE_MAPPING_AC_MASTER['mapping']
        elif target == 'CHARTERED_RENT_MASTER':
            index_nm = REAL_ESTATE_MAPPING_CH_MASTER['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = REAL_ESTATE_MAPPING_CH_MASTER['mapping']
        elif target == 'AC_CH':
            index_nm = AC_CH_MAPPING['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = AC_CH_MAPPING['mapping']
        elif target == 'GDP':
            index_nm = GDP_MAPPING['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = GDP_MAPPING['mapping']
        elif target == 'POPULATION':
            index_nm = POPULATION_MAPPING['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = POPULATION_MAPPING['mapping']
        elif target == 'PRICE':
            index_nm = PRICE_MAPPING['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = PRICE_MAPPING['mapping']
        elif target == 'UNSOLD':
            index_nm = UNSOLD_MAPPING['info']['index_nm'] + '=' + date_str
            self.logger.info(f"Index Name - {index_nm}")
            mapping = UNSOLD_MAPPING['mapping']
        return index_nm, mapping

    def iter_source(self, target, index_nm, dataframe):
        self.logger.info(f"Target Name - {target}")
        if target == 'ACTUAL':
            for idx in dataframe.index:
                yield real_estate_ac_fields(index_nm, dataframe, idx)
        elif target == 'CHARTERED_RENT':
            for idx in dataframe.index:
                yield real_estate_ch_fields(index_nm, dataframe, idx)
        elif target == 'ACTUAL_PRE':
            for idx in dataframe.index:
                yield real_estate_ac_pre_fields(index_nm, dataframe, idx)
        elif target == 'CHARTERED_RENT_PRE':
            for idx in dataframe.index:
                yield real_estate_ch_pre_fields(index_nm, dataframe, idx)
        elif target == 'AC_CH':
            for idx in dataframe.index:
                yield ac_ch_fields(index_nm, dataframe, idx)
        elif target == 'GDP':
            for idx in dataframe.index:
                yield gdp_fields(index_nm, dataframe, idx)
        elif target == 'POPULATION':
            for idx in dataframe.index:
                yield population_fields(index_nm, dataframe, idx)
        elif target == 'PRICE':
            for idx in dataframe.index:
                yield price_fields(index_nm, dataframe, idx)
        elif target == 'UNSOLD':
            for idx in dataframe.index:
                yield unsold_fields(index_nm, dataframe, idx)
