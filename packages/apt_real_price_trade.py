# 아파트 실거래가 조회
# http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?LAWD_CD=11305&DEAL_YMD=201803&pageNo=1&serviceKey=uSBGVwdHO%2Bf7zwY%2B7LSMMKwDTrmKkc9pT429CFbwuCeq2vkJmm9EXG1G5DtpiPFGN8m%2BTD4ykq0YVR%2FjXLXinw%3D%3D

import json
import math
import sys
from pprint import pprint
import urllib.request
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict

from packages.open_api import OpenApi
from packages.db import Database


class AptRealPriceTrade(OpenApi):

    def __init__(self):
        super().__init__()
        self.url_name = "apt_real_price_trade"
        self.param = None
        self.twenty_area = {}
        self.thirty_area = {}
        self.forty_area = {}
        self.etc_area = {}

    def set_param(self, param):
        region_code = urllib.parse.quote(self.__get_region_code(param['region']))
        self.param = "LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}&pageNo={page_no}&numOfRows={row_per_page}" \
            .format(LAWD_CD=region_code, DEAL_YMD=param['date'], page_no=param['page_no'],
                    row_per_page=param['row_per_page'])

    def save_database_from_open_api(self, item):
        pass

    def __get_region_code(self, region):
        return '11305'

    def create_select_sql(self, year, month):
        return """
SELECT 
    `apt_real_trade_price`.`id`,
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
FROM
    `naver`.`apt_real_trade_price`
WHERE
    `apt_name` IN (SELECT 
            `a`.`apt_name`
        FROM
            `naver`.`apt_real_trade_price` `a`
        WHERE
            `year` = %d
            AND `month` = %d
        GROUP BY `a`.`apt_name`
        HAVING COUNT(`a`.`apt_name`) > 5)
        AND `year` = %d
        AND `month` = %d
ORDER BY FIELD(apt_name,
        '벽산라이브파크',
        '삼각산아이원',
        '송천센트레빌',
        '미아동부센트레빌',
        '래미안트리베라1단지',
        '두산위브트레지움',
        '삼성래미안트리베라2단지',
        '에스케이북한산시티') DESC, `price` DESC;
""" % (year, month, year, month)

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

    def parse_data(self, data_apt_trade):
        self.set_parse_korean_real_estate_api(data_apt_trade)
        return self.items

    def set_parse_korean_real_estate_api(self, data_apt_trade):
        pared_data_apt_trade = {}
        for data in list(data_apt_trade):
            try:
                pared_data_apt_trade[str(data[17])].append({
                    "private_area": data[21],
                    "price": data[1],
                    "floor": data[24]
                })
            except KeyError as ke:
                pared_data_apt_trade[str(data[17])] = [{
                    "private_area": data[21],
                    "price": data[1],
                    "floor": data[24]
                }]
            except Exception as e:
                raise Exception(e)
        self.items = pared_data_apt_trade

    def set_area_data(self):
        for index, (apt_name, apt_data) in enumerate(self.items.items()):
            for data in apt_data:
                try:
                    if data['private_area'] < 60:
                        self.twenty_area.setdefault(apt_name, []).append(
                            "%s(%d층)" % (data['price'], data['floor']))
                    elif data['private_area'] < 85:
                        self.thirty_area.setdefault(apt_name, []).append(
                            "%s(%d층)" % (data['price'], data['floor']))
                    elif data['private_area'] < 120:
                        self.forty_area.setdefault(apt_name, []).append(
                            "%s(%d층)" % (data['price'], data['floor']))
                    else:
                        self.etc_area.setdefault(apt_name, []).append(
                            "%s(%d층)" % (data['price'], data['floor']))
                except Exception as e:
                    raise Exception(e)

    def get_contents(self):
        html_price = html_count = """
        <table>
            <thead>
                <tr>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>아파트/평형</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>20평</th>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>30평</th>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>40평</th>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>40평 초과</th>
                </tr>
            </thead>
            <tbody>
        """
        distinct_row = 0
        for apt_name in self.items:
            len_twenty_area = len(self.twenty_area.setdefault(apt_name, []))
            len_thirty_area = len(self.thirty_area.setdefault(apt_name, []))
            len_forty_area = len(self.forty_area.setdefault(apt_name, []))
            len_etc_area = len(self.etc_area.setdefault(apt_name, []))
            distinct_row += 1
            for i in range(0, max(len_twenty_area, len_thirty_area, len_forty_area, len_etc_area)):
                temp_twenty_area = i < len_twenty_area and self.twenty_area[apt_name][i] or ""
                temp_thirty_area = i < len_thirty_area and self.thirty_area[apt_name][i] or ""
                temp_forty_area = i < len_forty_area and self.forty_area[apt_name][i] or ""
                temp_etc_area = i < len_etc_area and self.etc_area[apt_name][i] or ""
                apt_name_title = i == 0 and apt_name or ''
                if temp_twenty_area + temp_thirty_area + temp_forty_area + temp_etc_area == "":
                    pprint('건너뛰기!!!!!!!!!!!!!!!!!!')
                    continue
                bgcolor = distinct_row % 2 == 1 and "background-color: #ddd;" or ""
                html_price += """
                <tr style='{5}'>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{0}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{1}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{2}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{3}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{4}</td>
                </tr>
                """.format(apt_name_title, temp_twenty_area, temp_thirty_area, temp_forty_area, temp_etc_area, bgcolor)
                # 20평, 30평, 40평 등 각각수 세서 총합에 넣어주기!!!
            html_count += """
            <tr style='{5}'>
                <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{0}</td>
                <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top; text-align: center;'>{1} 건</td>
                <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top; text-align: center;'>{2} 건</td>
                <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top; text-align: center;'>{3} 건</td>
                <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top; text-align: center;'>{4} 건</td>
            </tr>
            """.format(apt_name, len_twenty_area, len_thirty_area, len_forty_area,
                       len_twenty_area + len_thirty_area + len_forty_area, bgcolor)

        html_price += "</tbody></table>"
        html_count += "</tbody></table> <hr>"
        count_table = html_count.replace("40평 초과", "총거래(40평 이상 제외)")
        return {
            'price': html_price,
            'count': count_table
        }


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
