# 인구 데이터
import pandas as pd
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

POPULATION_URL = 'https://kosis.kr/statHtml/downGrid.do'
POPULATION_COOKIES = {
    'mb': 'N',
    'PCID': '16506134382599916704637',
    'newKOSIS2020StatisCtgrSettingCookie_2': 'A%7CB%7CC%7CD%7CE%7CF%7CG%7CH1%7CH2%7CI1%7CI2%7CJ1%7CJ2%7CK1%7CK2%7CL%7CM1%7CM2%7CN1%7CN2%7CO%7CP1%7CP2%7CQ%7CR%7CS1%7CS2%7CT%7CU%7CV',
    'pastQueryArr': '%uC9C0%uC5ED%uBCC4%20%uC778%uAD6C%uC218%7C%uC778%uAD6C%uC218%7C%uC9C0%uC5ED%uBCC4%20%uC784%uAE08',
    'JSESSIONID': 'fyxPPeu10btirFpiJd1Oar6kKtDA1YhyRac7KpHhMLLaWMBx7kzSm4gtoEuX2BK8.STAT_WAS2_servlet_engine5',
    'clientid': '060075621396',
    'KOSISMyViewStatisCookie': '101%7CDT_1IN1502%7C%uC778%uAD6C%2C%20%uAC00%uAD6C%20%uBC0F%20%uC8FC%uD0DD%20-%20%uC74D%uBA74%uB3D9%282015%2C2020%29%2C%20%uC2DC%uAD70%uAD6C%282016%7E2019%29%u2502101%7CDT_1IN1509%7C%uC131%2C%20%uC5F0%uB839%20%uBC0F%20%uC138%uB300%uAD6C%uC131%uBCC4%20%uC778%uAD6C%20-%20%uC2DC%uAD70%uAD6C%u2502460%7CTX_315_2009_H1009%7C%uD589%uC815%uAD6C%uC5ED%20%uD604%uD669%u2502460%7CTX_315_2009_H1001%7C%uB3C4%uC2DC%uC9C0%uC5ED%20%uC778%uAD6C%uD604%uD669%28%uC2DC%uAD70%uAD6C%29%u2502101%7CDT_1IN1507%7C%uC131%2C%20%uC5F0%uB839%20%uBC0F%20%uAC00%uAD6C%uC8FC%uC640%uC758%20%uAD00%uACC4%uBCC4%20%uC778%uAD6C%20-%20%uC2DC%uAD70%uAD6C%u2502101%7CDT_1IN1503%7C%uC5F0%uB839%20%uBC0F%20%uC131%uBCC4%20%uC778%uAD6C%20-%20%uC74D%uBA74%uB3D9%282015%2C2020%29%2C%20%uC2DC%uAD70%uAD6C%282016%7E2019%29%u2502322%7CDT_32202_B044%7C%uC2DC%uAD70%uAD6C%uBCC4%20%uAE09%uC5EC%uC9C0%uAE09%20%uD604%uD669%u2502118%7CDT_118N_MON049%7C%uD589%uC815%uAD6C%uC5ED%28%uC2DC%uB3C4%29/%20%uC0B0%uC5C5/%uADDC%uBAA8%uBCC4%20%uC784%uAE08%20%uBC0F%20%uADFC%uB85C%uC2DC%uAC04%28%uC0C1%uC6A9%uADFC%uB85C%uC790%2C%uC0C1%uC6A9%uADFC%uB85C%uC790%205%uC778%uC774%uC0C1%20%uC0AC%uC5C5%uCCB4%29%u2502365%7CTX_36504_A000%7C%uD3C9%uADE0%20%uC784%uAE08%20%uD604%uD669%u2502'
}
POPULATION_HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '40126',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'kosis.kr',
    'Origin': 'https://kosis.kr',
    'Referer': 'https://kosis.kr/statHtml/statHtmlContent.do?orgId=101&tblId=DT_1IN1502&pub=2&conn_path=ZA&list_id=A11_2015_1_10_10&vw_cd=MT_ZTITLE&language=ko&dbUser=NSI.&itm_id=',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
currentTimeDate = datetime.now() - relativedelta(years=2)
currentyear = currentTimeDate.strftime('%Y')
currentyear_5 = str(int(currentyear) - 5)
index = ','.join(sorted(list(set([x.strftime('%Y') for x in pd.date_range(start=currentyear_5,
                                                                          end=currentyear).to_list()])), reverse=True))

POPULATION_DATA = [
    ('orgId', '101'),
    ('tblId', 'DT_1IN1502'),
    ('language', 'ko'),
    ('file', ''),
    ('analText', ''),
    ('scrId', ''),
    ('fieldList', f'[{{"targetId":"PRD","targetValue":"","prdValue":"Y,{index},@"}},'
                  '{"targetId":"ITM_ID","targetValue":"T100","prdValue":""},'
                  '{"targetId":"ITM_ID","targetValue":"T200","prdValue":""},'
                  '{"targetId":"ITM_ID","targetValue":"T312","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"00","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"04","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"05","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"03","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"24","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"25","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"29","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11090","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11100","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11110","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11120","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11130","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11140","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11150","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11160","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11170","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11180","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11190","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11200","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11210","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11220","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11230","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11240","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11250","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21090","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21100","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21110","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21120","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21130","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21140","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21150","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23090","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"24010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"24020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"24030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"24040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"24050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"25010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"25020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"25030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"25040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"25050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"29004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"29005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"29003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"29010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31011","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31012","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31013","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31014","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31021","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31022","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31023","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31041","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31042","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31051","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31052","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31053","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31090","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31091","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31092","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31100","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31101","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31103","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31104","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31110","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31120","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31130","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31140","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31150","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31160","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31170","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31180","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31190","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31191","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31192","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31193","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31200","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31210","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31220","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31230","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31240","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31250","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31260","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31270","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31280","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32340","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32360","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32390","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32400","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32410","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33041","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33042","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33043","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33044","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33340","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33360","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33390","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34011","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34012","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34340","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34360","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35011","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35012","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35340","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35360","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36360","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36390","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36400","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36410","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36420","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36430","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36440","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36450","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36460","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36470","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36480","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37011","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37012","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37090","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37100","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37340","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37360","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37390","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37400","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37410","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37420","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37430","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38090","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38100","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38110","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38111","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38112","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38113","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38114","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38115","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38340","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38360","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38390","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38400","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39004","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39005","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39003","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39020","prdValue":""}]'),
    ('colAxis', 'ITEM'),
    ('rowAxis', 'A,TIME'),
    ('isFirst', 'N'),
    ('contextPath', '/statHtml'),
    ('ordColIdx', ''),
    ('ordType', ''),
    ('logSeq', '131672596'),
    ('vwCd', 'MT_ZTITLE'),
    ('listId', 'A11_2015_1_10_10'),
    ('connPath', 'ZA'),
    ('statId', '1962001'),
    ('pub', '2'),
    ('pubLog', '4'),
    ('viewKind', '2'),
    ('viewSubKind', '2_3'),
    ('doAnal', 'N'),
    ('analType', ''),
    ('analCmpr', ''),
    ('analTime', ''),
    ('analCombo', ''),
    ('originData', ''),
    ('analClass', ''),
    ('analItem', ''),
    ('obj_var_id', ''),
    ('itm_id', ''),
    ('mode', ''),
    ('dataOpt', 'ko'),
    ('noSelect', ''),
    ('view', 'csv'),
    ('analWithCHGRATE', ''),
    ('defaulPeriodArr', f'{{"Y": [{currentyear}]}}'),
    ('defaultClassArr', '[{"objVarId":"A","data":["00","04","05","03","11","21","22","23","24","25","26","29","31","32","33","34","35","36","37","38","39"],"classType":1,"classLvlCnt":21},{"objVarId":"A","data":["11010","11020","11030","11040","11050","11060","11070","11080","11090","11100","11110","11120","11130","11140","11150","11160","11170","11180","11190","11200","11210","11220","11230","11240","11250","21004","21005","21003","21010","21020","21030","21040","21050","21060","21070","21080","21090","21100","21110","21120","21130","21140","21150","21310","22004","22005","22003","22010","22020","22030","22040","22050","22060","22070","22310","23004","23005","23003","23010","23020","23030","23040","23050","23060","23070","23080","23090","23310","23320","24010","24020","24030","24040","24050","25010","25020","25030","25040","25050","26004","26005","26003","26010","26020","26030","26040","26310","29004","29005","29003","29010","31004","31005","31003","31010","31011","31012","31013","31014","31020","31021","31022","31023","31030","31040","31041","31042","31050","31051","31052","31053","31060","31070","31080","31090","31091","31092","31100","31101","31103","31104","31110","31120","31130","31140","31150","31160","31170","31180","31190","31191","31192","31193","31200","31210","31220","31230","31240","31250","31260","31270","31280","31350","31370","31380","32004","32005","32003","32010","32020","32030","32040","32050","32060","32070","32310","32320","32330","32340","32350","32360","32370","32380","32390","32400","32410","33004","33005","33003","33020","33030","33040","33041","33042","33043","33044","33320","33330","33340","33350","33360","33370","33380","33390","34004","34005","34003","34010","34011","34012","34020","34030","34040","34050","34060","34070","34080","34310","34330","34340","34350","34360","34370","34380","35004","35005","35003","35010","35011","35012","35020","35030","35040","35050","35060","35310","35320","35330","35340","35350","35360","35370","35380","36004","36005","36003","36010","36020","36030","36040","36060","36310","36320","36330","36350","36360","36370","36380","36390","36400","36410","36420","36430","36440","36450","36460","36470","36480","37004","37005","37003","37010","37011","37012","37020","37030","37040","37050","37060","37070","37080","37090","37100","37310","37320","37330","37340","37350","37360","37370","37380","37390","37400","37410","37420","37430","38004","38005","38003","38030","38050","38060","38070","38080","38090","38100","38110","38111","38112","38113","38114","38115","38310","38320","38330","38340","38350","38360","38370","38380","38390","38400","39004","39005","39003","39010","39020"],"classType":2,"classLvlCnt":307}]'),
    ('existStblCmmtKor', 'Y'),
    ('existStblCmmtEng', 'Y'),
    ('classAllArr', '[{"objVarId":"A","ovlSn":"1"}]'),
    ('classSet', '[{"objVarId":"A","ovlSn":"1","visible":"true"}]'),
    ('selectAllFlag', 'N'),
    ('selectTimeRangeCnt', ''),
    ('periodStr', 'Y'),
    ('funcPrdSe', 'Y'),
    ('tblNm', '인구, 가구 및 주택 - 읍면동(2015,2020), 시군구(2016~2019)'),
    ('tblEngNm', 'Population, Households and Housing Units'),
    ('isChangedDataOpt', ''),
    ('itemMultiply', '984'),
    ('dimCo', ''),
    ('dbUser', 'NSI.'),
    ('usePivot', 'N'),
    ('isChangedTableType', 'N'),
    ('isChangedPeriodCo', 'N'),
    ('isChangedPrdSort', 'N'),
    ('p_chkStatus', ''),
    ('p_objVarId', ''),
    ('p_lvl', ''),
    ('p_logicFlag', ''),
    ('p_classAllChkYn', 'N'),
    ('p_classAllSelectYn', 'N'),
    ('useAddFuncLog', ''),
    ('chargerLvl', ''),
    ('st', ''),
    ('new_win', ''),
    ('first_open', ''),
    ('debug', ''),
    ('maxCellOver', 'Y'),
    ('reqCellCnt', '5904'),
    ('inheritYn', 'N'),
    ('originOrgId', ''),
    ('originTblId', ''),
    ('pubSeType', ''),
    ('relChkOrgId', ''),
    ('relChkTblId', ''),
    ('highLightStr', ''),
    ('markType', ''),
    ('docId', ''),
    ('itmNm', ''),
    ('cmmtChk', 'Y'),
    ('labelOriginData', '원자료 함께 보기'),
    ('diviSearchYn', ''),
    ('orderStr', 'OV_L1_ID,TIME,CHAR_ITM_ID'),
    ('startNum', '1'),
    ('endNum', '5001'),
    ('colClsAt', 'N'),
    ('analyzable', 'true'),
    ('expDash', 'Y'),
    ('downGridFileType', 'csv'),
    ('downSort', 'asc'),
    ('pointType', 'screen'),
    ('downLargeFileType', 'excel'),
    ('downLargeExprType', '1'),
    ('downLargeSort', 'asc'),
    ('prdSortPop', 'asc'),
    ('naviInfo', 'tabItemText'),
    ('naviInfo', 'A'),
    ('naviInfo', 'tabTimeText'),
    ('assayLeft', 'none'),
    ('assayselectType', 'none'),
    ('selectType', ''),
    ('assayRight', 'none'),
    ('tableType', 'default'),
    ('dataOpt2', 'ko'),
    ('periodCo', ''),
    ('prdSort', 'asc'),
    ('compValue', ''),
    ('compValue01', ''),
    ('compValue02', ''),
]

POPULATION_DOWN_URL = 'https://kosis.kr/statHtml/downNormal.do'
POPULATION_DOWN_COOKIES = {
    'mb': 'N',
    'PCID': '16506134382599916704637',
    'newKOSIS2020StatisCtgrSettingCookie_2': 'A%7CB%7CC%7CD%7CE%7CF%7CG%7CH1%7CH2%7CI1%7CI2%7CJ1%7CJ2%7CK1%7CK2%7CL%7CM1%7CM2%7CN1%7CN2%7CO%7CP1%7CP2%7CQ%7CR%7CS1%7CS2%7CT%7CU%7CV',
    'pastQueryArr': '%uC9C0%uC5ED%uBCC4%20%uC778%uAD6C%uC218%7C%uC778%uAD6C%uC218%7C%uC9C0%uC5ED%uBCC4%20%uC784%uAE08',
    'JSESSIONID': 'fyxPPeu10btirFpiJd1Oar6kKtDA1YhyRac7KpHhMLLaWMBx7kzSm4gtoEuX2BK8.STAT_WAS2_servlet_engine5',
    'clientid': '060075621396',
    'KOSISMyViewStatisCookie': '101%7CDT_1IN1502%7C%uC778%uAD6C%2C%20%uAC00%uAD6C%20%uBC0F%20%uC8FC%uD0DD%20-%20%uC74D%uBA74%uB3D9%282015%2C2020%29%2C%20%uC2DC%uAD70%uAD6C%282016%7E2019%29%u2502101%7CDT_1IN1509%7C%uC131%2C%20%uC5F0%uB839%20%uBC0F%20%uC138%uB300%uAD6C%uC131%uBCC4%20%uC778%uAD6C%20-%20%uC2DC%uAD70%uAD6C%u2502460%7CTX_315_2009_H1009%7C%uD589%uC815%uAD6C%uC5ED%20%uD604%uD669%u2502460%7CTX_315_2009_H1001%7C%uB3C4%uC2DC%uC9C0%uC5ED%20%uC778%uAD6C%uD604%uD669%28%uC2DC%uAD70%uAD6C%29%u2502101%7CDT_1IN1507%7C%uC131%2C%20%uC5F0%uB839%20%uBC0F%20%uAC00%uAD6C%uC8FC%uC640%uC758%20%uAD00%uACC4%uBCC4%20%uC778%uAD6C%20-%20%uC2DC%uAD70%uAD6C%u2502101%7CDT_1IN1503%7C%uC5F0%uB839%20%uBC0F%20%uC131%uBCC4%20%uC778%uAD6C%20-%20%uC74D%uBA74%uB3D9%282015%2C2020%29%2C%20%uC2DC%uAD70%uAD6C%282016%7E2019%29%u2502322%7CDT_32202_B044%7C%uC2DC%uAD70%uAD6C%uBCC4%20%uAE09%uC5EC%uC9C0%uAE09%20%uD604%uD669%u2502118%7CDT_118N_MON049%7C%uD589%uC815%uAD6C%uC5ED%28%uC2DC%uB3C4%29/%20%uC0B0%uC5C5/%uADDC%uBAA8%uBCC4%20%uC784%uAE08%20%uBC0F%20%uADFC%uB85C%uC2DC%uAC04%28%uC0C1%uC6A9%uADFC%uB85C%uC790%2C%uC0C1%uC6A9%uADFC%uB85C%uC790%205%uC778%uC774%uC0C1%20%uC0AC%uC5C5%uCCB4%29%u2502365%7CTX_36504_A000%7C%uD3C9%uADE0%20%uC784%uAE08%20%uD604%uD669%u2502',
}
POPULATION_DOWN_HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '40298',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'kosis.kr',
    'Origin': 'https://kosis.kr',
    'Referer': 'https://kosis.kr/statHtml/statHtmlContent.do?orgId=101&tblId=DT_1IN1502&pub=2&conn_path=ZA&list_id=A11_2015_1_10_10&vw_cd=MT_ZTITLE&language=ko&dbUser=NSI.&itm_id=',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}


def make_population_down_data(csv):
    POPULATION_DATA = []

    POPULATION_DATA_1 = [
        ('orgId', '101'),
        ('tblId', 'DT_1IN1502'),
        ('language', 'ko')]
    POPULATION_DATA_2 = [('file', csv)]
    currentTimeDate = datetime.now() - relativedelta(years=2)
    currentyear = currentTimeDate.strftime('%Y')
    POPULATION_DATA_3 = [('analText', ''),
                         ('scrId', ''),
                         ('fieldList', f'[{{"targetId":"PRD","targetValue":"","prdValue":"Y,{index},@"}},'
                                       '{"targetId":"ITM_ID","targetValue":"T100","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T200","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T312","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"00","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"04","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"05","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"03","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"24","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"25","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"29","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11090","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11100","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11110","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11120","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11130","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11140","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11150","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11160","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11170","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11180","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11190","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11200","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11210","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11220","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11230","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11240","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11250","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21090","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21100","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21110","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21120","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21130","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21140","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21150","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23090","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"24010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"24020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"24030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"24040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"24050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"25010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"25020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"25030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"25040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"25050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"29004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"29005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"29003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"29010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31011","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31012","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31013","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31014","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31021","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31022","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31023","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31041","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31042","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31051","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31052","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31053","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31090","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31091","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31092","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31100","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31101","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31103","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31104","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31110","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31120","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31130","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31140","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31150","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31160","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31170","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31180","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31190","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31191","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31192","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31193","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31200","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31210","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31220","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31230","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31240","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31250","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31260","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31270","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31280","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32340","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32360","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32390","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32400","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32410","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33041","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33042","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33043","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33044","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33340","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33360","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33390","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34011","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34012","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34340","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34360","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35011","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35012","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35340","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35360","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36360","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36390","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36400","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36410","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36420","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36430","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36440","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36450","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36460","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36470","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36480","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37011","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37012","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37090","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37100","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37340","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37360","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37390","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37400","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37410","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37420","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37430","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38090","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38100","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38110","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38111","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38112","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38113","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38114","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38115","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38340","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38360","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38390","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38400","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39004","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39005","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39003","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39020","prdValue":""}]'),
                         ('colAxis', 'ITEM'),
                         ('rowAxis', 'A,TIME'),
                         ('isFirst', 'N'),
                         ('contextPath', '/statHtml'),
                         ('ordColIdx', ''),
                         ('ordType', ''),
                         ('logSeq', '131672596'),
                         ('vwCd', 'MT_ZTITLE'),
                         ('listId', 'A11_2015_1_10_10'),
                         ('connPath', 'ZA'),
                         ('statId', '1962001'),
                         ('pub', '2'),
                         ('pubLog', '4'),
                         ('viewKind', '2'),
                         ('viewSubKind', ''),
                         ('doAnal', 'N'),
                         ('analType', ''),
                         ('analCmpr', ''),
                         ('analTime', ''),
                         ('analCombo', ''),
                         ('originData', ''),
                         ('analClass', ''),
                         ('analItem', ''),
                         ('obj_var_id', ''),
                         ('itm_id', ''),
                         ('mode', ''),
                         ('dataOpt', 'ko'),
                         ('noSelect', ''),
                         ('view', 'csv'),
                         ('mobChk', 'false'),
                         ('analWithCHGRATE', ''),
                         ('defaulPeriodArr', f'{{"Y":[{currentyear}]}}'),
                         ('defaultClassArr', '[{"objVarId":"A","data":["00","04","05","03","11","21","22","23","24","25","26","29","31","32","33","34","35","36","37","38","39"],"classType":1,"classLvlCnt":21},{"objVarId":"A","data":["11010","11020","11030","11040","11050","11060","11070","11080","11090","11100","11110","11120","11130","11140","11150","11160","11170","11180","11190","11200","11210","11220","11230","11240","11250","21004","21005","21003","21010","21020","21030","21040","21050","21060","21070","21080","21090","21100","21110","21120","21130","21140","21150","21310","22004","22005","22003","22010","22020","22030","22040","22050","22060","22070","22310","23004","23005","23003","23010","23020","23030","23040","23050","23060","23070","23080","23090","23310","23320","24010","24020","24030","24040","24050","25010","25020","25030","25040","25050","26004","26005","26003","26010","26020","26030","26040","26310","29004","29005","29003","29010","31004","31005","31003","31010","31011","31012","31013","31014","31020","31021","31022","31023","31030","31040","31041","31042","31050","31051","31052","31053","31060","31070","31080","31090","31091","31092","31100","31101","31103","31104","31110","31120","31130","31140","31150","31160","31170","31180","31190","31191","31192","31193","31200","31210","31220","31230","31240","31250","31260","31270","31280","31350","31370","31380","32004","32005","32003","32010","32020","32030","32040","32050","32060","32070","32310","32320","32330","32340","32350","32360","32370","32380","32390","32400","32410","33004","33005","33003","33020","33030","33040","33041","33042","33043","33044","33320","33330","33340","33350","33360","33370","33380","33390","34004","34005","34003","34010","34011","34012","34020","34030","34040","34050","34060","34070","34080","34310","34330","34340","34350","34360","34370","34380","35004","35005","35003","35010","35011","35012","35020","35030","35040","35050","35060","35310","35320","35330","35340","35350","35360","35370","35380","36004","36005","36003","36010","36020","36030","36040","36060","36310","36320","36330","36350","36360","36370","36380","36390","36400","36410","36420","36430","36440","36450","36460","36470","36480","37004","37005","37003","37010","37011","37012","37020","37030","37040","37050","37060","37070","37080","37090","37100","37310","37320","37330","37340","37350","37360","37370","37380","37390","37400","37410","37420","37430","38004","38005","38003","38030","38050","38060","38070","38080","38090","38100","38110","38111","38112","38113","38114","38115","38310","38320","38330","38340","38350","38360","38370","38380","38390","38400","39004","39005","39003","39010","39020"],"classType":2,"classLvlCnt":307}]'),
                         ('existStblCmmtKor', 'Y'),
                         ('existStblCmmtEng', 'Y'),
                         ('classAllArr', '[{"objVarId":"A","ovlSn":"1"}]'),
                         ('classSet', '[{"objVarId":"A","ovlSn":"1","visible":"true"}]'),
                         ('selectAllFlag', 'N'),
                         ('selectTimeRangeCnt', ''),
                         ('periodStr', 'Y'),
                         ('funcPrdSe', 'Y'),
                         ('tblNm', '인구, 가구 및 주택 - 읍면동(2015,2020), 시군구(2016~2019)'),
                         ('tblEngNm', 'Population, Households and Housing Units'),
                         ('isChangedDataOpt', ''),
                         ('itemMultiply', '984'),
                         ('dimCo', ''),
                         ('dbUser', 'NSI.'),
                         ('usePivot', 'N'),
                         ('isChangedTableType', 'N'),
                         ('isChangedPeriodCo', 'N'),
                         ('isChangedPrdSort', 'N'),
                         ('p_chkStatus', ''),
                         ('p_objVarId', ''),
                         ('p_lvl', ''),
                         ('p_logicFlag', ''),
                         ('p_classAllChkYn', 'N'),
                         ('p_classAllSelectYn', 'N'),
                         ('useAddFuncLog', ''),
                         ('chargerLvl', ''),
                         ('st', ''),
                         ('new_win', ''),
                         ('first_open', ''),
                         ('debug', ''),
                         ('maxCellOver', 'Y'),
                         ('reqCellCnt', '5904'),
                         ('inheritYn', 'N'),
                         ('originOrgId', ''),
                         ('originTblId', ''),
                         ('pubSeType', ''),
                         ('relChkOrgId', ''),
                         ('relChkTblId', ''),
                         ('highLightStr', ''),
                         ('markType', ''),
                         ('docId', ''),
                         ('itmNm', ''),
                         ('cmmtChk', 'Y'),
                         ('labelOriginData', '원자료 함께 보기'),
                         ('diviSearchYn', ''),
                         ('orderStr', 'OV_L1_ID,TIME,CHAR_ITM_ID'),
                         ('startNum', '1'),
                         ('endNum', '5001'),
                         ('colClsAt', 'N'),
                         ('analyzable', 'true'),
                         ('expDash', 'Y'),
                         ('downGridFileType', 'csv'),
                         ('downSort', 'asc'),
                         ('pointType', 'screen'),
                         ('downLargeFileType', 'excel'),
                         ('downLargeExprType', '1'),
                         ('downLargeSort', 'asc'),
                         ('prdSortPop', 'asc'),
                         ('naviInfo', 'tabItemText'),
                         ('naviInfo', 'A'),
                         ('naviInfo', 'tabTimeText'),
                         ('assayLeft', 'none'),
                         ('assayselectType', 'none'),
                         ('selectType', ''),
                         ('assayRight', 'none'),
                         ('tableType', 'default'),
                         ('dataOpt2', 'ko'),
                         ('periodCo', ''),
                         ('prdSort', 'asc'),
                         ('compValue', ''),
                         ('compValue01', ''),
                         ('compValue02', ''),
                         ]
    POPULATION_DATA.extend(POPULATION_DATA_1)
    POPULATION_DATA.extend(POPULATION_DATA_2)
    POPULATION_DATA.extend(POPULATION_DATA_3)
    return POPULATION_DATA
