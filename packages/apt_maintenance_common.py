import json
import os
from pprint import pprint

from open_api import OpenApi


# TODO DB에 데이터 박고 불러와서 html 만들기
class AptMaintenanceCommon(OpenApi):
    def __init__(self):
        super().__init__()
        self.url_name = "apt_maintenance_fee"

    def set_param(self, parameters):
        self.param = "kaptCode={0}&searchDate={1}".format(parameters['kapt_code'], parameters['search_date'])

    def get_common_category(self):
        return {
            "kaptCode": "아파트코드",
            "kaptName": "아파트명",
        }

    def get_hsmp_labor_cost_info(self, kapt_code, search_date):  # 1. 단지별 인건비 정보조회
        self.url_method = "/getHsmpLaborCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_labor_cost_category(self):
        return {
            "pay": "급여",
            "sundryCost": "제수당",
            "bonus ": "상여금",
            "pension": "퇴직금",
            "accidentPremium ": "산재보험료",
            "employPremium": " 고용보험료",
            "nationalPension": "국민연금",
            "healthPremium": " 건강보험료",
            "welfareBenefit": "식대 등 복리후생비",
        }

    def get_hsmp_ofcrk_cost_info(self, kapt_code, search_date):  # 2. 단지별 제사무비 정보조회
        self.url_method = "/getHsmpOfcrkCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_ofcrk_cost_category(self):
        return {
            "officeSupply": "일반사무용품비",
            "bookSupply": "도서인쇄비",
            "transportCost": "여비교통비",
        }

    def get_hsmp_taxdue_info(self, kapt_code, search_date):  # 3. 단지별 제세공과금 정보조회
        self.url_method = "/getHsmpTaxdueInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_taxdue_category(self):
        return {
            "elecCost": "전기료",
            "telCost": "통신료",
            "postageCost": "우편료",
            "taxrestCost": "제세공과등 등",
        }

    def get_hsmp_clothing_cost_info(self, kapt_code, search_date):  # 4. 단지별 피복비 정보조회
        self.url_method = "/getHsmpClothingCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_clothing_cost_category(self):
        return {
            "clothesCost": "피복비",
        }

    def get_hsmp_edu_traing_cost_info(self, kapt_code, search_date):  # 5. 단지별 교육훈련비 정보조회
        self.url_method = "/getHsmpEduTraingCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_edu_traing_cost_category(self):
        return {
            "eduCost": "교육훈련비",
        }

    def get_hsmp_vhcle_mntnc_cost_info(self, kapt_code, search_date):  # 6. 단지별 차량유지비 정보조회
        self.url_method = "/getHsmpVhcleMntncCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_vhcle_mntnc_cost_category(self):
        return {
            "fuelCost": "연료비",
            "refairCost": "수리비",
            "carInsurance": "보험료",
            "carEtc": "기타차량유지비",
        }

    def get_hsmp_etc_cost_info(self, kapt_code, search_date):  # 7. 단지별 기타 부대비용 정보조회
        self.url_method = "/getHsmpEtcCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_etc_cost_category(self):
        return {
            "careItemCost": "관리용품구입비",
            "accountingCost": "전문가자문비 등",
            "hiddenCost": "잡비",
        }

    def get_hsmp_cleaning_cost_info(self, kapt_code, search_date):  # 8. 단지별 청소비 정보조회
        self.url_method = "/getHsmpCleaningCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_cleaning_cost_category(self):
        return {
            "cleanCost": "청소비",
        }

    def get_hsmp_guard_cost_info(self, kapt_code, search_date):  # 9. 단지별 경비비 정보조회
        self.url_method = "/getHsmpGuardCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_guard_cost_category(self):
        return {
            "guardCost": "경비비",
        }

    def get_hsmp_disinfection_cost_info(self, kapt_code, search_date):  # 10. 단지별 소독비 정보조회
        self.url_method = "/getHsmpDisinfectionCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_disinfection_cost_category(self):
        return {
            "disinfCost": "소독비",
        }

    def get_hsmp_elevator_mntnc_cost_info(self, kapt_code, search_date):  # 11. 단지별 승강기 유지비 정보조회
        self.url_method = "/getHsmpElevatorMntncCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_elevator_mntnc_cost_category(self):
        return {
            "elevCost": "승강기유지비",
        }

    def get_hsmp_home_network_mntnc_cost_info(self, kapt_code, search_date):  # 12. 단지별 지능형 홈네트워크 설비 유지비 정보조회
        self.url_method = "/getHsmpHomeNetworkMntncCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_home_network_mntnc_cost_category(self):
        return {
            "hnetwCost": "지능형홈네트워크설비유지비",
        }

    def get_hsmp_repairs_cost_info(self, kapt_code, search_date):  # 13. 단지별 수선비 정보조회
        self.url_method = "/getHsmpRepairsCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_repairs_cost_category(self):
        return {
            "lrefCost1": "수선비",
        }

    def get_hsmp_facility_mntnc_cost_info(self, kapt_code, search_date):  # 14. 단지별 시설유지비 정보조회
        self.url_method = "/getHsmpFacilityMntncCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_facility_mntnc_cost_category(self):
        return {
            "lrefCost2": "시설유지비",
        }

    def get_hsmp_safety_check_up_cost_info(self, kapt_code, search_date):  # 15. 단지별 안전점검비 정보조회
        self.url_method = "/getHsmpSafetyCheckUpCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_safety_check_up_cost_category(self):
        return {
            "lrefCost3": "안전점검비",
        }

    def get_hsmp_disaster_prevention_cost_info(self, kapt_code, search_date):  # 16. 단지별 재해예방비 정보조회
        self.url_method = "/getHsmpDisasterPreventionCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_disaster_prevention_cost_category(self):
        return {
            "lrefCost4": "재해예방비",
        }

    def get_hsmp_consign_manage_fee_info(self, kapt_code, search_date):  # 17. 단지별 위탁관리 수수료 정보조회
        self.url_method = "/getHsmpConsignManageFeeInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_consign_manage_fee_category(self):
        return {
            "manageCost": "위탁관리수수료",
        }

    def get_maintenance_list(self, kapt_code, search_date):
        self.set_param({"kapt_code": kapt_code, "search_date": search_date})
        json_content = self.get_content()
        return json.loads(json_content)

    def merge_all_data(self, kapt_code, search_date):
        maintenance_fee = {}
        data = self.get_hsmp_labor_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_ofcrk_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_taxdue_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_clothing_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_edu_traing_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_vhcle_mntnc_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_etc_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_cleaning_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_guard_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_disinfection_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_elevator_mntnc_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_home_network_mntnc_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_repairs_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_facility_mntnc_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_safety_check_up_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_disaster_prevention_cost_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)
        data = self.get_hsmp_consign_manage_fee_info(kapt_code, search_date)
        content = self.get_only_item_from_parsed_content(data)
        maintenance_fee.update(content)

        return maintenance_fee


if __name__ == "__main__":
    kapt_code = "A14272314"  # 두산트레지움
    search_date = "201801"
    maintenance_fee = {}
    apt_maintenance_fee = AptMaintenanceCommon()
    data = apt_maintenance_fee.get_hsmp_labor_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_ofcrk_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_taxdue_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_clothing_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_edu_traing_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_vhcle_mntnc_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_etc_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_cleaning_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_guard_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_disinfection_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_elevator_mntnc_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_home_network_mntnc_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_repairs_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_facility_mntnc_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_safety_check_up_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_disaster_prevention_cost_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)
    data = apt_maintenance_fee.get_hsmp_consign_manage_fee_info(kapt_code, search_date)
    content = apt_maintenance_fee.get_only_item_from_parsed_content(data)
    maintenance_fee.update(content)

    pprint(maintenance_fee)
