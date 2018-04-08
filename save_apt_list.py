from packages.db import Database
from packages.apt_list import AptList

load_code = "1130510100"  # 미아동

apt_list = AptList()
content = apt_list.get_legal_dong_apt_list(load_code)
items = apt_list.get_item_from_parsed_content(content)

db = Database()
db.connect()

sql = apt_list.create_sql()
param = apt_list.create_param(items)  # for 문 돌면서 items에 있는것들 모두 받을 수 있게 바꾸기
db.insert(sql, param)
db.close()
