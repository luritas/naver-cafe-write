import sys

from packages.db import Database
from packages.apt_maintenance_common import AptMaintenanceCommon
from pprint import pprint

load_code = "1130510100"  # 미아동
db = Database()
db.connect()

sql = """
SELECT 
    `kapt_code`
FROM
    naver.apt_list
WHERE
    load_code = '%s';
""" % (load_code)
kapt_codes = db.select(sql)

for kapt_code in kapt_codes:
    search_date = "201801"

    apt_maintenance_common = AptMaintenanceCommon()
    items = apt_maintenance_common.merge_all_data(kapt_code[0], search_date)

    sql = apt_maintenance_common.create_sql()
    param = apt_maintenance_common.create_param(items, load_code, search_date)  # for 문 돌면서 items에 있는것들 모두 받을 수 있게 바꾸기

    db.insert(sql, param)
db.close()
