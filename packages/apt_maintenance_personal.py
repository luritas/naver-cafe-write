import json
from pprint import pprint

from .open_api import OpenApi


class AptMaintenancePersonal(OpenApi):
    def __init__(self):
        super().__init__()
        self.url_name = "apt_maintenance_personal"

    def set_param(self, parameters):
        self.param = "kaptCode={0}&searchDate={1}".format(parameters['kapt_code'], parameters['search_date'])

    def get_maintenance_list(self, kapt_code, search_date):
        self.set_param({"kapt_code": kapt_code, "search_date": search_date})
        json_content = self.get_content()
        return json.loads(json_content)

    def get_common_category(self):
        return {
            "load_code": "지역",
            "searchDate": "기준월",
            "kaptCode": "아파트코드",
            "kaptName": "아파트명",
        }

    # 단지별 난방비 정보조회
    def get_hsmp_heat_cost_info(self, kapt_code, search_date):
        self.url_method = "/getHsmpHeatCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_heat_cost_category(self):
        return {
            "heatC": "난방공용",
            "heatP": "난방전용",
        }

    # 단지별 급탕비 정보조회
    def get_hsmp_hot_water_cost_info(self, kapt_code, search_date):
        self.url_method = "/getHsmpHotWaterCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_hot_water_cost_category(self):
        return {
            "waterHotC": "급탕공용",
            "waterHotP": "급탕전용",
        }

    # 단지별 가스사용료 정보조회
    def get_hsmp_gas_rental_fee_info(self, kapt_code, search_date):
        self.url_method = "/getHsmpGasRentalFeeInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_gas_rental_fee_category(self):
        return {
            "gasC": "가스공용",
            "gasP": "가스전용",
        }

    # 단지별 전기료 정보조회
    def get_hsmp_electricity_cost_info(self, kapt_code, search_date):
        self.url_method = "/getHsmpElectricityCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_electricity_cost_category(self):
        return {
            "electC": "전기공용",
            "electP": "전기전용",
        }

    # 단지별 수도료 정보조회
    def get_hsmp_water_cost_info(self, kapt_code, search_date):
        self.url_method = "/getHsmpWaterCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_water_cost_category(self):
        return {
            "waterCoolC": "수도공용",
            "waterCoolP": "수도전용",
        }

    # 단지별 정화조오물 수수료 정보조회
    def get_hsmp_water_purifier_tank_fee_info(self, kapt_code, search_date):
        self.url_method = "/getHsmpWaterPurifierTankFeeInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_water_purifier_tank_fee_category(self):
        return {
            "purifi": "정화조오물수수료",
        }

    # 단지별 생활폐기물 수수료 정보조회
    def get_hsmp_domestic_waste_fee_info(self, kapt_code, search_date):
        self.url_method = "/getHsmpDomesticWasteFeeInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_domestic_waste_fee_category(self):
        return {
            "scrap": "생활폐기물수수료",
        }

    # 단지별 입주자대표회의 운영비 정보조회
    def get_hsmp_moving_in_representation_mtg_info(self, kapt_code, search_date):
        self.url_method = "/getHsmpMovingInRepresentationMtgInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_moving_in_representation_mtg_category(self):
        return {
            "preMeet": "입주자대표회의 운영비",
        }

    # 단지별 건물보험료 정보조회
    def get_hsmp_building_insurance_fee_info(self, kapt_code, search_date):
        self.url_method = "/getHsmpBuildingInsuranceFeeInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_building_insurance_fee_category(self):
        return {
            "buildInsu": "건물보험료",
        }

    # 단지별 선거관리위원회 운영비 정보조회
    def get_hsmp_election_orpns_info(self, kapt_code, search_date):
        self.url_method = "/getHsmpElectionOrpnsInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_election_orpns_category(self):
        return {
            "electionMng": "선거관리위원회 운영비",
        }

    def merge_all_data(self, kapt_code, search_date):
        maintenance_fee = {}
        data = self.get_hsmp_heat_cost_info(kapt_code, search_date)
        if data['response']['body'] is None:
            return []
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_hot_water_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_gas_rental_fee_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_electricity_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_water_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_water_purifier_tank_fee_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_domestic_waste_fee_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_moving_in_representation_mtg_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_building_insurance_fee_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_election_orpns_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)

        return maintenance_fee

    def create_sql(self):
        sql = """
INSERT INTO `naver`.`apt_maintenance_personal`
(
`load_code`, `kaptCode`, `kaptName`, `searchDate`, `heatC`,
`heatP`, `waterHotC`, `waterHotP`, `gasC`, `gasP`,
`electC`, `electP`, `waterCoolC`, `waterCoolP`, `purifi`,
`scrap`, `preMeet`, `buildInsu`, `electionMng`
)
VALUES
(
%s, %s, %s, %s, %s,
%s, %s, %s, %s, %s,
%s, %s, %s, %s, %s,
%s, %s, %s, %s);
"""
        return sql

    def create_param(self, item, load_code, search_date):
        param = []
        try:
            param = [tuple([
                load_code,
                item['kaptCode'],
                item['kaptName'],
                search_date,
                item['heatC'],

                item['heatP'],
                item['waterHotC'],
                item['waterHotP'],
                item['gasC'],
                item['gasP'],

                item['electC'],
                item['electP'],
                item['waterCoolC'],
                item['waterCoolP'],
                item['purifi'],

                item['scrap'],
                item['preMeet'],
                item['buildInsu'],
                item['electionMng'],
            ])]
        except Exception as e:
            print(e)
            print(item)

        return param

    def get_category(self):
        category = self.get_common_category()
        category.update(self.get_hsmp_heat_cost_category())
        category.update(self.get_hsmp_hot_water_cost_category())
        category.update(self.get_hsmp_gas_rental_fee_category())
        category.update(self.get_hsmp_electricity_cost_category())
        category.update(self.get_hsmp_water_cost_category())
        category.update(self.get_hsmp_water_purifier_tank_fee_category())
        category.update(self.get_hsmp_domestic_waste_fee_category())
        category.update(self.get_hsmp_moving_in_representation_mtg_category())
        category.update(self.get_hsmp_building_insurance_fee_category())
        category.update(self.get_hsmp_election_orpns_category())

        return category

    def get_all_data_query(self, load_code, search_date):
        sql = """
SELECT 
    `apt_maintenance_personal`.`id`,
    `apt_maintenance_personal`.`load_code`,
    `apt_maintenance_personal`.`kaptCode`,
    `apt_maintenance_personal`.`kaptName`,
    `apt_maintenance_personal`.`searchDate`,
    `apt_maintenance_personal`.`heatC`,
    `apt_maintenance_personal`.`heatP`,
    `apt_maintenance_personal`.`waterHotC`,
    `apt_maintenance_personal`.`waterHotP`,
    `apt_maintenance_personal`.`gasC`,
    `apt_maintenance_personal`.`gasP`,
    `apt_maintenance_personal`.`electC`,
    `apt_maintenance_personal`.`electP`,
    `apt_maintenance_personal`.`waterCoolC`,
    `apt_maintenance_personal`.`waterCoolP`,
    `apt_maintenance_personal`.`purifi`,
    `apt_maintenance_personal`.`scrap`,
    `apt_maintenance_personal`.`preMeet`,
    `apt_maintenance_personal`.`buildInsu`,
    `apt_maintenance_personal`.`electionMng`
FROM
    `naver`.`apt_maintenance_personal`
WHERE
    load_code = %s AND searchDate = %s;
        """ % (load_code, search_date)
        return sql
