# -*- coding: utf-8 -*-
# cafe mulipart upload - python
import sys
import os
import urllib
import requests
from datetime import datetime
from pprint import pprint

from packages.apt_real_price_trade import AptRealPriceTrade
from packages.apt_real_rent import AptRealRent
from packages.db import Database

db = Database()
db.connect()

apt_real_price_trade = AptRealPriceTrade()
# apt_real_rent = AptRealRent()

data_apt_trade = db.select(apt_real_price_trade.create_select_sql())
# data_apt_rent = db.select(apt_real_rent.create_select_sql())

# pprint(data_apt_trade)
# pprint(data_apt_rent)
first = {}
second = {}
third = {}
for data in list(data_apt_trade):
    try:
        first[str(data[17])].append({
            "private_area": data[21],
            "price": data[1],
            "floor": data[24]
        })
    except KeyError as ke:
        first[str(data[17])] = [{
            "private_area": data[21],
            "price": data[1],
            "floor": data[24]
        }]
    except Exception as e:
        pprint(e)

twenty_area = {}
thirty_area = {}
forty_area = {}
etc_area = {}

for index, (apt_name, apt_data) in enumerate(first.items()):
    for data in apt_data:
        try:
            if data['private_area'] < 60:
                twenty_area[apt_name].append("%s(%d층)" % (data['price'], data['floor']))
            elif data['private_area'] < 85:
                thirty_area[apt_name].append("%s(%d층)" % (data['price'], data['floor']))
            elif data['private_area'] < 120:
                forty_area[apt_name].append("%s(%d층)" % (data['price'], data['floor']))
            else:
                etc_area[apt_name].append("%s(%d층)" % (data['price'], data['floor']))
        except KeyError as ke:
            if data['private_area'] < 60:
                twenty_area[apt_name] = ["%s(%d층)" % (data['price'], data['floor'])]
            elif data['private_area'] < 85:
                thirty_area[apt_name] = ["%s(%d층)" % (data['price'], data['floor'])]
            elif data['private_area'] < 120:
                forty_area[apt_name] = ["%s(%d층)" % (data['price'], data['floor'])]
            else:
                etc_area[apt_name] = ["%s(%d층)" % (data['price'], data['floor'])]
        except Exception as e:
            pprint(e)

# content += "{0:=<15} | {1:=^10} | {2:=^10}".format(apt, )

content = "{0:<20} | {1:^15} | {2:^15} | {3:^15} | {4:^15}\n".format("아파트/평형", "20평", "30평", "40평", "40평 초과")
content += "{0:-<15} | {1:-^16} | {2:-^16} | {3:-^16} | {4:-^16}\n".format("", "", "", "", "")
content = """
<table>
    <thead>
        <tr>
            <td>아파트/평형</td>
            <td>20평</td>
            <td>30평</td>
            <td>40평</td>
            <td>40평 초과</td>
        </tr>
    </thead>
    <tbody>
"""
for apt_name in first:
    try:
        len_twenty_area = len(twenty_area[apt_name])
    except Exception as e:
        len_twenty_area = 0
    try:
        len_thirty_area = len(thirty_area[apt_name])
    except Exception as e:
        len_thirty_area = 0
    try:
        len_forty_area = len(forty_area[apt_name])
    except Exception as e:
        len_forty_area = 0
    try:
        len_etc_area = len(etc_area[apt_name])
    except Exception as e:
        len_etc_area = 0
    for i in range(0, max(len_twenty_area, len_thirty_area, len_forty_area, len_etc_area)):
        try:
            temp_twenty_area = twenty_area[apt_name][i]
        except Exception as e:
            temp_twenty_area = ''
        try:
            temp_thirty_area = thirty_area[apt_name][i]
        except Exception as e:
            temp_thirty_area = ''
        try:
            temp_forty_area = forty_area[apt_name][i]
        except Exception as e:
            temp_forty_area = ''
        try:
            temp_etc_area = etc_area[apt_name][i]
        except Exception as e:
            temp_etc_area = ''
        if i != 0:
            apt_name_title = ''
        else:
            apt_name_title = apt_name
        if temp_twenty_area == '' and temp_thirty_area == '' and temp_forty_area == '' and temp_etc_area == '':
            pprint('건너뛰기!!!!!!!!!!!!!!!!!!')
            continue
        content += """
        <tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>
            <td>{4}</td>
        </tr>
        """.format(apt_name_title, temp_twenty_area, temp_thirty_area, temp_forty_area, temp_etc_area)

content += "</tbody></table>"
# print(content)
"""
    title = ""
    content = "{0:=<15} | {1:=^10} | {2:=^10} \n".format("아파트/평형", "20평", "30평")
    for (key, value) in first.items():
        title += "2018년 " + key + "월 실거래가"
    for (key1, value1) in value.items():
        content += "{0:=<15} | {1:=^10} | {2:=^10}".format(key1, value1['private_area'], value1['floor'])

    print(content)
"""

# raw[str(data[18])][str(data[17])] = data[21]
# raw[str(data[18])][str(data[17])] = data[24]


# TODO 우선 아파트 실거래가를 유의미하게 던져주기!! 예를 들면 1월 2월 각각 아파트 거래량 표기 미아뉴타운이 위로 보이고 아래는 그 이외의 것들
# TODO 두산트레지움       삼성트리베라2차        삼성트리베라1차        SK뷰         삼각산아이원      송천센트레빌1차    송천센트레빌 2차
# TODO 미아뉴타운 하면 길음뉴타운까지 같이하기

sql = "select * from tokens order by expires_at desc limit 1"
rows = db.select(sql)
# Connection 닫기
db.close()

today = datetime.now().strftime('%Y.%m.%d')

token = rows[0][1]
header = "Bearer " + token  # Bearer 다음에 공백 추가
clubid = os.environ.get("CLUB_ID")  # 카페의 고유 ID값
menuid = os.environ.get("MENU_ID")  # (상품게시판은 입력 불가)
url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"
subject = urllib.parse.quote("[{0}]미아동 국토부 실거래가".format(today))
content = urllib.parse.quote(content)
data = {'subject': subject, 'content': content}
files = [
    # ('image', ('YOUR_FILE_1', open('YOUR_FILE_1', 'rb'), 'image/jpeg', {'Expires': '0'})),
    # ('image', ('YOUR_FILE_2', open('YOUR_FILE_2', 'rb'), 'image/jpeg', {'Expires': '0'}))
]
headers = {'Authorization': header}
response = requests.post(url, headers=headers, data=data, files=files)
pprint(response.text)

rescode = response.status_code
if (rescode == 200):
    print(response.text)
else:
    print(rescode)