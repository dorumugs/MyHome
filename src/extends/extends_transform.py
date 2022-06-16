from src.core.core_transform import CoreTransform
from utils.database.database_config import DatabaseConfig
from config.project_env.directory_config import *
from config.molit_go_kr.actual_tx_and_chartered_rent import *
import os
import zipfile
from utils.log import logger
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
import shutil


class ExtendsTransform(CoreTransform):
    def __init__(self, _logger=None, extends_sqlalchemy=None):
        if _logger is None:
            self.logger = logger.setup_logger("[TRANSFORM]")
        else:
            self.logger = _logger
        super().__init__(extends_sqlalchemy)
        self.database_config = DatabaseConfig()

    @staticmethod
    def gzip_to_csv_sub(add_columns, origin_columns, base_dir, csv_dir, i, tx):
        df = pd.read_parquet(base_dir + i)
        for c in add_columns:
            if c in df.columns:
                pass
            else:
                df[c] = ''
        df = df[origin_columns]
        tx = pd.concat([tx, df], axis=0)
        df.to_csv(csv_dir + i.split()[0] + '.csv', sep='|')
        return tx

    def gzip_to_csv(self):
        os.makedirs(ACTUAL_TX_DIRECTORY_CSV, exist_ok=True)
        os.makedirs(CHARTERED_RENT_DIRECTORY_CSV, exist_ok=True)
        actual_tx_list = [f for f in listdir(ACTUAL_TX_DIRECTORY) if isfile(join(ACTUAL_TX_DIRECTORY, f))]
        chartered_rent_list = [f for f in listdir(CHARTERED_RENT_DIRECTORY) if isfile(join(CHARTERED_RENT_DIRECTORY, f))]
        actual_tx = pd.DataFrame(columns=['index'] + ACTUAL_TX_COLUMNS)
        chartered_rent = pd.DataFrame(columns=['index'] + CHARTERED_RENT_TX_COLUMNS)

        self.logger.info('Actual TX to CSV')
        for i in actual_tx_list:
            actual_tx = self.gzip_to_csv_sub(IN_ACTUAL_TX_COLUMNS, ACTUAL_TX_COLUMNS,
                                             ACTUAL_TX_DIRECTORY, ACTUAL_TX_DIRECTORY_CSV, i, actual_tx)
        self.logger.info('Chartered Rent TX to CSV')
        for i in chartered_rent_list:
            chartered_rent = self.gzip_to_csv_sub(IN_CHARTERED_RENT_TX_COLUMNS, CHARTERED_RENT_TX_COLUMNS,
                                                  CHARTERED_RENT_DIRECTORY, CHARTERED_RENT_DIRECTORY_CSV, i,
                                                  chartered_rent)

        actual_tx = actual_tx[ACTUAL_TX_COLUMNS]
        chartered_rent = chartered_rent[CHARTERED_RENT_TX_COLUMNS]
        actual_tx.to_csv(ACTUAL_TX_FINAL, sep='|', index=False)
        chartered_rent.to_csv(CHARTERED_RENT_FINAL, sep='|', index=False)
        shutil.rmtree(ACTUAL_TX_DIRECTORY_CSV)
        shutil.rmtree(CHARTERED_RENT_DIRECTORY_CSV)

    @staticmethod
    def date_one_to_date_two(x):
        if len(str(x.월)) == 1:
            x.월 = '0' + str(x.월)
        if "일" in x:
            if len(str(x.일)) == 1:
                x.일 = '0' + str(x.일)
        else:
            return str(x.년) + '-' + str(x.월) + '-' + '01'
        return str(x.년) + '-' + str(x.월) + '-' + str(x.일)

    def tx_data_pre(self):
        for csv in [ACTUAL_TX_FINAL, CHARTERED_RENT_FINAL]:
            df = pd.read_csv(csv, delimiter='|', low_memory=False)
            df['거래일'] = df.apply(lambda x: self.date_one_to_date_two(x), axis=1)
            df['분기'] = df.거래일.apply(lambda x: (int(x.split('-')[1]) - 1) // 3 + 1)
            df['지역코드'] = df['지역코드'].fillna('00000')
            df['법정동'] = df.법정동.apply(lambda x: str(x).lstrip().rstrip())
            df['지역코드'] = df.지역코드.apply(lambda x: ''.join(str(x).split('.')[0]))

            if csv == ACTUAL_TX_FINAL:
                df['거래금액'] = df.거래금액.apply(lambda x: int(''.join((str(x).split(',')))))
                df = df[ACTUAL_TX_COLUMNS + ['거래일'] + ['분기']]

            elif csv == CHARTERED_RENT_FINAL:
                df['보증금액'] = df['보증금액'].fillna(int(0))
                df['월세금액'] = df['월세금액'].fillna(int(0))
                df['보증금액'] = df.보증금액.apply(
                    lambda x: int(0) if len(str(x).strip()) == 0 else int(float(''.join((str(x).split(','))))))
                df['월세금액'] = df.월세금액.apply(
                    lambda x: int(0) if len(str(x).strip()) == 0 else int(float(''.join((str(x).split(','))))))
                df = df[CHARTERED_RENT_TX_COLUMNS + ['거래일'] + ['분기']]

            df.to_csv('/'.join(csv.split('/')[0:-1]) + '/pre_' + csv.split('/')[-1], sep='|', index=False)

    @staticmethod
    def rate_of_change(ac_ch, x_year='Non', x_month='Non', x_quarter='Non', target='yqm'):
        ac_ch_sdm = list(set(ac_ch.시도명.to_list()))
        df_year = pd.DataFrame()
        df_month = pd.DataFrame()
        df_quarter = pd.DataFrame()
        rate_of_tx = pd.DataFrame()
        for i in ac_ch_sdm:
            df_1 = ac_ch[ac_ch['시도명'] == i]
            df_1_sggm = list(set(df_1.시군구명.to_list()))
            for ii in df_1_sggm:
                if x_year != 'Non':
                    df_2 = df_1[df_1['시군구명'] == ii][['년', '시도명', '시군구명', x_year]].sort_values(
                        ['년', '시도명', '시군구명']).drop_duplicates().reset_index(drop=True)
                    df_2[x_year + '_증감률'] = df_2[x_year].pct_change()
                    df_year = pd.concat([df_year, df_2], axis=0)
                if x_month != 'Non':
                    df_2 = df_1[df_1['시군구명'] == ii][['년', '월', '시도명', '시군구명', x_month]].sort_values(
                        ['년', '월', '시도명', '시군구명']).drop_duplicates().reset_index(drop=True)
                    df_2[x_month + '_증감률'] = df_2[x_month].pct_change()
                    df_month = pd.concat([df_month, df_2], axis=0)
                if x_quarter != 'Non':
                    df_2 = df_1[df_1['시군구명'] == ii][['년', '분기', '시도명', '시군구명', x_quarter]].sort_values(
                        ['년', '분기', '시도명', '시군구명']).drop_duplicates().reset_index(drop=True)
                    df_2[x_quarter + '_증감률'] = df_2[x_quarter].pct_change()
                    df_quarter = pd.concat([df_quarter, df_2], axis=0)
        if target == 'yqm':
            df_year = df_year.reset_index(drop=True)
            df_month = df_month.reset_index(drop=True)
            df_quarter = df_quarter.reset_index(drop=True)
            rate_of_tx = pd.merge(left=df_month, right=df_year, how='left', left_on=['년', '시도명', '시군구명'],
                                  right_on=['년', '시도명', '시군구명'])
            rate_of_tx['분기'] = rate_of_tx.월.apply(lambda x: (x - 1) // 3 + 1)
            rate_of_tx = pd.merge(left=rate_of_tx, right=df_quarter, how='left', left_on=['년', '분기', '시도명', '시군구명'],
                                  right_on=['년', '분기', '시도명', '시군구명'])
        elif target == 'yq':
            df_year = df_year.reset_index(drop=True)
            df_quarter = df_quarter.reset_index(drop=True)
            rate_of_tx = pd.merge(left=df_quarter, right=df_year, how='left', left_on=['년', '시도명', '시군구명'],
                                  right_on=['년', '시도명', '시군구명'])
        elif target == 'y':
            rate_of_tx = df_year.reset_index(drop=True)
        return rate_of_tx

    def ac_ch_pre(self, ac_tx, ch_tx):
        actual_tx_year = pd.DataFrame(ac_tx[['시도명', '시군구명', '년', '월', '분기', '거래금액']].groupby([
            '시도명', '시군구명', '년'])['거래금액'].mean()).reset_index().rename(columns={'거래금액': '거래금액_년'})
        actual_tx_quarter = pd.DataFrame(
            ac_tx[['시도명', '시군구명', '년', '월', '분기', '거래금액']].groupby(['시도명', '시군구명', '년', '분기'])[
                '거래금액'].mean()).reset_index().rename(columns={'거래금액': '거래금액_분기'})
        actual_tx_month = pd.DataFrame(
            ac_tx[['시도명', '시군구명', '년', '월', '분기', '거래금액']].groupby(['시도명', '시군구명', '년', '월', '분기'])[
                '거래금액'].mean()).reset_index().rename(columns={'거래금액': '거래금액_월'})
        month_quarter_ac = pd.merge(actual_tx_month, actual_tx_quarter, how='left', left_on=['시도명', '시군구명', '년', '분기'],
                                    right_on=['시도명', '시군구명', '년', '분기'])
        month_quarter_year_ac = pd.merge(actual_tx_year, month_quarter_ac, how='left', left_on=['시도명', '시군구명', '년'],
                                         right_on=['시도명', '시군구명', '년'])

        chartered_rent_charter_only = ch_tx[ch_tx['월세금액'] == 0]
        chartered_rent_year = pd.DataFrame(
            chartered_rent_charter_only[['시도명', '시군구명', '년', '월', '분기', '보증금액']].groupby(['시도명', '시군구명', '년'])[
                '보증금액'].mean()).reset_index().rename(columns={'보증금액': '보증금액_년'})
        chartered_rent_quarter = pd.DataFrame(
            chartered_rent_charter_only[['시도명', '시군구명', '년', '월', '분기', '보증금액']].groupby(['시도명', '시군구명', '년', '분기'])[
                '보증금액'].mean()).reset_index().rename(columns={'보증금액': '보증금액_분기'})
        chartered_rent_month = pd.DataFrame(
            chartered_rent_charter_only[['시도명', '시군구명', '년', '월', '분기', '보증금액']].groupby(
                ['시도명', '시군구명', '년', '월', '분기'])['보증금액'].mean()).reset_index().rename(columns={'보증금액': '보증금액_월'})
        month_quarter_ch = pd.merge(chartered_rent_month, chartered_rent_quarter, how='left',
                                    left_on=['시도명', '시군구명', '년', '분기'], right_on=['시도명', '시군구명', '년', '분기'])
        month_quarter_year_ch = pd.merge(chartered_rent_year, month_quarter_ch, how='left',
                                         left_on=['시도명', '시군구명', '년'], right_on=['시도명', '시군구명', '년'])
        ac_ch = pd.merge(month_quarter_year_ac, month_quarter_year_ch, how='inner',
                         left_on=['시도명', '시군구명', '년', '월', '분기'],
                         right_on=['시도명', '시군구명', '년', '월', '분기'])
        ac_ch['전세가율_년'] = ac_ch.apply(lambda x: (x.보증금액_년 / x.거래금액_년) * 100, axis=1)
        ac_ch['전세가율_분기'] = ac_ch.apply(lambda x: (x.보증금액_분기 / x.거래금액_분기) * 100, axis=1)
        ac_ch['전세가율_월'] = ac_ch.apply(lambda x: (x.보증금액_월 / x.거래금액_월) * 100, axis=1)
        ac_ch = ac_ch[['시도명', '시군구명', '년', '월', '분기', '거래금액_년', '거래금액_월', '거래금액_분기',
                       '보증금액_년', '보증금액_월', '보증금액_분기', '전세가율_년', '전세가율_월', '전세가율_분기']]

        ac_tx = pd.merge(ac_tx, ac_ch, how='left', left_on=['시도명', '시군구명', '년', '월', '분기'],
                         right_on=['시도명', '시군구명', '년', '월', '분기'])
        ac_tx = ac_tx[['시도명', '시군구명', '법정동', '지번', '지역코드', '건축년도', '아파트', '전용면적', '층', '거래일',
                       '거래금액', '년', '월', '일', '분기', '총인구_명', 'Nominal_GDP_년', 'Nominal_GDP_분기', 'Real_GDP_년',
                       'Real_GDP_분기', '총지수_물가_년', '총지수_물가_분기', '미분양_개수_년', '미분양_개수_분기', '거래금액_년',
                       '거래금액_분기', '거래금액_월', '보증금액_년', '보증금액_분기', '보증금액_월', '전세가율_년', '전세가율_분기',
                       '전세가율_월']]

        ch_tx = pd.merge(ch_tx, ac_ch, how='left', left_on=['시도명', '시군구명', '년', '월', '분기'],
                         right_on=['시도명', '시군구명', '년', '월', '분기'])
        ch_tx = ch_tx[['시도명', '시군구명', '법정동', '지번', '지역코드', '건축년도', '아파트', '전용면적', '층', '거래일',
                       '보증금액', '월세금액', '년', '월', '일', '분기', '총인구_명', 'Nominal_GDP_년', 'Nominal_GDP_분기',
                       'Real_GDP_년', 'Real_GDP_분기', '총지수_물가_년', '총지수_물가_분기', '미분양_개수_년', '미분양_개수_분기',
                       '거래금액_년', '거래금액_분기', '거래금액_월', '보증금액_년', '보증금액_분기', '보증금액_월', '전세가율_년',
                       '전세가율_분기', '전세가율_월']]

        ac_ch = ac_tx[['시도명', '시군구명', '년', '월', '분기', '거래금액_년', '거래금액_분기', '거래금액_월',
                       '보증금액_년', '보증금액_분기', '보증금액_월', '전세가율_년', '전세가율_분기', '전세가율_월',
                       '총인구_명', 'Nominal_GDP_년', 'Nominal_GDP_분기', 'Real_GDP_년', 'Real_GDP_분기',
                       '총지수_물가_년', '총지수_물가_분기', '미분양_개수_년', '미분양_개수_분기']].drop_duplicates()

        rate_of_tx = self.rate_of_change(ac_ch, x_year='거래금액_년', x_month='거래금액_월', x_quarter='거래금액_분기', target='yqm')
        rate_of_deposit = self.rate_of_change(ac_ch, x_year='보증금액_년', x_month='보증금액_월', x_quarter='보증금액_분기',
                                              target='yqm')
        rate_of_ch = self.rate_of_change(ac_ch, x_year='전세가율_년', x_month='전세가율_월', x_quarter='전세가율_분기', target='yqm')

        rate_of_price = self.rate_of_change(ac_ch, x_year='총지수_물가_년', x_month='Non', x_quarter='총지수_물가_분기', target='yq')
        rate_of_unsold = self.rate_of_change(ac_ch, x_year='미분양_개수_년', x_month='Non', x_quarter='미분양_개수_분기',
                                             target='yq')
        rate_of_NGDP = self.rate_of_change(ac_ch, x_year='Nominal_GDP_년', x_month='Non', x_quarter='Nominal_GDP_분기',
                                           target='yq')
        rate_of_RGDP = self.rate_of_change(ac_ch, x_year='Real_GDP_년', x_month='Non', x_quarter='Real_GDP_분기',
                                           target='yq')

        rate_of_all = pd.merge(left=rate_of_tx, right=rate_of_deposit, how='left',
                               left_on=['년', '월', '분기', '시도명', '시군구명'], right_on=['년', '월', '분기', '시도명', '시군구명'])
        rate_of_all = pd.merge(left=rate_of_all, right=rate_of_ch, how='left', left_on=['년', '월', '분기', '시도명', '시군구명'],
                               right_on=['년', '월', '분기', '시도명', '시군구명'])
        rate_of_all = pd.merge(left=rate_of_all, right=rate_of_price, how='left', left_on=['년', '분기', '시도명', '시군구명'],
                               right_on=['년', '분기', '시도명', '시군구명'])
        rate_of_all = pd.merge(left=rate_of_all, right=rate_of_unsold, how='left', left_on=['년', '분기', '시도명', '시군구명'],
                               right_on=['년', '분기', '시도명', '시군구명'])
        rate_of_all = pd.merge(left=rate_of_all, right=rate_of_NGDP, how='left', left_on=['년', '분기', '시도명', '시군구명'],
                               right_on=['년', '분기', '시도명', '시군구명'])
        rate_of_all = pd.merge(left=rate_of_all, right=rate_of_RGDP, how='left', left_on=['년', '분기', '시도명', '시군구명'],
                               right_on=['년', '분기', '시도명', '시군구명'])

        ac_ch_final = pd.merge(left=ac_ch, right=rate_of_all, how='left', left_on=['년', '월', '분기', '시도명', '시군구명'],
                               right_on=['년', '월', '분기', '시도명', '시군구명'], suffixes=('', '_drop'))
        ac_ch_final.drop([col for col in ac_ch_final.columns if 'drop' in col], axis=1, inplace=True)
        # ac_ch_final = ac_ch_final.dropna()

        ac_ch_final['날짜'] = ac_ch_final.apply(lambda x: self.date_one_to_date_two(x), axis=1)

        ac_ch_final.to_csv('./data/csv/ac_ch.csv', sep='|', index=False)

        return ac_tx, ch_tx

    @staticmethod
    def tx_pre(tx_origin, region_pop, gdp, price, unsold):
        tx = pd.merge(tx_origin, region_pop, how='left', left_on=['지역코드', '년'], right_on=['시군구', '시점']).drop(columns=['시군구', '시점'])
        tx = pd.merge(tx, gdp, how='left', left_on=['년', '분기'], right_on=['년', '분기'])
        tx = pd.merge(tx, price, how='left', left_on=['년', '분기'], right_on=['년', '분기'])
        tx = pd.merge(tx, unsold, how='left', left_on=['시도명', '년', '분기'], right_on=['시도명', '년', '분기'])
        return tx

    def tx_data_all_pre(self):
        #시군구,시도명,시군구명,총인구_명,시점
        region_pop = pd.read_csv(CSV_DIRECTORY + "region_pop_full.csv", sep=',', encoding='utf-8', low_memory=False)
        region_pop = region_pop[['시군구', '시도명', '시군구명', '총인구_명', '시점']].drop_duplicates()
        gdp = pd.read_csv(CSV_DIRECTORY + "GDP_pre.csv", sep='|')
        price = pd.read_csv(CSV_DIRECTORY + "PRICE_pre.csv", sep='|')
        unsold = pd.read_csv(CSV_DIRECTORY + "UNSOLD_pre.csv", sep='|')

        actual_tx = pd.read_csv(AC_CH_FINAL_DIRECTORY + "pre_actual_tx.csv", sep='|', encoding='utf-8',
                                low_memory=False)
        # actual_tx = actual_tx[actual_tx['년'] >= 2011]
        chartered_rent = pd.read_csv(AC_CH_FINAL_DIRECTORY + "pre_chartered_rent.csv", sep='|',
                                     encoding='utf-8', low_memory=False)
        # chartered_rent = chartered_rent[chartered_rent['년'] >= 2011]

        ac_tx = self.tx_pre(actual_tx, region_pop, gdp, price, unsold)
        ch_tx = self.tx_pre(chartered_rent, region_pop, gdp, price, unsold)

        ac_tx, ch_tx = self.ac_ch_pre(ac_tx, ch_tx)

        ac_tx.to_csv(AC_CH_FINAL_DIRECTORY + "actual_tx_detail.csv", sep='|', index=False)
        ac_tx_pre = ac_tx[ACTUAL_TX_COLUMNS_PRE]
        ac_tx_pre = ac_tx_pre.replace(' ', '')
        ac_tx_pre = ac_tx_pre.replace('', 0)
        ac_tx_pre.to_csv(AC_CH_FINAL_DIRECTORY + "actual_tx_master.csv", sep='|', index=False)
        ch_tx.to_csv(AC_CH_FINAL_DIRECTORY + "chartered_rent_detail.csv", sep='|', index=False)
        ch_tx_pre = ch_tx[CHARTERED_RENT_TX_COLUMNS_PRE]
        ch_tx_pre = ch_tx_pre.replace(' ', '')
        ch_tx_pre = ch_tx_pre.replace('', 0)
        ch_tx_pre.to_csv(AC_CH_FINAL_DIRECTORY + "chartered_rent_master.csv", sep='|', index=False)
        # os.remove(AC_CH_FINAL_DIRECTORY + "pre_actual_tx.csv")
        # os.remove(AC_CH_FINAL_DIRECTORY + "pre_chartered_rent.csv")

    @staticmethod
    def city_name(x):
        pop_city_index_file = open("./config/POP_CITY_INDEX.txt", "r")
        content = pop_city_index_file.read()
        pop_city_index = content.split(",")
        pop_city_index = [i for i in pop_city_index if i != '']
        pop_city_index_file.close()

        pop_city_list_file = open("./config/POP_CITY_LIST.txt", "r")
        content = pop_city_list_file.read()
        pop_city_list = content.split(",")
        pop_city_list = [i for i in pop_city_list if i != '']
        pop_city_list_file.close()

        for i in range(len(pop_city_index)):
            if i != len(pop_city_index) - 1:
                if x.name >= int(pop_city_index[i]) and x.name < int(pop_city_index[i + 1]):
                    return pop_city_list[i]
            else:
                if x.name >= int(pop_city_index[i]):
                    return pop_city_list[i]

    @staticmethod
    def population_settings(csv, pop):
        region_code = pd.read_csv(REGION_CODE_DIRECTORY + "REGION_CODE_FULL.csv", sep='|', encoding='utf-8',
                                  low_memory=False)
        city = pd.DataFrame(region_code.시도명.value_counts()).reset_index().rename(columns={"index": "시도명", "시도명": "시군구"})
        city_list = city.시도명.to_list()
        pop_city_index = pop[pop['행정구역별(읍면동)'].isin(city_list)].index.to_list()
        pop_city_index.insert(0, 0)
        pop_city_list = pop[pop.index.isin(pop_city_index)]
        pop_city_list = pop_city_list['행정구역별(읍면동)'].to_list()

        with open('./config/POP_CITY_INDEX.txt', 'w') as f:
            for item in pop_city_index:
                if pop_city_index[-1] != item:
                    f.write("%s," % item)
                else:
                    f.write("%s," % item)

        with open('./config/POP_CITY_LIST.txt', 'w') as f:
            for item in pop_city_list:
                if pop_city_list[-1] != item:
                    f.write("%s," % item)
                else:
                    f.write("%s," % item)

    @staticmethod
    def population_full_settings(sgg_list, pop):
        sgg_0 = [s.split('-')[0] for s in sgg_list]
        sgg_1 = [s.split('-')[1] for s in sgg_list]
        sgg_0.insert(0, sgg_1[0])
        pop_city_index = pop[pop['행정구역별_읍면동'].isin(sgg_0)].index.to_list()
        pop_city_list = pop[pop.index.isin(pop_city_index)]
        pop_city_list = pop_city_list['행정구역별_읍면동'].to_list()

        with open('./config/POP_CITY_INDEX.txt', 'w') as f:
            for item in pop_city_index:
                if pop_city_index[-1] != item:
                    f.write("%s," % item)
                else:
                    f.write("%s," % item)

        with open('./config/POP_CITY_LIST.txt', 'w') as f:
            for item in pop_city_list:
                if pop_city_list[-1] != item:
                    f.write("%s," % item)
                else:
                    f.write("%s," % item)

    @staticmethod
    def remove_pop_city_files():
        pop_city_files = ['./config/POP_CITY_INDEX.txt', './config/POP_CITY_LIST.txt']
        for file in pop_city_files:
            if os.path.isfile(file):
                os.remove(file)

    def population_pre(self, input_csv, output_csv):
        pop = pd.read_csv(CSV_DIRECTORY + input_csv, sep=',', encoding='cp949')
        pop = pop.rename(columns={
            '행정구역별': '행정구역별(읍면동)',
            '시점': '시점',
            '인구 (명)': '총인구 (명)'
        })
        self.population_settings(input_csv, pop)
        pop['시도명'] = pop.apply(self.city_name, axis=1)
        pop['날짜'] = pop.시점.apply(lambda x: str(x) + '-01-01')
        self.remove_pop_city_files()
        pop = pop.replace('X', 0)
        pop_pre = pop.rename(columns={
            '행정구역별(읍면동)': '행정구역별_읍면동',
            '시점': '시점',
            '날자': '날짜',
            '총인구 (명)': '총인구_명',
            '남자 (명)': '남자_명',
            '여자 (명)': '여자_명',
            '일반가구 (가구)': '일반가구_가구',
            '주택-계 (호)': '주택-계_호',
            '단독주택 (호)': '단독주택_호',
            '아파트 (호)': '아파트_호',
            '연립주택 (호)': '연립주택_호',
            '다세대주택 (호)': '다세대주택_호',
            '비거주용 건물내 주택 (호)': '비거주용건물내주택_호',
            '주택이외의 거처 (호)': '주택이외의거처_호',
            '시도명': '시도명'
        })
        pop_pre.to_csv(CSV_DIRECTORY + output_csv, sep='|', na_rep='NaN', index=False)

    def population_post_pre(self, left_csv, right_csv, output_csv):
        left = pd.read_csv(CSV_DIRECTORY + left_csv, sep='|', encoding='utf-8')
        left_remains = left[['행정구역별_읍면동', '시점', '총인구_명', '시도명', '날짜']]

        right = pd.read_csv(CSV_DIRECTORY + right_csv, sep='|', encoding='utf-8')

        full_df = pd.DataFrame()

        date_list = sorted(list(set(right['시점'].to_list())), reverse=True)
        for d in date_list:
            right_date = right[right['시점'] == d]
            add_date = right_date[['시점']]
            add_remains = right_date[['행정구역별_읍면동', '총인구_명', '시도명']]
            add_1 = pd.concat([(add_date + 1), add_remains], axis=1)
            add_2 = pd.concat([(add_date + 2), add_remains], axis=1)
            add_3 = pd.concat([(add_date + 3), add_remains], axis=1)
            add_4 = pd.concat([(add_date + 4), add_remains], axis=1)
            right_date = right_date.append(add_1[['행정구역별_읍면동', '시점', '총인구_명', '시도명']])
            right_date = right_date.append(add_2[['행정구역별_읍면동', '시점', '총인구_명', '시도명']])
            right_date = right_date.append(add_3[['행정구역별_읍면동', '시점', '총인구_명', '시도명']])
            right_date = right_date.append(add_4[['행정구역별_읍면동', '시점', '총인구_명', '시도명']])
            right_date['날짜'] = right_date.시점.apply(lambda x: str(x) + '-01-01')
            full_df = full_df.append(right_date)

        full_df = full_df.append(left_remains)
        full_df.to_csv(CSV_DIRECTORY + output_csv, sep='|', na_rep='NaN', index=False)

    def population_full_pre(self, left_csv, right_csv, output_csv):
        left = pd.read_csv(CSV_DIRECTORY + left_csv, sep='|', encoding='utf-8')
        right = pd.read_csv(CSV_DIRECTORY + right_csv, sep='|', encoding='utf-8')
        right = pd.concat([left, right], axis=0)

        full_df = pd.DataFrame()
        date_list = sorted(list(set(right['시점'].to_list())), reverse=True)
        for d in date_list:
            right_date = right[right['시점'] == d]
            add_date = right_date[['시점']]
            add_remains = right_date[['행정구역별_읍면동', '총인구_명', '일반가구_가구', '시도명']]
            add_1 = pd.concat([(add_date + 1), add_remains], axis=1)
            add_2 = pd.concat([(add_date + 2), add_remains], axis=1)
            add_3 = pd.concat([(add_date + 3), add_remains], axis=1)
            add_4 = pd.concat([(add_date + 4), add_remains], axis=1)
            right_date = right_date.append(add_1[['행정구역별_읍면동', '시점', '총인구_명', '일반가구_가구', '시도명']])
            right_date = right_date.append(add_2[['행정구역별_읍면동', '시점', '총인구_명', '일반가구_가구', '시도명']])
            right_date = right_date.append(add_3[['행정구역별_읍면동', '시점', '총인구_명', '일반가구_가구', '시도명']])
            right_date = right_date.append(add_4[['행정구역별_읍면동', '시점', '총인구_명', '일반가구_가구', '시도명']])
            right_date['날짜'] = right_date.시점.apply(lambda x: str(x) + '-01-01')
            full_df = full_df.append(right_date)
        full_df.to_csv(CSV_DIRECTORY + output_csv, sep='|', na_rep='NaN', index=False)

        full_df = pd.read_csv(CSV_DIRECTORY + output_csv, sep='|', encoding='utf-8')
        sgg = pd.read_csv(CSV_DIRECTORY + 'population_pre.csv', sep='|', encoding='utf-8')
        sgg['행정구역별_시도명'] = sgg.apply(lambda x: x['행정구역별_읍면동'] + '-' + x['시도명'], axis=1)
        sgg_list = list(set(sgg['행정구역별_시도명'].to_list()))
        sdm_list = list(set(sgg['시도명'].to_list()))
        df = pd.DataFrame()
        for sdm in sdm_list:
            s = list(filter(lambda x: sdm in x, sgg_list))
            df_split = full_df[full_df['시도명'] == sdm].copy()
            self.population_full_settings(s, df_split)
            df_split['시군구명'] = df_split.apply(self.city_name, axis=1)
            df = pd.concat([df, df_split], axis=0)
        df = df[['행정구역별_읍면동', '시군구명', '시도명', '시점', '총인구_명', '일반가구_가구', '날짜']]
        df.to_csv(CSV_DIRECTORY + output_csv.split('.')[0] + '_extend.csv', sep='|', na_rep='NaN', index=False)


    def price_pre(self):
        price = pd.read_csv(CSV_DIRECTORY + "PRICE.csv", sep=',', encoding='cp949')
        price_t = price.drop(columns=['시도별']).T.reset_index().rename(columns={'index': '날짜', 0: '총지수'})
        price_t['날짜'] = price_t.날짜.apply(
            lambda x: x if len(str(x).split('.')) == 2 and int(
                str(x).split('.')[0]) > 1964 else np.nan)
        price_t = price_t.dropna().reset_index(drop=True)
        price_t = price_t.astype({
            '총지수': 'float'
        })

        price_t['분기'] = price_t.날짜.apply(lambda x: (int(str(x).split('.')[1]) - 1) // 3 + 1)
        price_t['년'] = price_t.날짜.apply(lambda x: str(x).split('.')[0])
        price_t['월'] = price_t.날짜.apply(lambda x: str(x).split('.')[1])

        left = pd.DataFrame(price_t.groupby(['년', '분기'])['총지수'].mean()).reset_index()
        right = pd.DataFrame(price_t.groupby(['년'])['총지수'].mean()).reset_index()
        price_t = pd.merge(left, right, how='left', left_on=['년'], right_on=['년'], suffixes=['_물가_분기', '_물가_년'])
        price_t['날짜'] = price_t.apply(lambda x: self.create_date_with_quarter(x), axis=1)
        price_t.to_csv(CSV_DIRECTORY + "PRICE_pre.csv", sep='|', na_rep='NaN', index=False)

    @staticmethod
    def city_town_name_replace(x):
        if x == '강원':
            x = '강원도'
        elif x == '경기':
            x = '경기도'
        elif x == '경남':
            x = '경상남도'
        elif x == '경북':
            x = '경상북도'
        elif x == '광주':
            x = '광주광역시'
        elif x == '대구':
            x = '대구광역시'
        elif x == '대전':
            x = '대전광역시'
        elif x == '부산':
            x = '부산광역시'
        elif x == '서울':
            x = '서울특별시'
        elif x == '세종':
            x = '세종특별자치시'
        elif x == '수도권':
            x = np.nan
        elif x == '울산':
            x = '울산광역시'
        elif x == '인천':
            x = '인천광역시'
        elif x == '전국':
            x = np.nan
        elif x == '전남':
            x = '전라남도'
        elif x == '전북':
            x = '전라북도'
        elif x == '제주':
            x = '제주특별자치도'
        elif x == '충남':
            x = '충청남도'
        elif x == '충북':
            x = '충청북도'

        return x

    def unsold_pre(self):
        unsold = pd.read_csv(CSV_DIRECTORY + "UNSOLD.csv", sep=',', encoding='cp949')
        unsold = unsold.fillna(0)
        unsold_date_list = unsold.columns.to_list()[5:-1]

        result = pd.DataFrame()
        for i in unsold_date_list:
            unsold_shape = unsold[i].shape[0]
            df = pd.DataFrame(columns=['날짜', '미분양_개수'])
            for ii in range(unsold_shape):
                add_df = pd.DataFrame(
                    [[str(unsold[i].name).replace('월', '').replace(' ', '').replace('.', ' '),
                      str(int(unsold[i][ii]))]], columns=['날짜', '미분양_개수']
                )
                df = df.append(add_df, ignore_index=True)
                # print(str(unsold[i].name).replace('월','').replace(' ','').replace('.',' '), str(int(unsold[i][ii])))
                if ii == (unsold_shape - 1):
                    df = pd.concat([unsold[['시도', '부문', '규모', '항목']], df], axis=1)
            result = pd.concat([result, df], axis=0)

        result['년'] = result.날짜.apply(lambda x: x.split(' ')[0])
        result['월'] = result.날짜.apply(lambda x: x.split(' ')[1])
        result['분기'] = result.날짜.apply(lambda x: (int(x.split(' ')[1]) - 1) // 3 + 1)
        unsold_pre = result[result['부문'] == '총합'].copy()
        unsold_pre['시도명'] = unsold_pre.시도.apply(lambda x: self.city_town_name_replace(x))
        unsold_pre = unsold_pre.dropna()
        unsold_pre = unsold_pre.astype({'미분양_개수': 'int'})
        left = pd.DataFrame(unsold_pre.groupby(['시도명', '년', '분기'])['미분양_개수'].mean()).reset_index()
        left = left.astype({'미분양_개수': 'int'})
        right = pd.DataFrame(unsold_pre.groupby(['시도명', '년'])['미분양_개수'].mean()).reset_index()
        right = right.astype({'미분양_개수': 'int'})
        unsold_pre = pd.merge(left, right, how='left', left_on=['시도명', '년'], right_on=['시도명', '년'],
                              suffixes=['_분기', '_년'])
        unsold_pre['날짜'] = unsold_pre.apply(lambda x: self.create_date_with_quarter(x), axis=1)
        unsold_pre.to_csv(CSV_DIRECTORY + "UNSOLD_pre.csv", sep='|', na_rep='NaN', index=False)

    @staticmethod
    def create_date_with_quarter(x):
        if x.분기 == 1:
            custom_date = str(int(x.년)) + '-03-01'
        elif x.분기 == 2:
            custom_date = str(int(x.년)) + '-06-01'
        elif x.분기 == 3:
            custom_date = str(int(x.년)) + '-09-01'
        elif x.분기 == 4:
            custom_date = str(int(x.년)) + '-12-01'
        return custom_date

    def gdp_pre(self, gdp, start, end):
        gdp = gdp[(gdp['year'] >= start) & (gdp['year'] < end)]
        gdp = gdp.astype({
            'Nominal_GDP': float,
            'Real_GDP': float
        })
        right = pd.DataFrame(gdp.groupby(['year'])['Nominal_GDP'].mean()).reset_index()
        gdp_pre = pd.merge(gdp, right, how='left', left_on=['year'], right_on=['year'], suffixes=['_분기', '_년'])
        right = pd.DataFrame(gdp.groupby(['year'])['Real_GDP'].mean()).reset_index()
        gdp_pre = pd.merge(gdp_pre, right, how='left', left_on=['year'], right_on=['year'], suffixes=['_분기', '_년'])
        gdp_pre = gdp_pre.rename(columns={
            'year': '년',
            'quarter': '분기'
        })
        gdp_pre['날짜'] = gdp_pre.apply(lambda x: self.create_date_with_quarter(x), axis=1)
        return gdp_pre

    @staticmethod
    def city_town_name(x):
        x_split = x.split(' ')
        if len(x_split) == 2:
            x = x_split[1]
        else:
            x = x_split[0]
        return x

    def preprocessing(self, pre_type):
        if pre_type == 'GDP':
            df = pd.read_csv(CSV_DIRECTORY + "GDP.csv", sep='|', encoding='utf-8', low_memory=False)
            df['checked'] = df.apply(
                lambda x: np.nan if x.년분기 == '-' or x.Nominal_GDP == '-' or x.Real_GDP == '-' else 'Y', axis=1)
            df = df.dropna()
            df['year'] = df.apply(lambda x: int(str(x.년분기[0:4])), axis=1)
            df['quarter'] = df.apply(lambda x: int(str(x.년분기[4:5])), axis=1)
            gdp = df[['year', 'quarter', 'Nominal_GDP', 'Real_GDP']]
            gdp = self.gdp_pre(gdp=gdp, start=1961, end=2022)
            gdp.to_csv(CSV_DIRECTORY + "GDP_pre.csv", sep='|', na_rep='NaN', index=False)
        elif pre_type == 'POPULATION':
            self.population_pre(input_csv="population.csv", output_csv="population_pre.csv")
        elif pre_type == 'POPULATION_POST':
            self.population_pre(input_csv="population_post.csv", output_csv="population_post_pre.csv")
            self.population_post_pre(left_csv="population_pre.csv", right_csv="population_post_pre.csv",
                                     output_csv="population_pre.csv")
        elif pre_type == 'POPULATION_FULL_POST':
            self.population_pre(input_csv="population_full.csv", output_csv="population_full_pre.csv")
            self.population_pre(input_csv="population_full_post.csv", output_csv="population_full_post_pre.csv")
            self.population_full_pre(left_csv="population_full_pre.csv", right_csv="population_full_post_pre.csv",
                                     output_csv="population_full_pre.csv")
        elif pre_type == 'REGION_POP':
            region_code_full = pd.read_csv(REGION_CODE_DIRECTORY + "REGION_CODE_FULL.csv", sep='|', encoding='utf-8',
                                           low_memory=False)
            pop = pd.read_csv(CSV_DIRECTORY + "population_pre.csv", sep='|', encoding='utf-8')
            region_code_full = region_code_full[['시군구', '시도명', '시군구명', '법정읍면동명']]
            # region_code_full['시군구명'] = region_code_full['시군구명'].apply(lambda x: self.city_town_name(str(x)))
            region_code_full['시군구명'] = region_code_full.apply(lambda x: '세종특별자치시' if x.시도명 == '세종특별자치시' else x.시군구명,
                                                              axis=1)
            region_pop = pd.merge(region_code_full[['시군구', '시도명', '시군구명']].drop_duplicates().reset_index(drop=True),
                                  pop[['행정구역별_읍면동', '시도명', '총인구_명', '시점']],
                                  how='right', left_on=['시도명', '시군구명'],
                                  right_on=['시도명', '행정구역별_읍면동']).drop(columns=['행정구역별_읍면동'])
            region_pop = region_pop.dropna(axis=0)
            region_pop = region_pop.astype({
                '시군구': 'int',
                '시도명': 'str',
                '시군구명': 'str',
                '총인구_명': 'int',
                '시점': 'int'
            })
            region_pop.to_csv(CSV_DIRECTORY + "region_pop_full.csv", sep=',', na_rep='NaN', index=False)
            # region_pop = pd.read_csv(CSV_DIRECTORY + "region_pop_full.csv", sep=',', encoding='utf-8', low_memory=False)
            # region_pop.drop_duplicates(keep='first').to_csv(CSV_DIRECTORY + "region_pop_full.csv", sep=',', na_rep='NaN',
            #                                                 index=False)
        elif pre_type == 'REG_REGION_CODE':
            with zipfile.ZipFile(CSV_DIRECTORY + "code.zip", 'r') as zf:
                zip_info = zf.infolist()
                dirname = CSV_DIRECTORY

                for member in zip_info:
                    member.filename = member.filename.encode('cp437').decode('euc-kr', 'ignore')
                    zf.extract(member, dirname)
                df = pd.read_csv(CSV_DIRECTORY + zip_info[0].filename, sep='\t', encoding='CP949')
                df.to_csv(CSV_DIRECTORY + "code.csv", sep=',', encoding='utf-8', index=False)
                os.remove(CSV_DIRECTORY + zip_info[0].filename)
            os.remove(CSV_DIRECTORY + "code.zip")


        elif pre_type == 'REGION_CODE_FULL':
            with zipfile.ZipFile(REGION_CODE_DIRECTORY + "REGION_CODE_FULL.zip", 'r') as zf:
                zip_info = zf.infolist()
                dirname = REGION_CODE_SUB_DIRECTORY

                for member in zip_info:
                    member.filename = member.filename.encode('cp437').decode('euc-kr', 'ignore')
                    zf.extract(member, dirname)

                filenames = os.listdir(dirname)
                filenames = [s for s in filenames if "지번_" in s]
                df = pd.DataFrame()
                for file in filenames:
                    temp = pd.read_csv(dirname + file, delimiter='|', encoding='cp949', low_memory=False,
                                       names={
                                           "관리번호": str,
                                           "일련번호": str,
                                           "법정동코드": str,
                                           "시도명": str,
                                           "시군구명": str,
                                           "법정읍면동명": str,
                                           "법정리명": str,
                                           "산여부": str,
                                           "지번본번(번지)": str,
                                           "지번부번(호)": str,
                                           "대표여부": str
                                       }
                                       )
                    df = pd.concat([df, temp], axis=0)
                df['시군구'] = df['법정동코드'].apply(lambda x: str(x)[0:5])
                header = ["관리번호", "일련번호", "법정동코드", "시도명", "시군구명", "법정읍면동명",
                          "법정리명", "산여부", "지번본번(번지)", "지번부번(호)", "대표여부", '시군구']
                df.to_csv(REGION_CODE_DIRECTORY + "REGION_CODE_FULL.csv", columns=header, sep='|', na_rep='NaN', index=False)
                shutil.rmtree(dirname)
        elif pre_type == 'TX':
            self.tx_data_pre()
        elif pre_type == 'TX_ALL_PRE':
            self.tx_data_all_pre()
        elif pre_type == 'PRICE':
            self.price_pre()
        elif pre_type == 'UNSOLD':
            self.unsold_pre()

    @staticmethod
    def additional_insight_detail(target):
        if target == '1':
            df = pd.read_csv(AC_CH_FINAL_DIRECTORY + "actual_tx_master.csv", sep='|', encoding='utf-8',
                             low_memory=False)
            df['거래월'] = df['거래일'].apply(lambda x: x.split('-')[0] + '-' + x.split('-')[1])
            df['전용평'] = df['전용면적'].apply(lambda x: int(x / 3.3))
            df['평단가'] = df.apply(lambda x: int(x.거래금액 / x.전용평), axis=1)
            df = df[['시도명', '시군구명', '법정동', '거래월', '전용면적', '거래금액', '전용평', '평단가']]
            df_month_tx = df.reset_index().groupby(['시도명', '시군구명', '법정동', '거래월'],
                                                   as_index=False)['평단가'].aggregate('mean')
            df_month_tx.to_csv(CSV_ADD_DIRECTORY + "month_tx.csv", sep='|', index=False)

            df_left = df.reset_index().groupby(['시도명', '시군구명', '거래월'], as_index=False)['평단가'].aggregate('mean')
            df_right = pd.read_csv(CSV_DIRECTORY + "population_pre.csv", sep='|', encoding='utf-8', low_memory=False)
            df_right = df_right[['행정구역별_읍면동', '총인구_명', '남자_명', '여자_명']]
            df = pd.merge(left=df_left, right=df_right, how='left', left_on=['시군구명'], right_on=['행정구역별_읍면동']
                          , suffixes=('', '_drop'))
            df = df[['시도명', '시군구명', '총인구_명', '남자_명', '여자_명', '거래월', '평단가']]
            df.to_csv(CSV_ADD_DIRECTORY + "pop_month_tx_1.csv", sep='|', index=False)
            df = pd.pivot_table(df,
                                index=['시도명', '시군구명', '총인구_명', '남자_명', '여자_명'],
                                values=['평단가'],
                                columns=['거래월']
                                ).reset_index()

            columns_list = []
            for i, v in enumerate(df.columns.tolist()):
                if i < 5:
                    columns_list.append(v[0])
                else:
                    columns_list.append(v[1])
            df.columns = columns_list
            df.to_csv(CSV_ADD_DIRECTORY + "pop_month_tx_2.csv", sep='|', index=False)
