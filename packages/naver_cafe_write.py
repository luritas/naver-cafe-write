import sys
import os
import urllib
import requests

from pprint import pprint
from packages.db import Database


class NaverCafeWrite:

    def __init__(self):
        self.db = Database()
        self.token = self.get_token()

    def get_token(self):
        self.db.connect()
        sql = "select * from tokens order by expires_at desc limit 1"
        rows = self.db.select(sql)
        # Connection 닫기
        self.db.close()
        return rows[0][1]

    def write_article_to_naver_cafe(self, subject, content, files):
        header = "Bearer " + self.token  # Bearer 다음에 공백 추가
        club_id = os.environ.get("CLUB_ID")  # 카페의 고유 ID값
        menu_id = os.environ.get("MENU_ID")  # (상품게시판은 입력 불가)
        url = "https://openapi.naver.com/v1/cafe/" + club_id + "/menu/" + menu_id + "/articles"
        subject = urllib.parse.quote(subject)
        content = urllib.parse.quote(content)
        data = {'subject': subject, 'content': content}
        headers = {'Authorization': header}
        response = requests.post(url, headers=headers, data=data, files=files)
        res_code = response.status_code
        if res_code == 200:
            return response
        else:
            pprint(response)
            raise Exception('네이버 카페 통신실패')
