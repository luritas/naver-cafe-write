import os
import sys
import json
from pprint import pprint

import xmltodict
import urllib.request


class OpenApi:

    def __init__(self):
        # self.service_key = {
        #     "apt_real_price_trade": os.environ.get("OPEN_API_SERVICE_KEY"),
        #     "apt_real_rent": os.environ.get("OPEN_API_SERVICE_KEY"),
        #     "apt_list": os.environ.get("OPEN_API_SERVICE_KEY"),
        #     "apt_maintenance_common": os.environ.get("OPEN_API_SERVICE_KEY")
        # }
        self.service_key = os.environ.get("APT_TRADE_SERVICE_KEY")
        self.hostname1 = "http://openapi.molit.go.kr"
        self.hostname2 = "http://apis.data.go.kr"
        self.urls = {
            "apt_real_price_trade": self.hostname1 + "/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/"
                                                     "getRTMSDataSvcAptTradeDev",
            "apt_real_rent": self.hostname1 + ":8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/"
                                              "getRTMSDataSvcAptRent",
            "apt_list": self.hostname2 + "/1611000/AptListService",
            "apt_maintenance_common": self.hostname2 + "/1611000/AptCmnuseManageCostService",
            "apt_maintenance_personal": self.hostname2 + "/1611000/AptIndvdlzManageCostService",
        }
        self.url_name = None
        self.url_method = None
        self.param = None

    def set_param(self, parameters):
        raise Exception("set_param 메서드를 구현해주세요")

    def save_database_from_open_api(self):
        raise Exception("save_database_from_open_api 메서드를 구현해주세요")

    def get_content(self):
        url = self.urls[self.url_name] + self.url_method
        self.param += "&serviceKey={SERVICE_KEY}".format(SERVICE_KEY=self.service_key)  # add service_key
        full_url = url + "?" + self.param
        print(self.url_name)
        print(full_url)
        # sys.exit()
        request = urllib.request.Request(full_url)
        response = urllib.request.urlopen(request)
        res_code = response.getcode()
        if res_code == 200:
            response_body = response.read()
            content = xmltodict.parse(response_body.decode('utf-8'))
            return json.dumps(content)
        else:
            return "Error Code:" + res_code

    def get_body_from_parsed_content(self, content):
        return content['response']['body']

    def get_header_from_parsed_content(self, content):
        return content['response']['header']

    def get_only_item_from_parsed_content(self, content):
        try:
            return self.get_body_from_parsed_content(content)['item']
        except Exception as e:
            print(e)
            sys.exit()

    def get_items_from_parsed_content(self, content):
        try:
            return self.get_body_from_parsed_content(content)['items']
        except Exception as e:
            print(e)
            sys.exit()

    def get_item_from_parsed_content(self, content):
        try:
            return self.get_items_from_parsed_content(content)['item']
        except Exception as e:
            print(e)
            sys.exit()

    def get_result_code_from_parsed_content(self, content):
        return self.get_header_from_parsed_content(content)['resultCode']

    def get_total_count(self, content):
        return int(self.get_body_from_parsed_content(content)['totalCount'])
