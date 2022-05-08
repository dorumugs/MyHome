ACTUAL_TX_URL = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?"
ACTUAL_TX_FINAL = './data/tx/final_files/actual_tx.csv'
CHARTERED_RENT_URL = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?"
CHARTERED_RENT_FINAL = './data/tx/final_files/chartered_rent.csv'
CODE_FILE_NAME = "./data/csv/code.csv"
ACTUAL_TX_COLUMNS = ['거래금액', '거래유형', '건축년도', '년', '법정동', '아파트', '월', '일', '전용면적',
                     '중개사소재지', '지번', '지역코드', '층']
IN_ACTUAL_TX_COLUMNS = ['거래유형', '중개사소재지']
EX_ACTUAL_TX_COLUMNS = ['해제사유발생일', '해제여부']
CHARTERED_RENT_TX_COLUMNS = ['갱신요구권사용', '건축년도', '계약구분', '계약기간', '년', '법정동', '보증금액', '아파트', '월', '월세금액',
                             '일', '전용면적', '종전계약보증금', '종전계약월세', '지번', '지역코드', '층']
IN_CHARTERED_RENT_TX_COLUMNS = ['갱신요구권사용', '계약구분', '계약기간', '종전계약보증금', '종전계약월세', '보증금액', '월세금액']
EX_CHARTERED_RENT_TX_COLUMNS = ['거래금액', '해제사유발생일', '해제여부']
ACTUAL_TX_COLUMNS_PRE = ['시도명', '시군구명', '법정동', '지번', '지역코드', '건축년도', '아파트', '전용면적', '층', '거래일', '거래금액',
                         '년', '월', '일', '분기']
CHARTERED_RENT_TX_COLUMNS_PRE = ['시도명', '시군구명', '법정동', '지번', '지역코드', '건축년도', '아파트', '전용면적', '층', '거래일',
                                 '보증금액', '월세금액', '년', '월', '일', '분기']
