from src.extends.extends_extract import ExtendsExtract
from src.extends.extends_transform import ExtendsTransform
from src.extends.extends_export import ExtendsExport
from utils.database.extends_elasticsearch import QelasticSearch
from utils.database.extends_mongo import ExtendsMongo
from utils.os_utils.extends_os_utils import ExtendsOsUtils
from config.molit_go_kr.actual_tx_and_chartered_rent import *
from config.project_env.molit_profile import *
from config.project_env.directory_config import *


class MyHome(object):
    def __init__(self, _logger):
        self.logger = _logger
        self.osutils = ExtendsOsUtils(self.logger)
        self.transform = ExtendsTransform(self.logger)
        self.extract = ExtendsExtract(self.logger)
        self.export = ExtendsExport(self.logger)
        self.qes = QelasticSearch(self.logger)

    def init_settings(self):
        """
        프로젝트에서 필요한 드렉토리를 생성한다.
        ./data/ 자식 디렉토리로 이루어져 있다.
        :return:
        """
        self.osutils.create_init_data_directories()

    def get_curl_data(self):
        """
        curl로 추출할 수 있는 데이터를 모아놓았다.
        모아진 데이터는 Transform하여 _pre가 붙은 데이터를 생성한다.
        REG_REGION이 기본이 되며 법정동 코드를 담고 있다.
        항상 최신을 유지할 수 있게 적용되어 있다.
        :return:
        """
        job_list = {
            # "REG_REGION_CODE": "1 JOB - for actual tx & chartered rent",
            # "REGION_CODE_FULL": "2 JOB - Full registered Number ",
            # "POPULATION": "3-1 JOB",
            # "POPULATION_POST": "3-2 JOB",
            # "POPULATION_FULL": "3-3 JOB",
            # "POPULATION_FULL_POST": "3-4 JOB",
            "REGION_POP": "4 JOB - Region Code + Poppulation",
            # "GDP": "5 JOB",
            # "UNSOLD": "6 JOB",
            # "PRICE": "7 JOB"
        }
        for job, desc in job_list.items():
            self.logger.info(f"{job} : Start # {desc}")
            # self.extract.get_data_by_curl(get_type=f'{job}')
            self.transform.preprocessing(pre_type=f'{job}')

    def real_estate(self, selected_month, key):
        """
        data.go.kr에서 molit.go.kr API를 제공한다.
        제공된 API로 실거래와 전세가를 추출할 수 있다.
        매일 한달 정도의 데이터를 가져오는 것이 최선이다.
        여러 API 키를 써도 IP를 체크하는지 사용이 불가하다.
        :return:
        """

        self.logger.info("code initializing")
        codes = self.extract.read_code_file()
        self.logger.info("code initialized : " + str(len(codes)))
        self.logger.info("data extract" + ' - ' + selected_month)
        self.extract.make_tx_df(ACTUAL_TX_URL, key, codes, selected_month, df_type="actual_tx")
        self.extract.make_tx_df(CHARTERED_RENT_URL, key, codes, selected_month, df_type="chartered_rent")

    def real_estate_pre(self):
        """
        gzip으로 된 파일을 csv로 변경하고 하나로 합친다.
        거래일을 년,월,분기로 나누고 Null값 처리한다.
        GDP, 물가, 미분양 필드를 추가한다.
        2011년 부터 데이터가 만들어지는 이유는 전월세 데이터가 2011년 부터 이기 때문이다.
        :return:
        """
        self.logger.info("gzip to csv")
        self.transform.gzip_to_csv()
        self.logger.info("TX preprocessing")
        self.transform.preprocessing(pre_type='TX')
        self.logger.info("TX End")
        self.logger.info("TX ALL preprocessing")
        self.transform.preprocessing(pre_type='TX_ALL_PRE')
        self.logger.info("TX ALL End")

    def additional_insight(self, target):
        """
        추가적인 Insight가 생기면 지속적으로 기능이 만들어지는 함수이다.
        :param target:
        :return:
        """
        if target == '1':
            #인구수, 월간 거래금액, 분기 거래금액, 년간 거리금액 Join Data
            self.logger.info("도시별, 인구수, 월간 거래금액")
            self.transform.additional_insight_detail(target='1')
        else:
            df = ''

    def export_elasticsearch(self):
        """
        아래 딕셔너리를 참고하여 데이터를 삽입한다.
            "AC_CH": "ac_ch.csv",
            "GDP": "GDP_pre.csv",
            "POPULATION": "population_pre.csv",
            "PRICE": "PRICE_pre.csv",
            "UNSOLD": "UNSOLD_pre.csv",
            "ACTUAL_MASTER": "actual_tx_master.csv",
            "CHARTERED_RENT_MASTER": "chartered_rent_master.csv",
            "ACTUAL_DETAIL": "actual_tx_detail.csv",
            "CHARTERED_RENT_DETAIL": "chartered_rent_detail.csv"
        :return:
        """

        export_list = {
            # "AC_CH": "ac_ch.csv",
            # "GDP": "GDP_pre.csv",
            "POPULATION": "population_pre.csv",
            # "PRICE": "PRICE_pre.csv",
            # "UNSOLD": "UNSOLD_pre.csv",
            # "ACTUAL_MASTER": "actual_tx_master.csv",
            # "CHARTERED_RENT_MASTER": "chartered_rent_master.csv",
            # "ACTUAL_DETAIL": "actual_tx_detail.csv",
            # "CHARTERED_RENT_DETAIL": "chartered_rent_detail.csv"
        }

        for key, value in export_list.items():
            target = key
            index_nm, mapping = self.qes.field_date(target=target)
            csv = CSV_DIRECTORY + value
            self.export.call_export_data_to_elasticsearch(index_nm, mapping, csv, target)

    def export_mongodb(self):
        export_csv_list = {
            # "code": "code.csv",
            # "AC_CH": "ac_ch.csv",
            # "GDP": "GDP_pre.csv",
            # "POPULATION": "population_pre.csv",
            # "PRICE": "PRICE_pre.csv",
            # "UNSOLD": "UNSOLD_pre.csv",
            "POPULATION_FULL": "population_full_pre_extend.csv",
        }

        export_final_list = {
            "ACTUAL_MASTER": "actual_tx_master.csv",
            "CHARTERED_RENT_MASTER": "chartered_rent_master.csv",
            "ACTUAL_DETAIL": "actual_tx_detail.csv",
            "CHARTERED_RENT_DETAIL": "chartered_rent_detail.csv"
        }

        for key, value in export_csv_list.items():
            self.export.call_remove_export_data_to_mongo(key, CSV_DIRECTORY + value)

        # for key, value in export_final_list.items():
        #     self.export.call_remove_export_data_to_mongo(key, AC_CH_FINAL_DIRECTORY + value)
        #     #self.export.call_export_data_to_mongo(key, AC_CH_FINAL_DIRECTORY + value)
