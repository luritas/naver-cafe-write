# 아파트 실거래가 조회
import os
import urllib.request
import json
import xmltodict


def search(region, date):
    service_key = os.environ.get("APT_TRADE_SERVICE_KEY")
    region_code = urllib.parse.quote(get_region_code(region))
    url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?"
    param = "LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}&serviceKey={SERVICE_KEY}" \
        .format(LAWD_CD=region_code, DEAL_YMD=date, SERVICE_KEY=service_key)
    # print(url + param)
    request = urllib.request.Request(url + param)
    response = urllib.request.urlopen(request)
    res_code = response.getcode()
    if res_code == 200:
        response_body = response.read()
        content = xmltodict.parse(response_body.decode('utf-8'))
        return json.dumps(content)
    else:
        return "Error Code:" + res_code


def get_region_code(region):
    return '11305'


# 모듈로 호출하지 않고 메인에서 호출했을 경우에만 실행
if __name__ == "__main__":
    print(search('미아동', '201802'))
