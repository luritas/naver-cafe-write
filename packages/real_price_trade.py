# 아파트 실거래가 조회
import json
import math
import urllib.request

from open_api import OpenApi

from db import Database
import sys
from pprint import pprint


class RealPriceTrade(OpenApi):

    def __init__(self):
        super().__init__()
        self.url_name = "real_price_trade"
        self.param = None

    def set_param(self, param):
        region_code = urllib.parse.quote(self.__get_region_code(param['region']))
        self.param = "LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}&pageNo={page_no}" \
            .format(LAWD_CD=region_code, DEAL_YMD=param['date'], page_no=param['page_no'])

    def save_database_from_open_api(self, item):
        pass

    def __get_region_code(self, region):
        return '11305'

    def create_sql(self):
        sql = """
    INSERT INTO `apt_real_trade_price`
(`id`,
`price`,
`completion date`,
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
`region_area`,
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
%s);
"""
        return sql

    def create_param(self):
        param = (
            (
                items[0][0]['거래금액'],
                items[0][0]['건축년도'],
                items[0][0]['년'],
                items[0][0]['도로명'],

                items[0][0]['도로명건물본번호코드'],
                items[0][0]['도로명건물부번호코드'],
                items[0][0]['도로명시군구코드'],
                items[0][0]['도로명일련번호코드'],
                items[0][0]['도로명지상지하코드'],

                items[0][0]['도로명코드'],
                items[0][0]['법정동'],
                items[0][0]['법정동본번코드'],
                items[0][0]['법정동부번코드'],
                items[0][0]['법정동시군구코드'],

                items[0][0]['법정동읍면동코드'],
                items[0][0]['법정동지번코드'],
                items[0][0]['아파트'],
                items[0][0]['월'],
                items[0][0]['일'],

                items[0][0]['일련번호'],
                items[0][0]['전용면적'],
                items[0][0]['지번'],
                items[0][0]['지역코드'],
                items[0][0]['층'],
            ),
        )

        return param


# 모듈로 호출하지 않고 메인에서 호출했을 경우에만 실행
if __name__ == "__main__":
    real_price_trade = RealPriceTrade()
    param = {"region": "강북구", "date": "201803", "page_no": 2}
    real_price_trade.set_param(param)
    json_content = real_price_trade.get_content()
    content = json.loads(json_content)
    items = [content['response']['body']['items']['item']]

    result_code = content['response']['header']['resultCode']
    if result_code != "00":
        raise Exception('공공데이터 포털 통신 오류')

    '''
    num_of_rows = int(content['response']['body']['numOfRows'])
    page_no = int(content['response']['body']['pageNo'])
    total_count = int(content['response']['body']['totalCount'])
    total_page = int(math.ceil(total_count / num_of_rows))

    for i in range(2, total_page):
        param = {"region": "강북구", "date": "201803", "page_no": i}
        real_price_trade.set_param(param)
        content = json.loads(real_price_trade.get_content())
        items.append(content['response']['body']['items']['item'])
    '''

    db = Database()
    db.connect()
    pprint(items[0][0])
    sql = real_price_trade.create_sql()
    param = real_price_trade.create_param()    # for 문 돌면서 items에 있는것들 모두 받을 수 있게 바꾸기
    db.insert(sql, param)

    db.close()
    for item in items:
        pass

    # pprint(items)

    # print(item)

    #  print(search('미아동', '201802'))
    # response => body => items => item 배열에 {}로 나옴
