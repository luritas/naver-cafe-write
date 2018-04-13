# -*- coding: utf-8 -*-
# cafe mulipart upload - python
import sys, getopt
import os
import urllib
import requests
from datetime import datetime
from pprint import pprint

from packages.apt_maintenance_personal import AptMaintenancePersonal
from packages.apt_maintenance_common import AptMaintenanceCommon
from packages.apt_real_price_trade import AptRealPriceTrade
from packages.db import Database
from packages.naver_cafe_write import NaverCafeWrite


def write_trade_price(argv: object) -> object:
    db = Database()
    db.connect()

    # TODO 월별로 실거래가와 거래건수를 따로 글써서 보여주기
    try:
        year = argv[1]
        start_month = argv[2]
        end_month = argv[3]
    except Exception as e:
        pprint("usage: python write_multipart.py {year} {month} [,{'send'}]")
        print(e)
        sys.exit()

    apt_real_price_trade = AptRealPriceTrade()
    data_apt_trade = db.select(
        apt_real_price_trade.create_select_sql(int(year), int(start_month), int(end_month),
                                               apt_real_price_trade.get_region_code('000')))
    db.close()
    # TODO 전월세 자료
    # apt_real_rent = AptRealRent()
    # data_apt_rent = db.select(apt_real_rent.create_select_sql())

    items = apt_real_price_trade.parse_data(data_apt_trade)
    apt_real_price_trade.set_area_data()  # 평수별로 데이터 나누기
    html = apt_real_price_trade.get_contents()

    print(argv)
    f = open('index.html', 'w')
    f.write(html.get("count", ''))
    f.write("=" * 100)
    f.write(html.get("price", ''))
    f.close()

    # TODO 우선 아파트 실거래가를 유의미하게 던져주기!! 예를 들면 1월 2월 각각 아파트 거래량 표기 미아뉴타운이 위로 보이고 아래는 그 이외의 것들
    # TODO 미아뉴타운 하면 길음뉴타운까지 같이하기

    if len(argv) > 4 and argv[4] == "send":
        today = datetime.now().strftime('%Y.%m.%d')

        subject = "[{0} 기준] {1}년 {2}월 성북구 국토부 실거래가".format(today, year, end_month)
        # data = {'subject': subject, 'content': html['price']}
        files = [
            # ('image', ('YOUR_FILE_1', open('YOUR_FILE_1', 'rb'), 'image/jpeg', {'Expires': '0'})),
            # ('image', ('YOUR_FILE_2', open('YOUR_FILE_2', 'rb'), 'image/jpeg', {'Expires': '0'}))
        ]
        naver_cafe_write = NaverCafeWrite()
        content = html.get("count", '') + html.get("price", '')
        response = naver_cafe_write.write_article_to_naver_cafe(subject, content, files)

        pprint("카페 전송 완료!!!!")
        pprint(response.text)


def write_maintenance_price(argv):
    apt_maintenance_common = AptMaintenanceCommon()
    common_category = apt_maintenance_common.get_category()
    apt_maintenance_personal = AptMaintenancePersonal()
    personal_cateogry = apt_maintenance_personal.get_category()
    # TODO personal 파싱하기

    db = Database()
    db.connect()
    load_code = "1130510100"  # 미아동
    search_date = "201801"
    sql = apt_maintenance_common.get_all_data_query(load_code, search_date)
    maintenance_common = db.select(sql)
    sql = apt_maintenance_personal.get_all_data_query(load_code, search_date)
    # sql = apt_maintenance_personal.get_
    db.close()
    for fee in maintenance_common:
        data = {
            "id": fee[0],
            common_category["load_code"]: fee[1],
            common_category["kaptCode"]: fee[2],
            common_category["kaptName"]: fee[3],
            common_category["searchDate"]: fee[4],
            common_category["pay"]: fee[5],
            common_category["sundryCost"]: fee[6],
            common_category["bonus"]: fee[7],
            common_category["pension"]: fee[8],
            common_category["accidentPremium"]: fee[9],
            common_category["employPremium"]: fee[10],
            common_category["nationalPension"]: fee[11],
            common_category["healthPremium"]: fee[12],
            common_category["welfareBenefit"]: fee[13],
            common_category["officeSupply"]: fee[14],
            common_category["bookSupply"]: fee[15],
            common_category["transportCost"]: fee[16],
            common_category["telCost"]: fee[17],
            common_category["postageCost"]: fee[18],
            common_category["taxrestCost"]: fee[19],
            common_category["clothesCost"]: fee[20],
            common_category["eduCost"]: fee[21],
            common_category["fuelCost"]: fee[22],
            common_category["refairCost"]: fee[23],
            common_category["carInsurance"]: fee[24],
            common_category["carEtc"]: fee[25],
            common_category["careItemCost"]: fee[26],
            common_category["accountingCost"]: fee[27],
            common_category["hiddenCost"]: fee[28],
            common_category["cleanCost"]: fee[29],
            common_category["guardCost"]: fee[30],
            common_category["disinfCost"]: fee[31],
            common_category["elevCost"]: fee[32],
            common_category["hnetwCost"]: fee[33],
            common_category["lrefCost1"]: fee[34],
            common_category["lrefCost2"]: fee[35],
            common_category["lrefCost3"]: fee[36],
            common_category["lrefCost4"]: fee[37],
            common_category["manageCost"]: fee[38]
        }


# 국토부 아파트 실거래가 글쓰기
if sys.argv[0] == 'trade':
    write_trade_price(sys.argv)
elif sys.argv[0] == 'maintenance' or True:
    write_maintenance_price(sys.argv)
