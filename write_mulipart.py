# cafe mulipart upload - python
import os
import sys
import requests
import urllib.request

from pprint import pprint
from packages.db import Database

from packages.apt_real_price_trade import AptRealPriceTrade
from packages.apt_real_rent import AptRealRent

db = Database()
db.connect()

# SQL문 실행
apt_real_price_trade = AptRealPriceTrade()
apt_real_rent = AptRealRent()

data_apt_trade = db.select(apt_real_price_trade.create_select_sql())
data_apt_rent = db.select(apt_real_rent.create_select_sql())

pprint(data_apt_trade)
pprint(data_apt_rent)

# TODO 우선 아파트 실거래가를 유의미하게 던져주기!! 예를 들면 1월 2월 각각 아파트 거래량 표기 미아뉴타운이 위로 보이고 아래는 그 이외의 것들
# TODO 두산트레지움       삼성트리베라2차        삼성트리베라1차        SK뷰         삼각산아이원      송천센트레빌1차    송천센트레빌 2차
# TODO 미아뉴타운 하면 길음뉴타운까지 같이하기

db.close()
sys.exit()

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
