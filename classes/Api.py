import abc
import json
from pprint import pprint


class Api:
    __metaclass__ = abc.ABCMeta
    data = None
    name = None

    # 인스턴스를 생성할때 dictionary 로 parameters 를 정의한다
    def __init__(self):
        json_data = open('/Users/peterpan_jk/git/naver-cafe-wrtie/data/actual_transaction_price.json')
        self.data = json.load(json_data)

    @abc.abstractmethod
    def get_name(self):
        return self.name

    def info(self):
        pass

    def set_parameters(self):
        pass

    def get_parameters(self):
        pass

    def get_items(self):
        pass

    @abc.abstractmethod
    def get_data(self):
        pass


if __name__ == "__main__":
    api = Api()

