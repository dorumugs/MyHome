from config.project_env.molit_profile import *
from utils.log import logger
from sys import version
from platform import platform
from src.myhome import MyHome
import pandas as pd
pd.set_option('display.max_columns', None)

# Logging Set
logger = logger.setup_logger("[MyHome Python]")
logger.info("Python Version -- " + str(version).replace('\n', ' '))
logger.info("OS Version -- " + str(platform()))

if __name__ == "__main__":
    my_home = MyHome(logger)
    my_home.init_settings() # 프로젝트 세팅

    my_home.get_curl_data() # 데이터 가져오기
    my_home.real_estate(selected_month='2019-10', key=BLACK_SERVICE_KEY) # 실거래, 전세가 가져오기
    my_home.real_estate_pre() # 전체 데이터 전처리 하기, 오래걸림
    my_home.additional_insight(target='1') # 추가 인사이트 데이터를 생성
    my_home.export_elasticsearch() # 엘라스틱서치에 삽입
    my_home.export_mongodb()
