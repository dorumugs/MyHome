from src.core.core_extract import CoreExtract
from utils.database.database_config import DatabaseConfig
from utils.log import logger
from config.project_env.directory_config import *
from config.molit_go_kr.actual_tx_and_chartered_rent import *
from config.kosis_kr.population import *
from config.kosis_kr.population_post import *
from config.kosis_kr.population_full import *
from config.kosis_kr.population_full_post import *
from config.kosis_kr.prices import *
from config.kosis_kr.unsold import *
from config.index_go_kr.gdp import *
from config.juso_go_kr.region_code import *
from config.code_go_kr.reg_region_code import *
import pandas as pd
import numpy as np
import requests
import json
import calendar
from bs4 import BeautifulSoup


class ExtendsExtract(CoreExtract):
    def __init__(self, _logger=None, extends_sqlalchemy=None):
        if _logger is None:
            self.logger = logger.setup_logger("[Extract]")
        else:
            self.logger = _logger
        super().__init__(extends_sqlalchemy)
        self.database_config = DatabaseConfig()

    @staticmethod
    def read_code_file():
        csv = pd.read_csv(CSV_DIRECTORY + "code.csv", sep=',', encoding='utf-8')
        csv["code"] = csv.법정동코드.apply(lambda x: str(x)[0:5])
        codes = list(set(csv.code.to_list()))
        return codes

    @staticmethod
    def create_date_range(selected_month):
        year_sm = selected_month.split('-')[0]
        day_sm = selected_month.split('-')[1]
        day_end = calendar.monthrange(int(year_sm), int(day_sm))
        date_list = pd.date_range(start=f'{selected_month}-01', end=f'{selected_month}-{day_end[1]}')
        date_list = list(set(date_list.format(formatter=lambda x: x.strftime("%Y%m"))))
        return date_list

    def make_tx_df(self, url, service_key, codes, selected_month, df_type):
        date_list = self.create_date_range(selected_month)
        if df_type == "actual_tx":
            df = pd.DataFrame(columns=ACTUAL_TX_COLUMNS)
        elif df_type == "chartered_rent":
            df = pd.DataFrame(columns=CHARTERED_RENT_TX_COLUMNS)
        else:
            df = pd.DataFrame()

        for date in date_list:
            if df_type == "actual_tx":
                each_df = self.request_api(ACTUAL_TX_COLUMNS, url, service_key, codes, date)
                each_df = each_df[ACTUAL_TX_COLUMNS]
                df = pd.concat([df, each_df], axis=0)
                self.logger.info(f"{date} actual_tx")
                df.to_parquet(ACTUAL_TX_DIRECTORY + "df_" + str(date) + ".gzip", compression="gzip")
            elif df_type == "chartered_rent":
                each_df = self.request_api(CHARTERED_RENT_TX_COLUMNS, url, service_key, codes, date)
                each_df = each_df[CHARTERED_RENT_TX_COLUMNS]
                df = pd.concat([df, each_df], axis=0)
                self.logger.info(f"{date} chartered_rent")
                df.to_parquet(CHARTERED_RENT_DIRECTORY + "df_" + str(date) + ".gzip", compression="gzip")
        return df

    @staticmethod
    def get_kosis_data(get_type, csv, url, headers, cookies, data, date_data=None):
        response = requests.get(url, headers=headers, cookies=cookies, data=data)
        text = json.loads(response.text)
        res_file = text['file']
        if get_type == 'UNSOLD':
            UNSOLD_DOWN_URL = unsold_url(res_file)
            response = requests.get(UNSOLD_DOWN_URL, headers=UNSOLD_DOWN_HEADERS, cookies=UNSOLD_DOWN_COOKIES,
                                    data=create_unsold_download_data())
        elif get_type == 'PRICE':
            response = requests.get(PRICE_DOWN_URL, headers=PRICES_HEADERS, cookies=PRICES_COOKIES,
                                    data=create_price_download_data(res_file))
        elif get_type == 'POPULATION':
            POPULATION_DOWN_DATA = make_population_down_data(res_file)
            response = requests.get(POPULATION_DOWN_URL, headers=POPULATION_DOWN_HEADER,
                                    cookies=POPULATION_DOWN_COOKIES, data=POPULATION_DOWN_DATA)
        elif get_type == 'POPULATION_POST':
            POPULATION_DOWN_POST_DATA = make_population_post_down_data(res_file)
            response = requests.get(POPULATION_DOWN_POST_URL, headers=POPULATION_DOWN_POST_HEADER,
                                    cookies=POPULATION_DOWN_POST_COOKIES, data=POPULATION_DOWN_POST_DATA)
        elif get_type == 'POPULATION_FULL':
            POPULATION_FULL_DOWN_DATA = make_population_full_down_data(res_file, date_data)
            response = requests.get(POPULATION_FULL_DOWN_URL, headers=POPULATION_FULL_DOWN_HEADER,
                                    cookies=POPULATION_FULL_DOWN_COOKIES, data=POPULATION_FULL_DOWN_DATA)
        elif get_type == 'POPULATION_FULL_POST':
            POPULATION_FULL_POST_DOWN_DATA = make_population_full_post_down_data(res_file, date_data)
            response = requests.get(POPULATION_FULL_POST_DOWN_URL, headers=POPULATION_FULL_POST_DOWN_HEADER,
                                    cookies=POPULATION_FULL_POST_DOWN_COOKIES, data=POPULATION_FULL_POST_DOWN_DATA)

        with open(csv, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=1024):
                fd.write(chunk)

    def get_data_by_curl(self, get_type):
        if get_type == 'GDP':
            response = requests.post(GDP_URL, headers=GDP_HEADERS, cookies=GDP_COOKIES, data=GDP_DATA)
            soup = BeautifulSoup(response.content, 'html.parser')
            tbl = soup.find("table", {"id": "t_Table_273601"})
            df = pd.read_html(str(tbl))[0].reset_index(drop=True).dropna()
            df = df.reset_index(drop=True).T
            df.rename(columns=df.iloc[0], inplace=True)
            df = df.drop(df.index[0]).reset_index().rename(columns={
                'index': '년분기', '국내총생산(명목GDP)': 'Nominal_GDP', '경제성장률(실질GDP성장률)': 'Real_GDP'
            })
            df.to_csv(CSV_DIRECTORY + "GDP.csv", sep='|', na_rep='NaN', index=False)
        elif get_type == 'REG_REGION_CODE':
            response = requests.post(CODE_URL, headers=CODE_HEADERS, cookies=CODE_COOKIES, data=CODE_DATA)
            with open(CSV_DIRECTORY + "code.zip", 'wb') as fd:
                for chunk in response.iter_content(chunk_size=1024):
                    fd.write(chunk)
        elif get_type == 'REGION_CODE_FULL':
            response = requests.get(REGION_CODE_FULL_URL, headers=REGION_FULL_HEADERS, cookies=REGION_FULL_COOKIES)
            with open(REGION_CODE_DIRECTORY + "REGION_CODE_FULL.zip", 'wb') as fd:
                for chunk in response.iter_content(chunk_size=1024):
                    fd.write(chunk)
        elif get_type == 'POPULATION':
            csv = CSV_DIRECTORY + "population.csv"
            self.get_kosis_data(get_type, csv, POPULATION_URL, POPULATION_HEADERS, POPULATION_COOKIES, POPULATION_DATA)
        elif get_type == 'POPULATION_POST':
            csv = CSV_DIRECTORY + "population_post.csv"
            self.get_kosis_data(get_type, csv, POPULATION_POST_URL, POPULATION_POST_HEADERS, POPULATION_POST_COOKIES,
                                POPULATION_POST_DATA)
        elif get_type == 'POPULATION_FULL':
            csv = CSV_DIRECTORY + "population_full.csv"
            currentyear_2020 = '2020'
            currentyear_2015 = '2015'
            index = sorted(list(
                set(
                    [x.strftime('%Y') for x in pd.date_range(start=currentyear_2015, end=currentyear_2020).to_list()]
                )
            ), reverse=True)
            index = [str(x) for x in index if int(x) % 5 == 0]

            df = pd.DataFrame()
            for i in index:
                self.get_kosis_data(get_type, csv, POPULATION_FULL_URL, POPULATION_FULL_HEADERS, POPULATION_FULL_COOKIES,
                                    make_population_full_data(i), i)
                pop = pd.read_csv(csv, sep=',', encoding='cp949')
                df = pd.concat([df, pop], axis=0)
            df.to_csv(csv, sep=',', na_rep='NaN', index=False, encoding='cp949')
        elif get_type == 'POPULATION_FULL_POST':
            csv = CSV_DIRECTORY + "population_full_post.csv"
            df = pd.DataFrame()
            for index in POPULATION_FULL_POST_INDEX:
                self.get_kosis_data(get_type, csv, POPULATION_FULL_POST_URL, POPULATION_FULL_POST_HEADERS,
                                    POPULATION_FULL_POST_COOKIES,
                                    make_population_full_post_data(index), index)
                pop = pd.read_csv(csv, sep=',', encoding='cp949')
                pop = pop.rename(columns={
                    '행정구역별': '행정구역별(읍면동)',
                    '시점': '시점',
                    '인구 (명)': '총인구 (명)',
                    '일반가구 (가구)': '일반가구 (가구)',
                    '일반가구수 (가구)': '일반가구 (가구)',
                    '가구 (가구)': '일반가구 (가구)'
                })
                df = pd.concat([df, pop], axis=0)
            df.to_csv(csv, sep=',', na_rep='NaN', index=False, encoding='cp949')
        elif get_type == 'UNSOLD':
            csv = CSV_DIRECTORY + "UNSOLD.csv"
            self.get_kosis_data(get_type, csv, UNSOLD_URL, UNSOLD_HEADERS, UNSOLD_COOKIES, create_unsold_data())
        elif get_type == 'PRICE':
            csv = CSV_DIRECTORY + "PRICE.csv"
            self.get_kosis_data(get_type, csv, PRICES_URL, PRICES_HEADERS, PRICES_COOKIES, create_price_data())

