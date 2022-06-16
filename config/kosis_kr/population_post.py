# 인구 데이터
import pandas as pd
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

POPULATION_POST_URL = 'https://kosis.kr/statHtml/downGrid.do'
POPULATION_POST_COOKIES = {
    'mb': 'N',
    'PCID': '16506134382599916704637',
    'newKOSIS2020StatisCtgrSettingCookie_2': 'A%7CB%7CC%7CD%7CE%7CF%7CG%7CH1%7CH2%7CI1%7CI2%7CJ1%7CJ2%7CK1%7CK2%7CL%7CM1%7CM2%7CN1%7CN2%7CO%7CP1%7CP2%7CQ%7CR%7CS1%7CS2%7CT%7CU%7CV',
    'pastQueryArr': '%uC9C0%uC5ED%uBCC4%20%uC778%uAD6C%uC218%7C%uC778%uAD6C%uC218%7C%uC9C0%uC5ED%uBCC4%20%uC784%uAE08',
    'JSESSIONID': 'fyxPPeu10btirFpiJd1Oar6kKtDA1YhyRac7KpHhMLLaWMBx7kzSm4gtoEuX2BK8.STAT_WAS2_servlet_engine5',
    'clientid': '060075621396',
    'KOSISMyViewStatisCookie': '101%7CDT_1IN1502%7C%uC778%uAD6C%2C%20%uAC00%uAD6C%20%uBC0F%20%uC8FC%uD0DD%20-%20%uC74D%uBA74%uB3D9%282015%2C2020%29%2C%20%uC2DC%uAD70%uAD6C%282016%7E2019%29%u2502101%7CDT_1IN1509%7C%uC131%2C%20%uC5F0%uB839%20%uBC0F%20%uC138%uB300%uAD6C%uC131%uBCC4%20%uC778%uAD6C%20-%20%uC2DC%uAD70%uAD6C%u2502460%7CTX_315_2009_H1009%7C%uD589%uC815%uAD6C%uC5ED%20%uD604%uD669%u2502460%7CTX_315_2009_H1001%7C%uB3C4%uC2DC%uC9C0%uC5ED%20%uC778%uAD6C%uD604%uD669%28%uC2DC%uAD70%uAD6C%29%u2502101%7CDT_1IN1507%7C%uC131%2C%20%uC5F0%uB839%20%uBC0F%20%uAC00%uAD6C%uC8FC%uC640%uC758%20%uAD00%uACC4%uBCC4%20%uC778%uAD6C%20-%20%uC2DC%uAD70%uAD6C%u2502101%7CDT_1IN1503%7C%uC5F0%uB839%20%uBC0F%20%uC131%uBCC4%20%uC778%uAD6C%20-%20%uC74D%uBA74%uB3D9%282015%2C2020%29%2C%20%uC2DC%uAD70%uAD6C%282016%7E2019%29%u2502322%7CDT_32202_B044%7C%uC2DC%uAD70%uAD6C%uBCC4%20%uAE09%uC5EC%uC9C0%uAE09%20%uD604%uD669%u2502118%7CDT_118N_MON049%7C%uD589%uC815%uAD6C%uC5ED%28%uC2DC%uB3C4%29/%20%uC0B0%uC5C5/%uADDC%uBAA8%uBCC4%20%uC784%uAE08%20%uBC0F%20%uADFC%uB85C%uC2DC%uAC04%28%uC0C1%uC6A9%uADFC%uB85C%uC790%2C%uC0C1%uC6A9%uADFC%uB85C%uC790%205%uC778%uC774%uC0C1%20%uC0AC%uC5C5%uCCB4%29%u2502365%7CTX_36504_A000%7C%uD3C9%uADE0%20%uC784%uAE08%20%uD604%uD669%u2502'
}
POPULATION_POST_HEADERS = {
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
currentyear_2010 = '2010'
currentyear_1925 = '1925'
index = sorted(list(set([x.strftime('%Y') for x in pd.date_range(start=currentyear_1925,
                                                                 end=currentyear_2010).to_list()])), reverse=True)
index = ','.join([x for x in index if int(x) % 5 == 0])

POPULATION_POST_DATA = [
    ('orgId', '101'),
    ('tblId', 'DT_1IN0001'),
    ('language', 'ko'),
    ('file', ''),
    ('analText', ''),
    ('scrId', ''),
    ('fieldList', f'[{{"targetId":"PRD","targetValue":"","prdValue":"F,{index},@"}},'
                  '{"targetId":"ITM_ID","targetValue":"T10","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"00","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"0A","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"0B","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"0C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"0D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"0E","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"11","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"24","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"25","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"61","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"62","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"63","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"64","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"65","prdValue":""},'
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
                  '{"targetId":"OV_L1_ID","targetValue":"2100C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"2100D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"2100E","prdValue":""},'
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
                  '{"targetId":"OV_L1_ID","targetValue":"21160","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"21800","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"2200C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"2200D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"2200E","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"22080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"2300C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"2300D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"2300E","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23090","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23100","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"23800","prdValue":""},'
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
                  '{"targetId":"OV_L1_ID","targetValue":"2600C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"2600D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"2600E","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"26310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3100A","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3100C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3100D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3100E","prdValue":""},'
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
                  '{"targetId":"OV_L1_ID","targetValue":"31056","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31057","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31090","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31091","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31092","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31100","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31101","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31102","prdValue":""},'
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
                  '{"targetId":"OV_L1_ID","targetValue":"31310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31340","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31360","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31390","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31400","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31410","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31420","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31430","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31800","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31810","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31820","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31830","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31840","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31850","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31860","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31870","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31880","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31890","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31900","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31910","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31920","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31930","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31940","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"31950","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3200A","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3200C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3200D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3200E","prdValue":""},'
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
                  '{"targetId":"OV_L1_ID","targetValue":"32800","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32810","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32820","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"32830","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3300A","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3300C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3300D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3300E","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33011","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33012","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33340","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33360","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33390","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33800","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33810","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"33820","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3400A","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3400C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3400D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3400E","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34011","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34012","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34340","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34350","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34360","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34370","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34380","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34390","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34400","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34410","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34800","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34810","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34820","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34830","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34840","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34850","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34860","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34870","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34880","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34881","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34882","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34883","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34884","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34885","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34886","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"34887","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3500A","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3500C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3500D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3500E","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35011","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35012","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35013","prdValue":""},'
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
                  '{"targetId":"OV_L1_ID","targetValue":"35800","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35810","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35820","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35830","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35840","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35850","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"35860","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3600A","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3600C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3600D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3600E","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36320","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36330","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36340","prdValue":""},'
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
                  '{"targetId":"OV_L1_ID","targetValue":"36800","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36810","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36820","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36830","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36840","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36850","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36860","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36861","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36862","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36863","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36864","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36865","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36866","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36867","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36868","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"36869","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3700A","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3700C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3700D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3700E","prdValue":""},'
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
                  '{"targetId":"OV_L1_ID","targetValue":"37800","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37810","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37820","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37830","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37840","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37850","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37860","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37870","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37880","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37890","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37900","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37910","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37911","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37912","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37913","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37914","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37915","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37916","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37918","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"37920","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3800A","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3800C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3800D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3800E","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38021","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38022","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38023","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38024","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38025","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38026","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38027","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38028","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38030","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38031","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38032","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38040","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38050","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38060","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38070","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38080","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38090","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38100","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38110","prdValue":""},'
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
                  '{"targetId":"OV_L1_ID","targetValue":"38410","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38800","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38810","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38820","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38830","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38840","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38850","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38860","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38870","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38880","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38890","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38900","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38960","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38110_2010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38111","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38112","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38113","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38114","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"38115","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3900A","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3900B","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3900C","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3900D","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"3900E","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39010","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39020","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39310","prdValue":""},'
                  '{"targetId":"OV_L1_ID","targetValue":"39320","prdValue":""},'
                  '{"targetId":"OV_L2_ID","targetValue":"00","prdValue":""}]'),
    ('colAxis', 'ITEM'),
    ('rowAxis', 'A,TIME'),
    ('isFirst', 'N'),
    ('contextPath', '/statHtml'),
    ('ordColIdx', ''),
    ('ordType', ''),
    ('logSeq', '231540516'),
    ('vwCd', 'MT_ZTITLE'),
    ('listId', 'A111'),
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
    ('defaulPeriodArr', f'{{"Y": [{currentyear_2010}]}}'),
    ('defaultClassArr', '[{"objVarId":"A","data":["00","0A","0B","0C","0D","0E","11","21","22","23","24","25","26","31","32","33","34","35","36","37","38","39","61","62","63","64","65"],"classType":1,"classLvlCnt":27},{"objVarId":"D","data":["00","05","10","15","20","25","30","35","40","45","50","55","60","65","70","75","77","80","84","85","90","95","96","97","98","99","9A"],"classType":1,"classLvlCnt":27}]'),
    ('existStblCmmtKor', 'Y'),
    ('existStblCmmtEng', 'Y'),
    ('classAllArr', '[{"objVarId":"A","ovlSn":"1"},{"objVarId":"D","ovlSn":"2"}]'),
    ('classSet', '[{"objVarId":"A","ovlSn":"1","visible":"true"},{"objVarId":"D","ovlSn":"2","visible":"true"}]'),
    ('selectAllFlag', 'N'),
    ('selectTimeRangeCnt', ''),
    ('periodStr', 'F'),
    ('funcPrdSe', 'F'),
    ('tblNm', '총조사인구 총괄(읍면동/성/연령별)'),
    ('tblEngNm', 'Summary of Census Population(by administrative district/sex/age)'),
    ('isChangedDataOpt', ''),
    ('itemMultiply', '469'),
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
    ('reqCellCnt', '8442'),
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
    ('endNum', '5000'),
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
    ('naviInfo', 'D'),
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

POPULATION_DOWN_POST_URL = 'https://kosis.kr/statHtml/downNormal.do'

POPULATION_DOWN_POST_COOKIES = {
    'mb': 'N',
    'PCID': '16506134382599916704637',
    'newKOSIS2020StatisCtgrSettingCookie_2': 'A%7CB%7CC%7CD%7CE%7CF%7CG%7CH1%7CH2%7CI1%7CI2%7CJ1%7CJ2%7CK1%7CK2%7CL%7CM1%7CM2%7CN1%7CN2%7CO%7CP1%7CP2%7CQ%7CR%7CS1%7CS2%7CT%7CU%7CV',
    'pastQueryArr': '%uC9C0%uC5ED%uBCC4%20%uC778%uAD6C%uC218%7C%uC778%uAD6C%uC218%7C%uC9C0%uC5ED%uBCC4%20%uC784%uAE08',
    'JSESSIONID': 'fyxPPeu10btirFpiJd1Oar6kKtDA1YhyRac7KpHhMLLaWMBx7kzSm4gtoEuX2BK8.STAT_WAS2_servlet_engine5',
    'clientid': '060075621396',
    'KOSISMyViewStatisCookie': '101%7CDT_1IN1502%7C%uC778%uAD6C%2C%20%uAC00%uAD6C%20%uBC0F%20%uC8FC%uD0DD%20-%20%uC74D%uBA74%uB3D9%282015%2C2020%29%2C%20%uC2DC%uAD70%uAD6C%282016%7E2019%29%u2502101%7CDT_1IN1509%7C%uC131%2C%20%uC5F0%uB839%20%uBC0F%20%uC138%uB300%uAD6C%uC131%uBCC4%20%uC778%uAD6C%20-%20%uC2DC%uAD70%uAD6C%u2502460%7CTX_315_2009_H1009%7C%uD589%uC815%uAD6C%uC5ED%20%uD604%uD669%u2502460%7CTX_315_2009_H1001%7C%uB3C4%uC2DC%uC9C0%uC5ED%20%uC778%uAD6C%uD604%uD669%28%uC2DC%uAD70%uAD6C%29%u2502101%7CDT_1IN1507%7C%uC131%2C%20%uC5F0%uB839%20%uBC0F%20%uAC00%uAD6C%uC8FC%uC640%uC758%20%uAD00%uACC4%uBCC4%20%uC778%uAD6C%20-%20%uC2DC%uAD70%uAD6C%u2502101%7CDT_1IN1503%7C%uC5F0%uB839%20%uBC0F%20%uC131%uBCC4%20%uC778%uAD6C%20-%20%uC74D%uBA74%uB3D9%282015%2C2020%29%2C%20%uC2DC%uAD70%uAD6C%282016%7E2019%29%u2502322%7CDT_32202_B044%7C%uC2DC%uAD70%uAD6C%uBCC4%20%uAE09%uC5EC%uC9C0%uAE09%20%uD604%uD669%u2502118%7CDT_118N_MON049%7C%uD589%uC815%uAD6C%uC5ED%28%uC2DC%uB3C4%29/%20%uC0B0%uC5C5/%uADDC%uBAA8%uBCC4%20%uC784%uAE08%20%uBC0F%20%uADFC%uB85C%uC2DC%uAC04%28%uC0C1%uC6A9%uADFC%uB85C%uC790%2C%uC0C1%uC6A9%uADFC%uB85C%uC790%205%uC778%uC774%uC0C1%20%uC0AC%uC5C5%uCCB4%29%u2502365%7CTX_36504_A000%7C%uD3C9%uADE0%20%uC784%uAE08%20%uD604%uD669%u2502',
}
POPULATION_DOWN_POST_HEADER = {
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


def make_population_post_down_data(csv):
    POPULATION_POST_DATA = []

    POPULATION_POST_DATA_1 = [
        ('orgId', '101'),
        ('tblId', 'DT_1IN0001'),
        ('language', 'ko')]
    POPULATION_POST_DATA_2 = [('file', csv)]

    POPULATION_POST_DATA_3 = [('analText', ''),
                         ('scrId', ''),
                         ('fieldList', f'[{{"targetId":"PRD","targetValue":"","prdValue":"F,{index},@"}},'
                                       '{"targetId":"ITM_ID","targetValue":"T10","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"00","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"0A","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"0B","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"0C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"0D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"0E","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"11","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"24","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"25","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"61","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"62","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"63","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"64","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"65","prdValue":""},'
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
                                       '{"targetId":"OV_L1_ID","targetValue":"2100C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"2100D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"2100E","prdValue":""},'
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
                                       '{"targetId":"OV_L1_ID","targetValue":"21160","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"21800","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"2200C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"2200D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"2200E","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"22080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"2300C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"2300D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"2300E","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23090","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23100","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"23800","prdValue":""},'
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
                                       '{"targetId":"OV_L1_ID","targetValue":"2600C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"2600D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"2600E","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"26310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3100A","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3100C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3100D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3100E","prdValue":""},'
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
                                       '{"targetId":"OV_L1_ID","targetValue":"31056","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31057","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31090","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31091","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31092","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31100","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31101","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31102","prdValue":""},'
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
                                       '{"targetId":"OV_L1_ID","targetValue":"31310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31340","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31360","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31390","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31400","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31410","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31420","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31430","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31800","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31810","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31820","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31830","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31840","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31850","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31860","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31870","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31880","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31890","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31900","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31910","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31920","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31930","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31940","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"31950","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3200A","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3200C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3200D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3200E","prdValue":""},'
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
                                       '{"targetId":"OV_L1_ID","targetValue":"32800","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32810","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32820","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"32830","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3300A","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3300C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3300D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3300E","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33011","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33012","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33340","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33360","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33390","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33800","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33810","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"33820","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3400A","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3400C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3400D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3400E","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34011","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34012","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34340","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34350","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34360","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34370","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34380","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34390","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34400","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34410","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34800","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34810","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34820","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34830","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34840","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34850","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34860","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34870","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34880","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34881","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34882","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34883","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34884","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34885","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34886","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"34887","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3500A","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3500C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3500D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3500E","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35011","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35012","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35013","prdValue":""},'
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
                                       '{"targetId":"OV_L1_ID","targetValue":"35800","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35810","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35820","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35830","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35840","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35850","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"35860","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3600A","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3600C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3600D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3600E","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36320","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36330","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36340","prdValue":""},'
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
                                       '{"targetId":"OV_L1_ID","targetValue":"36800","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36810","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36820","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36830","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36840","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36850","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36860","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36861","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36862","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36863","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36864","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36865","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36866","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36867","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36868","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"36869","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3700A","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3700C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3700D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3700E","prdValue":""},'
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
                                       '{"targetId":"OV_L1_ID","targetValue":"37800","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37810","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37820","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37830","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37840","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37850","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37860","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37870","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37880","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37890","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37900","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37910","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37911","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37912","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37913","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37914","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37915","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37916","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37918","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"37920","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3800A","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3800C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3800D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3800E","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38021","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38022","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38023","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38024","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38025","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38026","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38027","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38028","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38030","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38031","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38032","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38040","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38050","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38060","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38070","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38080","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38090","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38100","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38110","prdValue":""},'
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
                                       '{"targetId":"OV_L1_ID","targetValue":"38410","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38800","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38810","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38820","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38830","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38840","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38850","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38860","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38870","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38880","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38890","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38900","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38960","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38110_2010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38111","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38112","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38113","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38114","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"38115","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3900A","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3900B","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3900C","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3900D","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"3900E","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39010","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39020","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39310","prdValue":""},'
                                       '{"targetId":"OV_L1_ID","targetValue":"39320","prdValue":""},'
                                       '{"targetId":"OV_L2_ID","targetValue":"00","prdValue":""}]'),
                         ('colAxis', 'ITEM'),
                         ('rowAxis', 'A,TIME'),
                         ('isFirst', 'N'),
                         ('contextPath', '/statHtml'),
                         ('ordColIdx', ''),
                         ('ordType', ''),
                         ('logSeq', '131540516'),
                         ('vwCd', 'MT_ZTITLE'),
                         ('listId', 'A111'),
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
                         ('analWithCHGRATE', ''),
                         ('defaulPeriodArr', f'{{"Y":[{currentyear_2010}]}}'),
                         ('defaultClassArr', '[{"objVarId":"A","data":["00","0A","0B","0C","0D","0E","11","21","22","23","24","25","26","31","32","33","34","35","36","37","38","39","61","62","63","64","65"],"classType":1,"classLvlCnt":27},{"objVarId":"D","data":["00","05","10","15","20","25","30","35","40","45","50","55","60","65","70","75","77","80","84","85","90","95","96","97","98","99","9A"],"classType":1,"classLvlCnt":27}]'),
                         ('existStblCmmtKor', 'Y'),
                         ('existStblCmmtEng', 'Y'),
                         ('classAllArr', '[{"objVarId":"A","ovlSn":"1"},{"objVarId":"D","ovlSn":"2"}]'),
                         ('classSet', '[{"objVarId":"A","ovlSn":"1","visible":"true"},{"objVarId":"D","ovlSn":"2","visible":"true"}]'),
                         ('selectAllFlag', 'N'),
                         ('selectTimeRangeCnt', ''),
                         ('periodStr', 'F'),
                         ('funcPrdSe', 'F'),
                         ('tblNm', '총조사인구 총괄(읍면동/성/연령별)'),
                         ('tblEngNm', 'Summary of Census Population(by administrative district/sex/age)'),
                         ('isChangedDataOpt', ''),
                         ('itemMultiply', '469'),
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
                         ('reqCellCnt', '8442'),
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
                         ('endNum', '5000'),
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
                         ('naviInfo', 'D'),
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
    POPULATION_POST_DATA.extend(POPULATION_POST_DATA_1)
    POPULATION_POST_DATA.extend(POPULATION_POST_DATA_2)
    POPULATION_POST_DATA.extend(POPULATION_POST_DATA_3)
    return POPULATION_POST_DATA
