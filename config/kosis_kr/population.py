# 인구 데이터
import pandas as pd
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

POPULATION_URL = 'https://kosis.kr/statHtml/downGrid.do'
POPULATION_COOKIES = {
    'newKOSIS2020StatisCtgrSettingCookie_2': 'A%7CB%7CC%7CD%7CE%7CF%7CG%7CH1%7CH2%7CI1%7CI2%7CJ1%7CJ2%7CK1%7CK2%7CL%7CM1%7CM2%7CN1%7CN2%7CO%7CP1%7CP2%7CQ%7CR%7CS1%7CS2%7CT%7CU%7CV',
    'mb': 'N',
    'PCID': '16281139835577069142434',
    'KOSISMyViewStatisCookie': '101%7CINH_1B26001_A021%7C%uC21C%uC774%uB3D9%uC778%uAD6C%28%uC2DC%uB3C4/%uC2DC/%uAD70/%uAD6C%29%u2502101%7CDT_1IN1503%7C%uC5F0%uB839%20%uBC0F%20%uC131%uBCC4%20%uC778%uAD6C%20-%20%uC74D%uBA74%uB3D9%282015%2C2020%29%2C%20%uC2DC%uAD70%uAD6C%282016%7E2019%29%u2502101%7CDT_1B04005N%7C%uD589%uC815%uAD6C%uC5ED%28%uC74D%uBA74%uB3D9%29%uBCC4/5%uC138%uBCC4%20%uC8FC%uBBFC%uB4F1%uB85D%uC778%uAD6C%282011%uB144%7E%29%u2502101%7CDT_1IN1502%7C%uC778%uAD6C%2C%20%uAC00%uAD6C%20%uBC0F%20%uC8FC%uD0DD%20-%20%uC74D%uBA74%uB3D9%282015%2C2020%29%2C%20%uC2DC%uAD70%uAD6C%282016%7E2019%29%u2502',
    'JSESSIONID': 'WZ8sjid6swFpyAAe354MlZOY7kKa1LbJsmRMFVKj51fFQcy0p76moV26VcLTl1Z1.STAT_WAS2_servlet_engine5',
}
POPULATION_HEADERS = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://kosis.kr',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://kosis.kr/statHtml/statHtml.do?mode=tab&orgId=101&tblId=DT_1IN1502&vw_cd=MT_ZTITLE&list_id=A11_2015_1_10_10&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_ZTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do%27',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
}
currentTimeDate = datetime.now() - relativedelta(years=2)
currentyear = currentTimeDate.strftime('%Y')

POPULATION_DATA = [
    ('orgId', '101'),
    ('tblId', 'DT_1IN1502'),
    ('language', 'ko'),
    ('file', ''),
    ('analText', ''),
    ('scrId', ''),
    ('fieldList',
     f'[{{"targetId":"PRD","targetValue":"","prdValue":"Y,{currentyear},@"}},'
     '{"targetId":"ITM_ID","targetValue":"T100","prdValue":""},{"targetId":"ITM_ID","targetValue":"T110","prdValue":""},{"targetId":"ITM_ID","targetValue":"T120","prdValue":""},{"targetId":"ITM_ID","targetValue":"T130","prdValue":""},{"targetId":"ITM_ID","targetValue":"T131","prdValue":""},{"targetId":"ITM_ID","targetValue":"T132","prdValue":""},{"targetId":"ITM_ID","targetValue":"T140","prdValue":""},{"targetId":"ITM_ID","targetValue":"T141","prdValue":""},{"targetId":"ITM_ID","targetValue":"T142","prdValue":""},{"targetId":"ITM_ID","targetValue":"T200","prdValue":""},{"targetId":"ITM_ID","targetValue":"T210","prdValue":""},{"targetId":"ITM_ID","targetValue":"T220","prdValue":""},{"targetId":"ITM_ID","targetValue":"T230","prdValue":""},{"targetId":"ITM_ID","targetValue":"T310","prdValue":""},{"targetId":"ITM_ID","targetValue":"T311","prdValue":""},{"targetId":"ITM_ID","targetValue":"T312","prdValue":""},{"targetId":"ITM_ID","targetValue":"T313","prdValue":""},{"targetId":"ITM_ID","targetValue":"T314","prdValue":""},{"targetId":"ITM_ID","targetValue":"T315","prdValue":""},{"targetId":"ITM_ID","targetValue":"T320","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"00","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"04","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"05","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"03","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"24","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"25","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"26","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"29","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"39","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11070","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11080","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11090","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11100","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11110","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11120","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11130","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11140","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11150","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11160","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11170","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11180","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11190","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11200","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11210","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11220","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11230","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11240","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"11250","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21070","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21080","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21090","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21100","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21110","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21120","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21130","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21140","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21150","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"21310","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22070","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"22310","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23070","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23080","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23090","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23310","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"23320","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"24010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"24020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"24030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"24040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"24050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"25010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"25020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"25030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"25040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"25050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"26004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"26005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"26003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"26010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"26020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"26030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"26040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"26310","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"29004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"29005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"29003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"29010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31011","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31012","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31013","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31014","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31021","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31022","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31023","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31041","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31042","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31051","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31052","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31053","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31070","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31080","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31090","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31091","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31092","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31100","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31101","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31103","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31104","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31110","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31120","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31130","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31140","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31150","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31160","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31170","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31180","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31190","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31191","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31192","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31193","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31200","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31210","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31220","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31230","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31240","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31250","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31260","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31270","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31280","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31350","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31370","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"31380","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32070","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32310","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32320","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32330","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32340","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32350","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32360","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32370","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32380","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32390","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32400","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"32410","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33041","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33042","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33043","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33044","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33320","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33330","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33340","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33350","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33360","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33370","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33380","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"33390","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34011","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34012","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34070","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34080","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34310","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34330","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34340","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34350","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34360","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34370","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"34380","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35011","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35012","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35310","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35320","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35330","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35340","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35350","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35360","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35370","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"35380","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36310","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36320","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36330","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36350","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36360","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36370","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36380","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36390","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36400","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36410","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36420","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36430","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36440","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36450","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36460","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36470","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"36480","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37011","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37012","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37020","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37040","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37070","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37080","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37090","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37100","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37310","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37320","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37330","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37340","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37350","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37360","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37370","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37380","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37390","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37400","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37410","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37420","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"37430","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38030","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38050","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38060","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38070","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38080","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38090","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38100","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38110","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38111","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38112","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38113","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38114","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38115","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38310","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38320","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38330","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38340","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38350","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38360","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38370","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38380","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38390","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"38400","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"39004","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"39005","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"39003","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"39010","prdValue":""},{"targetId":"OV_L1_ID","targetValue":"39020","prdValue":""}]'),
    ('colAxis', 'TIME,ITEM'),
    ('rowAxis', 'A'),
    ('isFirst', 'N'),
    ('contextPath', '/statHtml'),
    ('ordColIdx', ''),
    ('ordType', ''),
    ('logSeq', '110339461'),
    ('vwCd', 'MT_ZTITLE'),
    ('listId', 'A11_2015_1_10_10'),
    ('connPath', 'MT_ZTITLE'),
    ('statId', '1962001'),
    ('pub', ''),
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
    ('mode', 'tab'),
    ('dataOpt', 'ko'),
    ('noSelect', ''),
    ('view', 'csv'),
    ('existStblCmmtKor', 'Y'),
    ('existStblCmmtEng', 'Y'),
    ('classAllArr', '[{"objVarId":"A","ovlSn":"1"}]'),
    ('classSet', '[{"objVarId":"A","ovlSn":"1","visible":"true"}]'),
    ('selectAllFlag', 'N'),
    ('selectTimeRangeCnt', ''),
    ('periodStr', 'Y'),
    ('funcPrdSe', ''),
    ('tblNm', '인구, 가구 및 주택 - 읍면동(2015,2020), 시군구(2016~2019)'),
    ('tblEngNm', 'Population, Households and Housing Units'),
    ('isChangedDataOpt', ''),
    ('itemMultiply', '6560'),
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
    ('first_open', 'Y'),
    ('debug', ''),
    ('maxCellOver', ''),
    ('reqCellCnt', '6560'),
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
    ('tableType', 'default'),
    ('dataOpt2', 'ko'),
    ('periodCo', ''),
    ('prdSort', 'asc'),
    ('findData', 'on'),
    ('compValue', ''),
    ('compValue01', ''),
    ('compValue02', ''),
    ('expDash', 'Y'),
    ('downGridFileType', 'csv'),
    ('downSort', 'asc'),
    ('pointType', 'screen'),
    ('downLargeFileType', 'excel'),
    ('downLargeExprType', '1'),
    ('downLargeSort', 'asc'),
    ('naviInfo', 'tabItemText'),
    ('naviInfo', 'A'),
    ('naviInfo', 'tabTimeText'),
    ('itemChkLi', 'T100'),
    ('itemChkLi', 'T110'),
    ('itemChkLi', 'T120'),
    ('itemChkLi', 'T130'),
    ('itemChkLi', 'T131'),
    ('itemChkLi', 'T132'),
    ('itemChkLi', 'T140'),
    ('itemChkLi', 'T141'),
    ('itemChkLi', 'T142'),
    ('itemChkLi', 'T200'),
    ('itemChkLi', 'T210'),
    ('itemChkLi', 'T220'),
    ('itemChkLi', 'T230'),
    ('itemChkLi', 'T310'),
    ('itemChkLi', 'T311'),
    ('itemChkLi', 'T312'),
    ('itemChkLi', 'T313'),
    ('itemChkLi', 'T314'),
    ('itemChkLi', 'T315'),
    ('itemChkLi', 'T320'),
    ('classLvlAllChk1_3', 'on'),
    ('classChkLi1_1', '00='),
    ('defaultFolder', '1'),
    ('classChkLi1_1', '04='),
    ('defaultFolder', '1'),
    ('classChkLi1_1', '05='),
    ('defaultFolder', '1'),
    ('classChkLi1_1', '03='),
    ('defaultFolder', '1'),
    ('classChkLi1_1', '11='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '21='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '22='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '23='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '24='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '25='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '26='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '29='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '31='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '32='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '33='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '34='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '35='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '36='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '37='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '38='),
    ('defaultFolder', '0'),
    ('classChkLi1_1', '39='),
    ('defaultFolder', '0'),
    ('classLvlAllChk1_3', 'on'),
    ('headCheck', 'Y'),
    ('timeChkY', f'{currentyear}'),
]

POPULATION_DOWN_URL = 'https://kosis.kr/statHtml/downNormal.do'
POPULATION_DOWN_COOKIES = {
    'JSESSIONID': 'HT4MF4EF88KSXT5tTtbhC3bMOzP9SkSMslj0DxDS3O7zzJ8Ypp6smGgbO7UEmdHd.STAT_SIGA1_servlet_engine5',
}
POPULATION_DOWN_HEADER = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://kosis.kr',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://kosis.kr/statHtml/statHtml.do?mode=tab&orgId=101&tblId=DT_1IN1502&vw_cd=MT_ZTITLE&list_id=A11_2015_1_10_10&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=MT_ZTITLE&path=%252FstatisticsList%252FstatisticsListIndex.do%27',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
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
                         ('fieldList', f'[{{"targetId":"PRD","targetValue":"","prdValue":"Y,{currentyear},@"}},'
                                       '{"targetId":"ITM_ID","targetValue":"T100","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T110","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T120","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T130","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T131","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T132","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T140","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T141","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T142","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T200","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T210","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T220","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T230","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T310","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T311","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T312","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T313","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T314","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T315","prdValue":""},'
                                       '{"targetId":"ITM_ID","targetValue":"T320","prdValue":""},'
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
                         ('colAxis', 'TIME,ITEM'),
                         ('rowAxis', 'A'),
                         ('isFirst', 'N'),
                         ('contextPath', '/statHtml'),
                         ('ordColIdx', ''),
                         ('ordType', ''),
                         ('logSeq', '110308094'),
                         ('vwCd', 'MT_ZTITLE'),
                         ('listId', 'A11_2015_1_10_10'),
                         ('connPath', 'MT_ZTITLE'),
                         ('statId', '1962001'),
                         ('pub', ''),
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
                         ('mode', 'tab'),
                         ('dataOpt', 'ko'),
                         ('noSelect', ''),
                         ('view', 'csv'),
                         ('existStblCmmtKor', 'Y'),
                         ('existStblCmmtEng', 'Y'),
                         ('classAllArr', '[{"objVarId":"A","ovlSn":"1"}]'),
                         ('classSet', '[{"objVarId":"A","ovlSn":"1","visible":"true"}]'),
                         ('selectAllFlag', 'N'),
                         ('selectTimeRangeCnt', ''),
                         ('periodStr', 'Y'),
                         ('funcPrdSe', ''),
                         ('tblNm', '인구, 가구 및 주택 - 읍면동                         (2015,2020), 시군구                         (2016~2019)'),
                         ('tblEngNm', 'Population, Households and Housing Units'),
                         ('isChangedDataOpt', ''),
                         ('itemMultiply', '6560'),
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
                         ('first_open', 'Y'),
                         ('debug', ''),
                         ('maxCellOver', ''),
                         ('reqCellCnt', '6560'),
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
                         ('tableType', 'default'),
                         ('dataOpt2', 'ko'),
                         ('periodCo', ''),
                         ('prdSort', 'desc'),
                         ('findData', 'on'),
                         ('compValue', ''),
                         ('compValue01', ''),
                         ('compValue02', ''),
                         ('expDash', 'Y'),
                         ('downGridFileType', 'csv'),
                         ('downSort', 'asc'),
                         ('pointType', 'screen'),
                         ('downLargeFileType', 'excel'),
                         ('downLargeExprType', '1'),
                         ('downLargeSort', 'asc'),
                         ('naviInfo', 'tabItemText'),
                         ('naviInfo', 'A'),
                         ('naviInfo', 'tabTimeText'),
                         ('itemChkLi', 'T100'),
                         ('itemChkLi', 'T110'),
                         ('itemChkLi', 'T120'),
                         ('itemChkLi', 'T130'),
                         ('itemChkLi', 'T131'),
                         ('itemChkLi', 'T132'),
                         ('itemChkLi', 'T140'),
                         ('itemChkLi', 'T141'),
                         ('itemChkLi', 'T142'),
                         ('itemChkLi', 'T200'),
                         ('itemChkLi', 'T210'),
                         ('itemChkLi', 'T220'),
                         ('itemChkLi', 'T230'),
                         ('itemChkLi', 'T310'),
                         ('itemChkLi', 'T311'),
                         ('itemChkLi', 'T312'),
                         ('itemChkLi', 'T313'),
                         ('itemChkLi', 'T314'),
                         ('itemChkLi', 'T315'),
                         ('itemChkLi', 'T320'),
                         ('classLvlAllChk1_3', 'on'),
                         ('classChkLi1_1', '00='),
                         ('defaultFolder', '1'),
                         ('classChkLi1_1', '04='),
                         ('defaultFolder', '1'),
                         ('classChkLi1_1', '05='),
                         ('defaultFolder', '1'),
                         ('classChkLi1_1', '03='),
                         ('defaultFolder', '1'),
                         ('classChkLi1_1', '11='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '21='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '22='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '23='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '24='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '25='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '26='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '29='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '31='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '32='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '33='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '34='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '35='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '36='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '37='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '38='),
                         ('defaultFolder', '0'),
                         ('classChkLi1_1', '39='),
                         ('defaultFolder', '0'),
                         ('classLvlAllChk1_3', 'on'),
                         ('headCheck', 'Y'),
                         ('timeChkY', f'{currentyear}'),
                         ]
    POPULATION_DATA.extend(POPULATION_DATA_1)
    POPULATION_DATA.extend(POPULATION_DATA_2)
    POPULATION_DATA.extend(POPULATION_DATA_3)
    return POPULATION_DATA