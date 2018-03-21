# 아파트 실거래가 조회
# http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?LAWD_CD=11305&DEAL_YMD=201803&pageNo=1&serviceKey=uSBGVwdHO%2Bf7zwY%2B7LSMMKwDTrmKkc9pT429CFbwuCeq2vkJmm9EXG1G5DtpiPFGN8m%2BTD4ykq0YVR%2FjXLXinw%3D%3D

import json
import math
import sys
import urllib.request
from datetime import datetime
from dateutil.relativedelta import relativedelta

from packages.open_api import OpenApi
from packages.db import Database


class AptRealPriceTrade(OpenApi):

    def __init__(self):
        super().__init__()
        self.url_name = "apt_real_price_trade"
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

    def create_select_sql(self):
        return """
            SELECT `apt_real_trade_price`.`id`,
                `apt_real_trade_price`.`price`,
                `apt_real_trade_price`.`completion_date`,
                `apt_real_trade_price`.`year`,
                `apt_real_trade_price`.`road_address`,
                `apt_real_trade_price`.`road_main_code`,
                `apt_real_trade_price`.`road_sub_code`,
                `apt_real_trade_price`.`road_sigungu_code`,
                `apt_real_trade_price`.`road_serial_code`,
                `apt_real_trade_price`.`road_under_code`,
                `apt_real_trade_price`.`road_code`,
                `apt_real_trade_price`.`law_name`,
                `apt_real_trade_price`.`law_main_code`,
                `apt_real_trade_price`.`law_sub_code`,
                `apt_real_trade_price`.`law_sigungu_code`,
                `apt_real_trade_price`.`law_umd_code`,
                `apt_real_trade_price`.`law_jibun_code`,
                `apt_real_trade_price`.`apt_name`,
                `apt_real_trade_price`.`month`,
                `apt_real_trade_price`.`day`,
                `apt_real_trade_price`.`serial_number`,
                `apt_real_trade_price`.`private_area`,
                `apt_real_trade_price`.`jibun`,
                `apt_real_trade_price`.`region_code`,
                `apt_real_trade_price`.`floor`,
                `apt_real_trade_price`.`status`,
                `apt_real_trade_price`.`created_at`
            FROM `naver`.`apt_real_trade_price`;
        """

    def create_sql(self):
        sql = """
    INSERT INTO `apt_real_trade_price`
(`id`,
`price`,
`completion_date`,
`year`,
`road_address`,

`road_main_code`,
`road_sub_code`,
`road_sigungu_code`,
`road_serial_code`,
`road_under_code`,

`road_code`,
`law_name`,
`law_main_code`,
`law_sub_code`,
`law_sigungu_code`,

`law_umd_code`,
`law_jibun_code`,
`apt_name`,
`month`,
`day`,

`serial_number`,
`private_area`,
`jibun`,
`region_code`,
`floor`,
`status`)
VALUES
(NULL,
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
%s,
%s,
0) ON DUPLICATE KEY UPDATE `status` = 2;
"""
        return sql

    def create_param(self, items):
        param = []
        for index, item in enumerate(items):
            try:
                item['도로명지상지하코드']
            except Exception as e:
                item['도로명지상지하코드'] = ''

            # print("[" + str(index) + "]" + item['아파트'] + " 단지 실거래가를 추가하였습니다")
            param.append(tuple([
                item['거래금액'],
                item['건축년도'],
                item['년'],
                item['도로명'],

                item['도로명건물본번호코드'],
                item['도로명건물부번호코드'],
                item['도로명시군구코드'],
                item['도로명일련번호코드'],
                item['도로명지상지하코드'],

                item['도로명코드'],
                item['법정동'],
                item['법정동본번코드'],
                item['법정동부번코드'],
                item['법정동시군구코드'],

                item['법정동읍면동코드'],
                item['법정동지번코드'],
                item['아파트'],
                item['월'],
                item['일'],

                item['일련번호'],
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


# 모듈로 호출하지 않고 메인에서 호출했을 경우에만 실행
if __name__ == "__main__":
    today_date = datetime.today()
    today_month = today_date.strftime("%Y%m")
    one_month_ago = (today_date - relativedelta(months=1)).strftime("%Y%m")
    two_month_ago = (today_date - relativedelta(months=2)).strftime("%Y%m")

    print(two_month_ago + " 이후의 실거래가를 조회합니다")
    print("=" * 50)

    months = (two_month_ago, one_month_ago, today_month)
    real_price_trade = AptRealPriceTrade()
    total_items = []
    for month in months:
        print(str(month) + "를 조회합니다")
        content = real_price_trade.get_parsed_content('강북구', str(month), 1, 1)

        if real_price_trade.get_result_code_from_parsed_content(content) != "00":
            raise Exception('공공데이터 포털 통신 오류')

        total_count = real_price_trade.get_total_count(content)
        row_per_page = 10
        total_page_no = int(math.ceil(total_count / row_per_page)) + 1

        for i in range(1, total_page_no):
            print("Page Number: " + str(i))
            content = real_price_trade.get_parsed_content('강북구', str(month), i, row_per_page)
            items = real_price_trade.get_items_from_parsed_content(content)
            for item in items:
                total_items.append(item)

    # pprint(total_items)
    db = Database()
    db.connect()
    sql = real_price_trade.create_sql()
    param = real_price_trade.create_param(total_items)  # for 문 돌면서 items에 있는것들 모두 받을 수 있게 바꾸기
    db.insert(sql, param)

    db.close()
    #  print(search('미아동', '201802'))
    # response => body => items => item 배열에 {}로 나옴
