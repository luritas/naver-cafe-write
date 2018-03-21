# 아파트 전월세 조회
#

import json
import math
import urllib.request
from datetime import datetime
from dateutil.relativedelta import relativedelta

from open_api import OpenApi
from db import Database


class RealPriceTrade(OpenApi):

    def __init__(self):
        super().__init__()
        self.url_name = "real_price_trade"
        self.param = None

    def set_param(self, param):
        region_code = urllib.parse.quote(self.__get_region_code(param['region']))
        self.param = "LAWD_CD={LAWD_CD}&DEAL_YMD={DEAL_YMD}&pageNo={page_no}&numOfRows={row_per_page}" \
            .format(LAWD_CD=region_code, DEAL_YMD=param['date'], page_no=param['page_no'],
                    row_per_page=param['row_per_page'])

    def save_database_from_open_api(self, item):
        pass

    def __get_region_code(self, region):
        return '11305'

    def create_sql(self):
        pass

    def create_param(self, items):
        pass