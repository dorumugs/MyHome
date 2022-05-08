import pandas as pd
import requests
import bs4


class CoreExtract(object):
    def __init__(self, extends_sqlalchemy=None):
        self.extends_sqlalchemy = extends_sqlalchemy

    @staticmethod
    def df_for_date(rows):
        row_list = []
        name_list = []
        column_list = []
        rows_len = len(rows)
        for i in range(0, rows_len):
            columns = rows[i].find_all()

            columns_len = len(columns)
            for j in range(0, columns_len):
                if i == 0:
                    name_list.append(columns[j].name)
                eachColumn = columns[j].text
                column_list.append(eachColumn)
            row_list.append(column_list)
            column_list = []

        df = pd.DataFrame(row_list, columns=name_list)
        return df

    def request_api(self, tx_columns, url, service_key, codes, date):
        df = pd.DataFrame(columns=tx_columns)
        for code in codes:
            payload = "serviceKey=" + service_key + "&" \
                      + "LAWD_CD=" + code + "&" \
                      + "DEAL_YMD=" + date
            res = requests.get(url + payload).text
            xmlobj = bs4.BeautifulSoup(res, 'lxml-xml')
            rows = xmlobj.findAll('item')
            each_df = self.df_for_date(rows)
            if each_df.shape[0] != 0:
                each_df = each_df[tx_columns]
                df = pd.concat([df, each_df], axis=0)
        return df