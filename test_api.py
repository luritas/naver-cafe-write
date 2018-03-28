import unittest

from packages.open_api import OpenApi
from packages.apt_list import AptList
from packages.apt_maintenance_common import AptMaintenanceFee
from pprint import pprint


class TestApi(unittest.TestCase):

    def test_result_code_from_apt_list_legal(self):
        apt_list = AptList()
        load_code = "1130510100"  # 미아동
        content = apt_list.get_legal_dong_apt_list(load_code)
        result_code = apt_list.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

    def test_result_code_from_apt_list_road(self):
        apt_list = AptList()
        load_code = "1130510100"  # 미아동
        content = apt_list.get_road_name_apt_list(load_code)
        result_code = apt_list.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

    def test_result_code_from_apt_maintenance_fee(self):
        apt_maintenance_fee = AptMaintenanceFee()
        kapt_code = "A14272314"  # 우선 두산만
        search_date = "201801"
        content = apt_maintenance_fee.get_hsmp_labor_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_ofcrk_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_taxdue_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_clothing_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_edu_traing_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_vhcle_mntnc_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_etc_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_cleaning_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_guard_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_disinfection_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_elevator_mntnc_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_home_network_mntnc_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_repairs_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_facility_mntnc_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_safety_check_up_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_disaster_prevention_cost_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')

        content = apt_maintenance_fee.get_hsmp_consign_manage_fee_info(kapt_code, search_date)
        result_code = apt_maintenance_fee.get_result_code_from_parsed_content(content)
        self.assertEqual(result_code, '00')
