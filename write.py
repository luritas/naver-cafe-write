# cafe mulipart upload - python
import os
import sys
import requests
import urllib.request
import datetime
import json
import db
from search import news

# SQL문 실행
connect = db.connect()
curs = connect.cursor()
sql = "select * from tokens order by expires_at desc limit 1"
curs.execute(sql)
 
# 데이타 Fetch
rows = curs.fetchall()
# Connection 닫기
connect.close()

token = rows[0][1];
news = news.search('강북')
# print("token: " + token)
json_data = news
data = json.loads(json_data)
article = ''
now = datetime.datetime.now()
for item in data['items']:
#    if (item['pubDate'])
#        continue
    title = now.strftime('[%Y.%m.%d]') + ' 오늘의 뉴스'
    article += item['title'] + '<br>' + '원문링크: ' + item['link'] + '<br><br>' # item['description']

header = "Bearer " + token  # Bearer 다음에 공백 추가
clubid = os.environ.get("CLUB_ID")  # 카페의 고유 ID값
menuid = os.environ.get("MENU_ID")  # (상품게시판은 입력 불가)
url = "https://openapi.naver.com/v1/cafe/" + clubid + "/menu/" + menuid + "/articles"
subject = urllib.parse.quote(title)
content = urllib.parse.quote(article)
data = {"subject":  subject, "content" : content}
files = []
headers = {'Authorization': header }
response = requests.post(url, headers=headers, data=data, files=files)

rescode = response.status_code
if(rescode==200):
    print (response.text)
else:
    print(rescode)
       
