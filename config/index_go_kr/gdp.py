import pandas as pd
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


currentTimeDate = datetime.now() - relativedelta(months=6)
current = currentTimeDate.strftime('%Y%m')
GDP_URL = f'http://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=273601&idx_cd=2736&freq=Q&period=196001:{current}'
GDP_COOKIES = {
    'chrCookie1651395967026': 'cookieValue',
    'idxCd_2736': '2736',
    'clientid': '000038765407',
}
GDP_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'www.index.go.kr',
    'Referer': 'http://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=2736&stts_cd=273601&freq=Q',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}
GDP_DATA = {
    'stts_cd': '273601',
    'idx_cd': '2736',
    'freq': 'Q',
    'period': f'196001:{current}',
}
