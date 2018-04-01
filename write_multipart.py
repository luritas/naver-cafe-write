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

db = Database()
db.connect()

# TODO 월별로 실거래가와 거래건수를 따로 글써서 보여주기
try:
    year = sys.argv[1]
    start_month = sys.argv[2]
    end_month = sys.argv[3]
except Exception as e:
    pprint("usage: python write_multipart.py {year} {month} [,{'send'}]")
    print(e)
    sys.exit()

apt_real_price_trade = AptRealPriceTrade()
data_apt_trade = db.select(
    apt_real_price_trade.create_select_sql(int(year), int(start_month), int(end_month),
                                           apt_real_price_trade.get_region_code('000')))

# TODO 전월세 자료
# apt_real_rent = AptRealRent()
# data_apt_rent = db.select(apt_real_rent.create_select_sql())

items = apt_real_price_trade.parse_data(data_apt_trade)
apt_real_price_trade.set_area_data()  # 평수별로 데이터 나누기
html = apt_real_price_trade.get_contents()

print(sys.argv)
f = open('index.html', 'w')
f.write(html.get("count", ''))
f.write("=" * 100)
f.write(html.get("price", ''))
f.close()

# TODO 우선 아파트 실거래가를 유의미하게 던져주기!! 예를 들면 1월 2월 각각 아파트 거래량 표기 미아뉴타운이 위로 보이고 아래는 그 이외의 것들
# TODO 미아뉴타운 하면 길음뉴타운까지 같이하기

if len(sys.argv) > 4 and sys.argv[4] == "send":
    today = datetime.now().strftime('%Y.%m.%d')

    subject = "[{0} 기준] {1}년 {2}월 성북구 국토부 실거래가".format(today, year, end_month)
    data = {'subject': subject, 'content': html['price']}
    files = [
        # ('image', ('YOUR_FILE_1', open('YOUR_FILE_1', 'rb'), 'image/jpeg', {'Expires': '0'})),
        # ('image', ('YOUR_FILE_2', open('YOUR_FILE_2', 'rb'), 'image/jpeg', {'Expires': '0'}))
    ]
    naver_cafe_write = NaverCafeWrite()
    content = html.get("count", '') + html.get("price", '')
    response = naver_cafe_write.write_article_to_naver_cafe(subject, content, files)

    pprint("카페 전송 완료!!!!")
    pprint(response.text)
