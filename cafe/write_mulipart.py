# cafe mulipart upload - python
import os
import sys
import requests
import urllib.request

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
    print (response.text)
else:
    print(rescode)
