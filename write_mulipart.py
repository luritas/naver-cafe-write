# cafe mulipart upload - python
import os
import sys
import math
# import requests
import urllib.request

from packages.db import Database
from packages.apt_real_price_trade import AptRealPriceTrade

from datetime import datetime
from dateutil.relativedelta import relativedelta

# **************************** 실거래가 조회 시작 **************************** #
today_date = datetime.today()
today_month = today_date.strftime("%Y%m")
one_month_ago = (today_date - relativedelta(months=1)).strftime("%Y%m")
two_month_ago = (today_date - relativedelta(months=2)).strftime("%Y%m")

print(two_month_ago + " 이후의 실거래가를 조회합니다")
print("=" * 50)

months = (two_month_ago, one_month_ago, today_month)
apt_real_price_trade = AptRealPriceTrade()
total_items = []
for month in months:
    print(str(month) + "를 조회합니다")
    content = apt_real_price_trade.get_parsed_content('강북구', str(month), 1, 1)
    if apt_real_price_trade.get_result_code_from_parsed_content(content) != "00":
        raise Exception('공공데이터 포털 통신 오류')

    total_count = apt_real_price_trade.get_total_count(content)
    row_per_page = 10
    total_page_no = int(math.ceil(total_count / row_per_page)) + 1
    for i in range(1, total_page_no):
        print("Page Number: " + str(i))
        content = apt_real_price_trade.get_parsed_content('강북구', str(month), i, row_per_page)
        items = apt_real_price_trade.get_items_from_parsed_content(content)
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

token = os.environ.get("TOKEN")
header = "Bearer " + token  # Bearer 다음에 공백 추가
clubid = os.environ.get("CLUB_ID")  # 카페의 고유 ID값
menuid = os.environ.get("MENU_ID")  # (상품게시판은 입력 불가)
url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"
subject = urllib.parse.quote("네이버 Cafe api Test Python")
content = urllib.parse.quote(
    "<font color='red'>python multi-part</font>로 첨부한 글입니다. <br> python 이미지 첨부 <br> <img src='#0' />")
data = {'subject': subject, 'content': content}
files = [
    # ('image', ('YOUR_FILE_1', open('YOUR_FILE_1', 'rb'), 'image/jpeg', {'Expires': '0'})),
    # ('image', ('YOUR_FILE_2', open('YOUR_FILE_2', 'rb'), 'image/jpeg', {'Expires': '0'}))
]
headers = {'Authorization': header}
response = requests.post(url, headers=headers, data=data, files=files)

rescode = response.status_code
if (rescode == 200):
    print(response.text)
else:
    print(rescode)