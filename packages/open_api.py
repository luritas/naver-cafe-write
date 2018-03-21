import os
import sys
import json
import xmltodict
import urllib.request


class OpenApi:

    def __init__(self):
        self.service_key = os.environ.get("APT_TRADE_SERVICE_KEY")
        self.hostname = "http://openapi.molit.go.kr"
        self.urls = {
            "apt_real_price_trade": self.hostname + "/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/"
                                                "getRTMSDataSvcAptTradeDev",
            "apt_real_rent": self.hostname + ":8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/"
                                             "getRTMSDataSvcAptRent"
        }
        self.url_name = None
        self.param = None

    def set_param(self, parameters):
        raise Exception("set_param 메서드를 구현해주세요")

    def save_database_from_open_api(self):
        raise Exception("save_database_from_open_api 메서드를 구현해주세요")

    def get_content(self):
        url = self.urls[self.url_name]
        self.param += "&serviceKey={SERVICE_KEY}".format(SERVICE_KEY=self.service_key)  # add service_key
        # print(url + "?" + self.param)
        # sys.exit()
        request = urllib.request.Request(url + "?" + self.param)
        response = urllib.request.urlopen(request)
        res_code = response.getcode()
        if res_code == 200:
            response_body = response.read()
            content = xmltodict.parse(response_body.decode('utf-8'))
            return json.dumps(content)
        else:
            return "Error Code:" + res_code