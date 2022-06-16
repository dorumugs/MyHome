class DatabaseConfig(object):
    def __init__(self,):
        self.MYSQL_URL = 'localhost'
        self.MYSQL_ID = 'root'
        self.MYSQL_PW = '1234'
        self.MONGODB_URL = '1.214.48.106'
        self.MONGODB_PORT = 27017
        self.MONGODB_ID = 'root'
        self.MONGODB_PW = '2B$rich'
        self.MONGODB_DB = 'blackdb'
        self.ELASTICSEARCH_URL = "1.214.48.106:9200"
        self.ELASTICSEARCH_ID = 'elastic'
        self.ELASTICSEARCH_PW = '2B$rich'
        self.ELASTICSEARCH_CONN = {
            "hosts": [
                f"http://{self.ELASTICSEARCH_ID}:{self.ELASTICSEARCH_PW}@{self.ELASTICSEARCH_URL}/"
            ]
        }
