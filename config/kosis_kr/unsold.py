# 미분양 정보 세팅
import pandas as pd
from datetime import date

UNSOLD_URL = 'https://kosis.kr/statHtml/makeLarge.do'
UNSOLD_COOKIES = {
    'newKOSIS2020StatisCtgrSettingCookie_1': 'A%7CB%7CC%7CD%7CE%7CF%7CG%7CH1%7CI1%7CH2%7CN1%7CN2%7CT%7CU%7CK1%7CK2%7CJ1%7CJ2%7CL%7CM1%7CM2%7CO%7CO2%7CP%7CQ%7CR%7CS1%7CS2%7CI2%7CV',
    'mb': 'N',
    'JSESSIONID': 'EnL7qKu1dUa9sWANoarCunMr1Ko8iHEmxcZlMeTPO3wtw2T6JwUgaD7aVBnSh6KM.STAT_WAS1_servlet_engine5',
}
UNSOLD_HEADERS = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://kosis.kr',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://kosis.kr/statHtml/statHtml.do?orgId=116&tblId=DT_MLTM_2080&vw_cd=&list_id=&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=E1&docId=0317427997&markType=S&itmNm=%EC%A0%84%EA%B5%AD',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
}


UNSOLD_DOWN_HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://kosis.kr',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://kosis.kr/statHtml/statHtml.do?orgId=116&tblId=DT_MLTM_2080&vw_cd=&list_id=&scrId=&seqNo=&lang_mode=ko&obj_var_id=&itm_id=&conn_path=E1&docId=0317427997&markType=S&itmNm=%EC%A0%84%EA%B5%AD',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7',
}
UNSOLD_DOWN_COOKIES = {
    'newKOSIS2020StatisCtgrSettingCookie_1': 'A%7CB%7CC%7CD%7CE%7CF%7CG%7CH1%7CI1%7CH2%7CN1%7CN2%7CT%7CU%7CK1%7CK2%7CJ1%7CJ2%7CL%7CM1%7CM2%7CO%7CO2%7CP%7CQ%7CR%7CS1%7CS2%7CI2%7CV',
    'mb': 'N',
    'JSESSIONID': 'EnL7qKu1dUa9sWANoarCunMr1Ko8iHEmxcZlMeTPO3wtw2T6JwUgaD7aVBnSh6KM.STAT_WAS1_servlet_engine5',
}

def unsold_url(csv):
    url = f'https://kosis.kr/statHtml/downLarge.do?file={csv}'
    return url

def create_unsold_data():
    UNSOLD_DATA = []
    data_1 = [
        ('orgId', '116'),
        ('tblId', 'DT_MLTM_2080'),
        ('language', 'ko'),
        ('file', ''),
        ('analText', ''),
        ('scrId', ''),
    ]

    today = date.today()
    today_ym = today.strftime("%Y%m%d")
    date_data = pd.date_range('20070101', today_ym)
    date_data_list_sort = list(set(date_data.format(formatter=lambda x: x.strftime('%Y%m'))))
    date_data_list_reverse = date_data_list_sort
    date_data_list_sort.sort()
    date_data_list_reverse.reverse()
    max_date = date_data_list_sort[-1]
    date_data = ','.join(date_data_list_sort)
    data_2 = [
        ('fieldList',
         f'[{{"targetId":"PRD","targetValue":"","prdValue":"M,{date_data},@"}},'
         '{"targetId":"ITM_ID","targetValue":"13103792722T1","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0001","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0002","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0003","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0004","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0005","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0006","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0007","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0008","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0009","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0010","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0011","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0012","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0013","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0014","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0015","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0016","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0017","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0018","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0019","prdValue":""},'
         '{"targetId":"OV_L2_ID","targetValue":"13102792722B.0001","prdValue":""},'
         '{"targetId":"OV_L2_ID","targetValue":"13102792722B.0002","prdValue":""},'
         '{"targetId":"OV_L2_ID","targetValue":"13102792722B.0003","prdValue":""},'
         '{"targetId":"OV_L3_ID","targetValue":"13102792722C.0001","prdValue":""},'
         '{"targetId":"OV_L3_ID","targetValue":"13102792722C.0002","prdValue":""},'
         '{"targetId":"OV_L3_ID","targetValue":"13102792722C.0003","prdValue":""},'
         '{"targetId":"OV_L3_ID","targetValue":"13102792722C.0004","prdValue":""},'
         '{"targetId":"OV_L3_ID","targetValue":"13102792722C.0005","prdValue":""}]'),
    ]
    data_3 = [
        ('colAxis', 'TIME,13101792722B,13101792722C'),
        ('rowAxis', '13101792722A'),
        ('isFirst', 'N'),
        ('contextPath', '/statHtml'),
        ('ordColIdx', ''),
        ('ordType', ''),
        ('logSeq', '106033059'),
        ('vwCd', ''),
        ('listId', ''),
        ('connPath', 'E1'),
        ('statId', '1998033'),
        ('pub', ''),
        ('pubLog', '4'),
        ('viewKind', '2'),
        ('viewSubKind', '2_7_2'),
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
        ('existStblCmmtKor', 'Y'),
        ('existStblCmmtEng', 'N'),
        ('classAllArr',
         '[{"objVarId":"13101792722A","ovlSn":"1"},{"objVarId":"13101792722B","ovlSn":"2"},{"objVarId":"13101792722C","ovlSn":"3"}]'),
        ('classSet',
         '[{"objVarId":"13101792722A","ovlSn":"1","visible":"true"},{"objVarId":"13101792722B","ovlSn":"2","visible":"true"},{"objVarId":"13101792722C","ovlSn":"3","visible":"true"}]'),
        ('selectAllFlag', 'N'),
        ('selectTimeRangeCnt', '3'),
        ('periodStr', 'M'),
        ('funcPrdSe', ''),
        ('tblNm', '\uADDC\uBAA8\uBCC4 \uBBF8\uBD84\uC591\uD604\uD669'),
        ('tblEngNm', 'Unsold Housings by Size'),
        ('isChangedDataOpt', ''),
        ('itemMultiply', '285'),
        ('dimCo', '152'),
        ('dbUser', 'NSI.'),
        ('usePivot', 'N'),
        ('isChangedTableType', 'N'),
        ('isChangedPeriodCo', 'N'),
        ('isChangedPrdSort', 'N'),
        ('p_chkStatus', ''),
        ('p_objVarId', ''),
        ('p_lvl', ''),
        ('p_logicFlag', 'Y'),
        ('p_classAllChkYn', 'Y'),
        ('p_classAllSelectYn', 'N'),
        ('useAddFuncLog', ''),
        ('chargerLvl', ''),
        ('st', ''),
        ('new_win', ''),
        ('first_open', 'Y'),
        ('debug', ''),
        ('maxCellOver', ''),
        ('reqCellCnt', '855'),
        ('inheritYn', 'N'),
        ('originOrgId', ''),
        ('originTblId', ''),
        ('pubSeType', ''),
        ('relChkOrgId', ''),
        ('relChkTblId', ''),
    ]
    data_4 = [
        ('highLightStr',
         f'[{{"targetId":"PRD","targetValue":"{max_date}","prdSe":"M"}},'
         '{"targetId":"ITM","targetValue":"13103792722T1"},'
         '{"targetId":"VAL","val":"15,786","originVal":"15786"},'
         '{"targetId":"CLASS",'
         '"value":{"objId1":"13101792722A","OV_L1_ID":"13102792722A.0001","objId2":"13101792722B",'
         '"OV_L2_ID":"13102792722B.0001","objId3":"13101792722C","OV_L3_ID":"13102792722C.0001"},"classCnt":3}]'),
    ]
    data_5 = [
        ('markType', 'S'),
        ('docId', '3174'),
        ('itmNm', '\uC804\uAD6D'),
        ('tableType', 'default'),
        ('dataOpt2', 'ko'),
        ('periodCo', ''),
        ('enableLevelExpr', 'Y'),
        ('prdSort', 'desc'),
        ('findData', 'on'),
        ('compValue', ''),
        ('compValue01', ''),
        ('compValue02', ''),
        ('expDash', 'Y'),
        ('downGridFileType', 'xlsx'),
        ('downGridCellMerge', 'Y'),
        ('downGridMeta', 'Y'),
        ('downSort', 'asc'),
        ('pointType', 'screen'),
        ('downLargeFileType', 'csv'),
        ('downLargeExprType', '1'),
        ('downLargeSort', 'asc'),
        ('naviInfo', 'tabItemText'),
        ('naviInfo', '13101792722A'),
        ('naviInfo', '13101792722B'),
        ('naviInfo', '13101792722C'),
        ('naviInfo', 'tabTimeText'),
        ('itemChkLi', '13103792722T1'),
        ('classAllSelect', 'on'),
        ('classAllSelect', 'on'),
        ('classAllSelect', 'on'),
        ('classLvlAllChk1_1', 'on'),
        ('classChkLi1_1', '13102792722A.0001='),
        ('classChkLi1_1', '13102792722A.0002='),
        ('classChkLi1_1', '13102792722A.0003='),
        ('classChkLi1_1', '13102792722A.0004='),
        ('classChkLi1_1', '13102792722A.0005='),
        ('classChkLi1_1', '13102792722A.0006='),
        ('classChkLi1_1', '13102792722A.0007='),
        ('classChkLi1_1', '13102792722A.0008='),
        ('classChkLi1_1', '13102792722A.0009='),
        ('classChkLi1_1', '13102792722A.0010='),
        ('classChkLi1_1', '13102792722A.0011='),
        ('classChkLi1_1', '13102792722A.0012='),
        ('classChkLi1_1', '13102792722A.0013='),
        ('classChkLi1_1', '13102792722A.0014='),
        ('classChkLi1_1', '13102792722A.0015='),
        ('classChkLi1_1', '13102792722A.0016='),
        ('classChkLi1_1', '13102792722A.0017='),
        ('classChkLi1_1', '13102792722A.0018='),
        ('classChkLi1_1', '13102792722A.0019='),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('classLvlAllChk2_1', 'on'),
        ('classChkLi2_1', '13102792722B.0001='),
        ('classChkLi2_1', '13102792722B.0002='),
        ('classChkLi2_1', '13102792722B.0003='),
        ('classLvlAllChk3_1', 'on'),
        ('classChkLi3_1', '13102792722C.0001='),
        ('classChkLi3_1', '13102792722C.0002='),
        ('classChkLi3_1', '13102792722C.0003='),
        ('classChkLi3_1', '13102792722C.0004='),
        ('classChkLi3_1', '13102792722C.0005='),
        ('headCheck', 'M'),
    ]
    data_6 = []
    for i in date_data_list_reverse:
        temp = ('timeChkM', i)
        data_6.append(temp)
    UNSOLD_DATA.extend(data_1)
    UNSOLD_DATA.extend(data_2)
    UNSOLD_DATA.extend(data_3)
    UNSOLD_DATA.extend(data_4)
    UNSOLD_DATA.extend(data_5)
    UNSOLD_DATA.extend(data_6)
    return UNSOLD_DATA

def create_unsold_download_data():
    UNSOLD_DOWN_DATA = []
    data_1 = [
        ('orgId', '116'),
        ('tblId', 'DT_MLTM_2080'),
        ('language', 'ko'),
        ('file', ''),
        ('analText', ''),
        ('scrId', ''),
    ]

    today = date.today()
    today_ym = today.strftime("%Y%m%d")
    date_data = pd.date_range('20070101', today_ym)
    date_data_list_sort = list(set(date_data.format(formatter=lambda x: x.strftime('%Y%m'))))
    date_data_list_reverse = date_data_list_sort
    date_data_list_sort.sort()
    date_data_list_reverse.reverse()
    max_date = date_data_list_sort[-1]
    date_data = ','.join(date_data_list_sort)
    data_2 = [
        ('fieldList',
         f'[{{"targetId":"PRD","targetValue":"","prdValue":"M,{date_data},@"}},'
         '{"targetId":"ITM_ID","targetValue":"13103792722T1","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0001","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0002","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0003","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0004","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0005","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0006","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0007","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0008","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0009","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0010","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0011","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0012","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0013","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0014","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0015","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0016","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0017","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0018","prdValue":""},'
         '{"targetId":"OV_L1_ID","targetValue":"13102792722A.0019","prdValue":""},'
         '{"targetId":"OV_L2_ID","targetValue":"13102792722B.0001","prdValue":""},'
         '{"targetId":"OV_L2_ID","targetValue":"13102792722B.0002","prdValue":""},'
         '{"targetId":"OV_L2_ID","targetValue":"13102792722B.0003","prdValue":""},'
         '{"targetId":"OV_L3_ID","targetValue":"13102792722C.0001","prdValue":""},'
         '{"targetId":"OV_L3_ID","targetValue":"13102792722C.0002","prdValue":""},'
         '{"targetId":"OV_L3_ID","targetValue":"13102792722C.0003","prdValue":""},'
         '{"targetId":"OV_L3_ID","targetValue":"13102792722C.0004","prdValue":""},'
         '{"targetId":"OV_L3_ID","targetValue":"13102792722C.0005","prdValue":""}]'),
    ]
    data_3 = [
        ('colAxis', 'TIME,13101792722B,13101792722C'),
        ('rowAxis', '13101792722A'),
        ('isFirst', 'N'),
        ('contextPath', '/statHtml'),
        ('ordColIdx', ''),
        ('ordType', ''),
        ('logSeq', '106033059'),
        ('vwCd', ''),
        ('listId', ''),
        ('connPath', 'E1'),
        ('statId', '1998033'),
        ('pub', ''),
        ('pubLog', '4'),
        ('viewKind', '2'),
        ('viewSubKind', '2_7_2'),
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
        ('existStblCmmtKor', 'Y'),
        ('existStblCmmtEng', 'N'),
        ('classAllArr',
         '[{"objVarId":"13101792722A","ovlSn":"1"},{"objVarId":"13101792722B","ovlSn":"2"},{"objVarId":"13101792722C","ovlSn":"3"}]'),
        ('classSet',
         '[{"objVarId":"13101792722A","ovlSn":"1","visible":"true"},{"objVarId":"13101792722B","ovlSn":"2","visible":"true"},{"objVarId":"13101792722C","ovlSn":"3","visible":"true"}]'),
        ('selectAllFlag', 'N'),
        ('selectTimeRangeCnt', '3'),
        ('periodStr', 'M'),
        ('funcPrdSe', ''),
        ('tblNm', '\uADDC\uBAA8\uBCC4 \uBBF8\uBD84\uC591\uD604\uD669'),
        ('tblEngNm', 'Unsold Housings by Size'),
        ('isChangedDataOpt', ''),
        ('itemMultiply', '285'),
        ('dimCo', '152'),
        ('dbUser', 'NSI.'),
        ('usePivot', 'N'),
        ('isChangedTableType', 'N'),
        ('isChangedPeriodCo', 'N'),
        ('isChangedPrdSort', 'N'),
        ('p_chkStatus', ''),
        ('p_objVarId', ''),
        ('p_lvl', ''),
        ('p_logicFlag', 'Y'),
        ('p_classAllChkYn', 'Y'),
        ('p_classAllSelectYn', 'N'),
        ('useAddFuncLog', ''),
        ('chargerLvl', ''),
        ('st', ''),
        ('new_win', ''),
        ('first_open', 'Y'),
        ('debug', ''),
        ('maxCellOver', ''),
        ('reqCellCnt', '855'),
        ('inheritYn', 'N'),
        ('originOrgId', ''),
        ('originTblId', ''),
        ('pubSeType', ''),
        ('relChkOrgId', ''),
        ('relChkTblId', ''),
    ]
    data_4 = [
        ('highLightStr',
         f'[{{"targetId":"PRD","targetValue":"{max_date}","prdSe":"M"}},'
         '{"targetId":"ITM","targetValue":"13103792722T1"},'
         '{"targetId":"VAL","val":"15,786","originVal":"15786"},'
         '{"targetId":"CLASS",'
         '"value":{"objId1":"13101792722A","OV_L1_ID":"13102792722A.0001","objId2":"13101792722B",'
         '"OV_L2_ID":"13102792722B.0001","objId3":"13101792722C","OV_L3_ID":"13102792722C.0001"},"classCnt":3}]'),
    ]
    data_5 = [
        ('markType', 'S'),
        ('docId', '3174'),
        ('itmNm', '\uC804\uAD6D'),
        ('tableType', 'default'),
        ('dataOpt2', 'ko'),
        ('periodCo', ''),
        ('enableLevelExpr', 'Y'),
        ('prdSort', 'desc'),
        ('findData', 'on'),
        ('compValue', ''),
        ('compValue01', ''),
        ('compValue02', ''),
        ('expDash', 'Y'),
        ('downGridFileType', 'xlsx'),
        ('downGridCellMerge', 'Y'),
        ('downGridMeta', 'Y'),
        ('downSort', 'asc'),
        ('pointType', 'screen'),
        ('downLargeFileType', 'csv'),
        ('downLargeExprType', '1'),
        ('downLargeSort', 'asc'),
        ('naviInfo', 'tabItemText'),
        ('naviInfo', '13101792722A'),
        ('naviInfo', '13101792722B'),
        ('naviInfo', '13101792722C'),
        ('naviInfo', 'tabTimeText'),
        ('itemChkLi', '13103792722T1'),
        ('classAllSelect', 'on'),
        ('classAllSelect', 'on'),
        ('classAllSelect', 'on'),
        ('classLvlAllChk1_1', 'on'),
        ('classChkLi1_1', '13102792722A.0001='),
        ('classChkLi1_1', '13102792722A.0002='),
        ('classChkLi1_1', '13102792722A.0003='),
        ('classChkLi1_1', '13102792722A.0004='),
        ('classChkLi1_1', '13102792722A.0005='),
        ('classChkLi1_1', '13102792722A.0006='),
        ('classChkLi1_1', '13102792722A.0007='),
        ('classChkLi1_1', '13102792722A.0008='),
        ('classChkLi1_1', '13102792722A.0009='),
        ('classChkLi1_1', '13102792722A.0010='),
        ('classChkLi1_1', '13102792722A.0011='),
        ('classChkLi1_1', '13102792722A.0012='),
        ('classChkLi1_1', '13102792722A.0013='),
        ('classChkLi1_1', '13102792722A.0014='),
        ('classChkLi1_1', '13102792722A.0015='),
        ('classChkLi1_1', '13102792722A.0016='),
        ('classChkLi1_1', '13102792722A.0017='),
        ('classChkLi1_1', '13102792722A.0018='),
        ('classChkLi1_1', '13102792722A.0019='),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('defaultFolder', '1'),
        ('classLvlAllChk2_1', 'on'),
        ('classChkLi2_1', '13102792722B.0001='),
        ('classChkLi2_1', '13102792722B.0002='),
        ('classChkLi2_1', '13102792722B.0003='),
        ('classLvlAllChk3_1', 'on'),
        ('classChkLi3_1', '13102792722C.0001='),
        ('classChkLi3_1', '13102792722C.0002='),
        ('classChkLi3_1', '13102792722C.0003='),
        ('classChkLi3_1', '13102792722C.0004='),
        ('classChkLi3_1', '13102792722C.0005='),
        ('headCheck', 'M'),
    ]
    data_6 = []
    for i in date_data_list_reverse:
        temp = ('timeChkM', i)
        data_6.append(temp)
    UNSOLD_DOWN_DATA.extend(data_1)
    UNSOLD_DOWN_DATA.extend(data_2)
    UNSOLD_DOWN_DATA.extend(data_3)
    UNSOLD_DOWN_DATA.extend(data_4)
    UNSOLD_DOWN_DATA.extend(data_5)
    UNSOLD_DOWN_DATA.extend(data_6)
    return UNSOLD_DOWN_DATA
