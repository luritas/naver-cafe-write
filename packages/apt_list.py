import json
import sys
from pprint import pprint

from .open_api import OpenApi


class AptList(OpenApi):
    def __init__(self):
        super().__init__()
        self.url_name = "apt_list"
        self.load_code = None

    def get_legal_dong_apt_list(self, load_code):
        self.url_method = '/getLegaldongAptList'
        self.load_code = load_code
        return self.get_apt_list(load_code)

    def get_road_name_apt_list(self, load_code):
        self.url_method = '/getLegaldongAptList'
        return self.get_apt_list(load_code)

    def get_apt_list(self, load_code):
        self.set_param({"load_code": load_code})
        json_content = self.get_content()
        return json.loads(json_content)

    def set_param(self, parameters):
        self.param = "loadCode={0}&numOfRows=1000".format(parameters['load_code'])

    def create_sql(self):
        sql = """
INSERT INTO `naver`.`apt_list`
(
`load_code`,
`kapt_code`,
`kapt_name`)
VALUES
(
%s,
%s,
%s);
"""
        return sql

    def create_param(self, items):
        param = []
        for item in items:
            param.append(tuple([
                self.load_code,
                item['kaptCode'],
                item['kaptName'],
            ]))
        return param


if __name__ == "__main__":
    apt_list = AptList()
    load_code = "1130510100"  # 미아동
    content = apt_list.get_legal_dong_apt_list(load_code)
    items = apt_list.get_items_from_parsed_content(content)
    pprint(items)
