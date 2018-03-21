# 아파트 전월세 조회
# http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?LAWD_CD=11305&DEAL_YMD=201801&pageNo=1&numOfRows=1&serviceKey=uSBGVwdHO%2Bf7zwY%2B7LSMMKwDTrmKkc9pT429CFbwuCeq2vkJmm9EXG1G5DtpiPFGN8m%2BTD4ykq0YVR%2FjXLXinw%3D%3D

import json
import math
import urllib.request
import sys
from pprint import pprint
from datetime import datetime
from dateutil.relativedelta import relativedelta

from open_api import OpenApi
from db import Database


class AptRealRent(OpenApi):

    def __init__(self):
        super().__init__()
        self.url_name = "apt_real_rent"
        self.param = None

    def set_param(self, param):
        region_code = urllib.parse.quote(self.__get_region_code(param['region']))
        self.param = "LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}&pageNo={page_no}&numOfRows={row_per_page}" \
            .format(LAWD_CD=region_code, DEAL_YMD=param['date'], page_no=param['page_no'],
                    row_per_page=param['row_per_page'])

    def save_database_from_open_api(self, item):
        pass

    def __get_region_code(self, region):
        return '11305'

    def create_sql(self):
        return """
INSERT INTO `naver`.`apt_real_rent`
(`id`,
`completion date`,
`year`,
`law_name`,
`deposit`,

`apt_name`,
`month`,
`rent_fee`,
`day`,
`private_area`,

`jibun`,
`region_code`,
`floor`)
VALUES
(null,
%s,
%s,
%s,
%s,

%s,
%s,
%s,
%s,
%s,

%s,
%s,
%s);
"""

    def create_param(self, items):
        param = []
        for index, item in enumerate(items):
            # print("[" + str(index) + "]" + item['아파트'] + " 단지 실거래가를 추가하였습니다")
            param.append(tuple([
                item['건축년도'],
                item['년'],
                item['법정동'],
                item['보증금액'],
                item['아파트'],

                item['월'],
                item['월세금액'],
                item['일'],
                item['전용면적'],

                item['지번'],
                item['지역코드'],
                item['층'],
            ]))

        return tuple(param)

    def get_parsed_content(self, region, date, page_no, row_per_page):
        self.set_param({"region": region, "date": date, "page_no": page_no, "row_per_page": row_per_page})
        json_content = self.get_content()
        return json.loads(json_content)

    def get_body_from_parsed_content(self, content):
        return content['response']['body']

    def get_header_from_parsed_content(self, content):
        return content['response']['header']

    def get_items_from_parsed_content(self, content):
        try:
            return self.get_body_from_parsed_content(content)['items']['item']
        except Exception as e:
            print(e)
            sys.exit()

    def get_result_code_from_parsed_content(self, content):
        return self.get_header_from_parsed_content(content)['resultCode']

    def get_total_count(self, content):
        return int(self.get_body_from_parsed_content(content)['totalCount'])

if __name__ == "__main__":
    today_date = datetime.today()
    today_month = today_date.strftime("%Y%m")
    one_month_ago = (today_date - relativedelta(months=1)).strftime("%Y%m")
    two_month_ago = (today_date - relativedelta(months=2)).strftime("%Y%m")

    print(two_month_ago + " 이후의 임대차거래를 조회합니다")
    print("=" * 50)

    months = (two_month_ago, one_month_ago, today_month)
    apt_real_rent = AptRealRent()
    total_items = []
    for month in months:
        print(str(month) + " 임대차 거래가를 조회합니다")
        content = apt_real_rent.get_parsed_content('강북구', str(month), 1, 1)

        if apt_real_rent.get_result_code_from_parsed_content(content) != "00":
            raise Exception('공공데이터 포털 통신 오류')

        total_count = apt_real_rent.get_total_count(content)
        row_per_page = 999999
        total_page_no = int(math.ceil(total_count / row_per_page)) + 1

        for i in range(1, total_page_no):
            print("Page Number: " + str(i))
            content = apt_real_rent.get_parsed_content('강북구', str(month), i, row_per_page)
            items = apt_real_rent.get_items_from_parsed_content(content)
            for item in items:
                total_items.append(item)

    # pprint(total_items)
    db = Database()
    db.connect()
    sql = apt_real_rent.create_sql()
    param = apt_real_rent.create_param(total_items)  # for 문 돌면서 items에 있는것들 모두 받을 수 있게 바꾸기
    db.insert(sql, param)

    db.close()
    #  print(search('미아동', '201802'))
    # response => body => items => item 배열에 {}로 나옴
