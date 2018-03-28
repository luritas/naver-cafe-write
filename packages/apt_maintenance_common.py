import json
import os
from pprint import pprint

from packages.open_api import OpenApi


class AptMaintenanceFee(OpenApi):
    def __init__(self):
        super().__init__()
        self.url_name = "apt_maintenance_fee"

    def set_param(self, parameters):
        self.param = "kaptCode={0}&searchDate={1}".format(parameters['kapt_code'], parameters['search_date'])

    def get_hsmp_labor_cost_info(self, kapt_code, search_date):  # 1. 단지별 인건비 정보조회
        self.url_method = "/getHsmpLaborCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_ofcrk_cost_info(self, kapt_code, search_date):  # 2. 단지별 제사무비 정보조회
        self.url_method = "/getHsmpOfcrkCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_taxdue_info(self, kapt_code, search_date):  # 3. 단지별 제세공과금 정보조회
        self.url_method = "/getHsmpTaxdueInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_clothing_cost_info(self, kapt_code, search_date):  # 4. 단지별 피복비 정보조회
        self.url_method = "/getHsmpClothingCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_edu_traing_cost_info(self, kapt_code, search_date):  # 5. 단지별 교육훈련비 정보조회
        self.url_method = "/getHsmpEduTraingCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_vhcle_mntnc_cost_info(self, kapt_code, search_date):  # 6. 단지별 차량유지비 정보조회
        self.url_method = "/getHsmpVhcleMntncCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_etc_cost_info(self, kapt_code, search_date):  # 7. 단지별 기타 부대비용 정보조회
        self.url_method = "/getHsmpEtcCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_cleaning_cost_info(self, kapt_code, search_date):  # 8. 단지별 청소비 정보조회
        self.url_method = "/getHsmpCleaningCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_guard_cost_info(self, kapt_code, search_date):  # 9. 단지별 경비비 정보조회
        self.url_method = "/getHsmpGuardCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_disinfection_cost_info(self, kapt_code, search_date):  # 10. 단지별 소독비 정보조회
        self.url_method = "/getHsmpDisinfectionCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_elevator_mntnc_cost_info(self, kapt_code, search_date):  # 11. 단지별 승강기 유지비 정보조회
        self.url_method = "/getHsmpElevatorMntncCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_home_network_mntnc_cost_info(self, kapt_code, search_date):  # 12. 단지별 지능형 홈네트워크 설비 유지비 정보조회
        self.url_method = "/getHsmpHomeNetworkMntncCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_repairs_cost_info(self, kapt_code, search_date):  # 13. 단지별 수선비 정보조회
        self.url_method = "/getHsmpRepairsCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_facility_mntnc_cost_info(self, kapt_code, search_date):  # 14. 단지별 시설유지비 정보조회
        self.url_method = "/getHsmpFacilityMntncCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_safety_check_up_cost_info(self, kapt_code, search_date):  # 15. 단지별 안전점검비 정보조회
        self.url_method = "/getHsmpSafetyCheckUpCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_disaster_prevention_cost_info(self, kapt_code, search_date):  # 16. 단지별 재해예방비 정보조회
        self.url_method = "/getHsmpDisasterPreventionCostInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_hsmp_consign_manage_fee_info(self, kapt_code, search_date):  # 17. 단지별 위탁관리 수수료 정보조회
        self.url_method = "/getHsmpConsignManageFeeInfo"
        return self.get_maintenance_list(kapt_code, search_date)

    def get_maintenance_list(self, kapt_code, search_date):
        self.set_param({"kapt_code": kapt_code, "search_date": search_date})
        json_content = self.get_content()
        return json.loads(json_content)


if __name__ == "__main__":
    apt_maintenance_fee = AptMaintenanceFee()
    kapt_code = "A14272314"  # 우선 두산만
    search_date = "201801"
    content = apt_maintenance_fee.get_hsmp_labor_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_ofcrk_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_taxdue_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_clothing_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_edu_traing_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_vhcle_mntnc_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_etc_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_cleaning_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_guard_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_disinfection_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_elevator_mntnc_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_home_network_mntnc_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_repairs_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_facility_mntnc_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_safety_check_up_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_disaster_prevention_cost_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
    content = apt_maintenance_fee.get_hsmp_consign_manage_fee_info(kapt_code, search_date)
    pprint(content)
    print("=" * 50)
