# -*- coding: utf-8 -*-
# cafe mulipart upload - python
import sys, getopt
import os
import urllib
import requests
from datetime import datetime
from pprint import pprint

from packages.apt_real_price_trade import AptRealPriceTrade
from packages.apt_real_rent import AptRealRent
from packages.db import Database
from packages.naver_cafe_write import NaverCafeWrite
from packages.apt_maintenance_common import AptMaintenanceCommon


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
    category = apt_maintenance_common.get_common_category()
    category.update(apt_maintenance_common.get_hsmp_labor_cost_category())
    category.update(apt_maintenance_common.get_hsmp_ofcrk_cost_category())
    category.update(apt_maintenance_common.get_hsmp_taxdue_category())
    category.update(apt_maintenance_common.get_hsmp_clothing_cost_category())
    category.update(apt_maintenance_common.get_hsmp_edu_traing_cost_category())
    category.update(apt_maintenance_common.get_hsmp_vhcle_mntnc_cost_category())
    category.update(apt_maintenance_common.get_hsmp_etc_cost_category())
    category.update(apt_maintenance_common.get_hsmp_cleaning_cost_category())
    category.update(apt_maintenance_common.get_hsmp_guard_cost_category())
    category.update(apt_maintenance_common.get_hsmp_disinfection_cost_category())
    category.update(apt_maintenance_common.get_hsmp_elevator_mntnc_cost_category())
    category.update(apt_maintenance_common.get_hsmp_home_network_mntnc_cost_category())
    category.update(apt_maintenance_common.get_hsmp_repairs_cost_category())
    category.update(apt_maintenance_common.get_hsmp_facility_mntnc_cost_category())
    category.update(apt_maintenance_common.get_hsmp_safety_check_up_cost_category())
    category.update(apt_maintenance_common.get_hsmp_disaster_prevention_cost_category())
    category.update(apt_maintenance_common.get_hsmp_consign_manage_fee_category())

    db = Database()
    db.connect()
    load_code = "1130510100"  # 미아동
    search_date = "201801"
    sql = apt_maintenance_common.get_all_data_query(load_code, search_date)
    maintenance_common = db.select(sql)
    for fee in maintenance_common:
        data = {
            "id": fee[0],
            category["load_code"]: fee[1],
            category["kaptCode"]: fee[2],
            category["kaptName"]: fee[3],
            category["searchDate"]: fee[4],
            category["pay"]: fee[5],
            category["sundryCost"]: fee[6],
            category["bonus"]: fee[7],
            category["pension"]: fee[8],
            category["accidentPremium"]: fee[9],
            category["employPremium"]: fee[10],
            category["nationalPension"]: fee[11],
            category["healthPremium"]: fee[12],
            category["welfareBenefit"]: fee[13],
            category["officeSupply"]: fee[14],
            category["bookSupply"]: fee[15],
            category["transportCost"]: fee[16],
            category["telCost"]: fee[17],
            category["postageCost"]: fee[18],
            category["taxrestCost"]: fee[19],
            category["clothesCost"]: fee[20],
            category["eduCost"]: fee[21],
            category["fuelCost"]: fee[22],
            category["refairCost"]: fee[23],
            category["carInsurance"]: fee[24],
            category["carEtc"]: fee[25],
            category["careItemCost"]: fee[26],
            category["accountingCost"]: fee[27],
            category["hiddenCost"]: fee[28],
            category["cleanCost"]: fee[29],
            category["guardCost"]: fee[30],
            category["disinfCost"]: fee[31],
            category["elevCost"]: fee[32],
            category["hnetwCost"]: fee[33],
            category["lrefCost1"]: fee[34],
            category["lrefCost2"]: fee[35],
            category["lrefCost3"]: fee[36],
            category["lrefCost4"]: fee[37],
            category["manageCost"]: fee[38]
        }

    db.close()


# 국토부 아파트 실거래가 글쓰기
if sys.argv[0] == 'trade':
    write_trade_price(sys.argv)
elif sys.argv[0] == 'maintenance' or True:
    write_maintenance_price(sys.argv)
