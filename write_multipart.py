# -*- coding: utf-8 -*-
# cafe mulipart upload - python
import sys, getopt
import os
import urllib
import requests
from datetime import datetime
from pprint import pprint

from packages.apt_list import AptList
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
    apt_list = AptList()
    apt_maintenance_common = AptMaintenanceCommon()
    apt_maintenance_personal = AptMaintenancePersonal()
    # TODO personal 파싱하기

    db = Database()
    db.connect()
    load_code = "1130510100"  # 미아동
    search_date = "201801"
    sql = apt_list.get_all_list_query(load_code)
    apt_list_by_load_code = db.select(sql)
    sql = apt_maintenance_common.get_all_data_query(load_code, search_date)
    maintenance_common = db.select(sql)
    sql = apt_maintenance_personal.get_all_data_query(load_code, search_date)
    maintenance_personal = db.select(sql)
    common_category = apt_maintenance_common.get_category()
    personal_category = apt_maintenance_personal.get_category()

    # sql = apt_maintenance_personal.get_
    db.close()
    common = {}
    for index in range(0, len(maintenance_common)):
        common.setdefault(maintenance_common[index][2], {
            "id": maintenance_common[index][0],
            common_category["load_code"]: maintenance_common[index][1],
            # common_category["kaptCode"]: maintenance_common[index][2],
            common_category["kaptName"]: maintenance_common[index][3],
            common_category["searchDate"]: maintenance_common[index][4],
            common_category["pay"]: maintenance_common[index][5],
            common_category["sundryCost"]: maintenance_common[index][6],
            common_category["bonus"]: maintenance_common[index][7],
            common_category["pension"]: maintenance_common[index][8],
            common_category["accidentPremium"]: maintenance_common[index][9],
            common_category["employPremium"]: maintenance_common[index][10],
            common_category["nationalPension"]: maintenance_common[index][11],
            common_category["healthPremium"]: maintenance_common[index][12],
            common_category["welfareBenefit"]: maintenance_common[index][13],
            common_category["officeSupply"]: maintenance_common[index][14],
            common_category["bookSupply"]: maintenance_common[index][15],
            common_category["transportCost"]: maintenance_common[index][16],
            common_category["telCost"]: maintenance_common[index][17],
            common_category["postageCost"]: maintenance_common[index][18],
            common_category["taxrestCost"]: maintenance_common[index][19],
            common_category["clothesCost"]: maintenance_common[index][20],
            common_category["eduCost"]: maintenance_common[index][21],
            common_category["fuelCost"]: maintenance_common[index][22],
            common_category["refairCost"]: maintenance_common[index][23],
            common_category["carInsurance"]: maintenance_common[index][24],
            common_category["carEtc"]: maintenance_common[index][25],
            common_category["careItemCost"]: maintenance_common[index][26],
            common_category["accountingCost"]: maintenance_common[index][27],
            common_category["hiddenCost"]: maintenance_common[index][28],
            common_category["cleanCost"]: maintenance_common[index][29],
            common_category["guardCost"]: maintenance_common[index][30],
            common_category["disinfCost"]: maintenance_common[index][31],
            common_category["elevCost"]: maintenance_common[index][32],
            common_category["hnetwCost"]: maintenance_common[index][33],
            common_category["lrefCost1"]: maintenance_common[index][34],
            common_category["lrefCost2"]: maintenance_common[index][35],
            common_category["lrefCost3"]: maintenance_common[index][36],
            common_category["lrefCost4"]: maintenance_common[index][37],
            common_category["manageCost"]: maintenance_common[index][38]
        })

    personal = {}
    for index in range(0, len(maintenance_personal)):
        personal.setdefault(maintenance_personal[index][2], {
            personal_category["searchDate"]: maintenance_personal[index][0],
            personal_category["heatC"]: maintenance_personal[index][0],
            personal_category["heatP"]: maintenance_personal[index][0],
            personal_category["waterHotC"]: maintenance_personal[index][0],
            personal_category["waterHotP"]: maintenance_personal[index][0],
            personal_category["gasC"]: maintenance_personal[index][0],
            personal_category["gasP"]: maintenance_personal[index][0],
            personal_category["electC"]: maintenance_personal[index][0],
            personal_category["electP"]: maintenance_personal[index][0],
            personal_category["waterCoolC"]: maintenance_personal[index][0],
            personal_category["waterCoolP"]: maintenance_personal[index][0],
            personal_category["purifi"]: maintenance_personal[index][0],
            personal_category["scrap"]: maintenance_personal[index][0],
            personal_category["preMeet"]: maintenance_personal[index][0],
            personal_category["buildInsu"]: maintenance_personal[index][0],
            personal_category["electionMng"]: maintenance_personal[index][0]
        })

    merged_data = []
    for apt in apt_list_by_load_code:
        code = apt[2]
        merged_data.append({
            **common[code], **personal[code]
        })
    pprint(merged_data)
    sys.exit()


# 국토부 아파트 실거래가 글쓰기
if sys.argv[0] == 'trade':
    write_trade_price(sys.argv)
elif sys.argv[0] == 'maintenance' or True:
    write_maintenance_price(sys.argv)
