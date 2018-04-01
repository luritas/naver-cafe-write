import sys
import math

from pprint import pprint

from packages.db import Database
from packages.apt_real_price_trade import AptRealPriceTrade

from datetime import datetime
from dateutil.relativedelta import relativedelta

# **************************** 실거래가 조회 시작 **************************** #
# 초기 값 설정
today_date = datetime.today()
today_month = today_date.strftime("%Y%m")
one_month_ago = (today_date - relativedelta(months=1)).strftime("%Y%m")
two_month_ago = (today_date - relativedelta(months=2)).strftime("%Y%m")
region = "걍북구"

print("실거래가를 조회합니다. 아직은 하드코딩으로 박아주세요")
print("=" * 50)

months = ("201801", "201802", "201803",)  # one_month_ago, today_month)
apt_real_price_trade = AptRealPriceTrade()
total_items = []
for month in months:
    print(str(month) + "를 조회합니다")
    content = apt_real_price_trade.get_parsed_content(region, str(month), 1, 1)
    if apt_real_price_trade.get_result_code_from_parsed_content(content) != "00":
        raise Exception('공공데이터 포털 통신 오류')

    total_count = apt_real_price_trade.get_total_count(content)
    row_per_page = 100
    total_page_no = int(math.ceil(total_count / row_per_page)) + 1
    for i in range(1, total_page_no):
        print("Page Number: " + str(i))
        content = apt_real_price_trade.get_parsed_content(region, str(month), i, row_per_page)
        items = apt_real_price_trade.get_item_from_parsed_content(content)
        for item in items:
            total_items.append(item)

db = Database()
db.connect()
sql = apt_real_price_trade.create_sql()
param = apt_real_price_trade.create_param(total_items)  # for 문 돌면서 items에 있는것들 모두 받을 수 있게 바꾸기
db.insert(sql, param)

db.close()
sys.exit()

# **************************** 실거래가 조회 끝 **************************** #
