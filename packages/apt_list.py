import json
import sys
from pprint import pprint

from .open_api import OpenApi


class AptList(OpenApi):
    def __init__(self):
        super().__init__()
        self.url_name = "apt_list"
        self.load_code = None
        self.merged_data = None

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

    def get_all_list_query(self, load_code):
        return """
SELECT `apt_list`.`id`,
    `apt_list`.`load_code`,
    `apt_list`.`kapt_code`,
    `apt_list`.`kapt_name`,
    `apt_list`.`created_at`
FROM `naver`.`apt_list`
WHERE
    load_code = %s
ORDER BY FIELD(kapt_code,
    'A14272305',
    'A14210001',
    'A14272311',
    'A14210002',
    'A14272304',
    'A14280502',
    'A14272313',
    'A14272314',
    'A14272308',
    'A14272309') DESC;
        """ % load_code

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

    def get_html(self, merged_data):
        html = """
<br>
    <br>
        <table style="width: 7000px">
            <thead>
                <tr>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>아파트/관리비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>급여</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>제수당</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>상여금</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>퇴직금</td>
                    
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>산재보험료</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>고용보험료</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>국민연금</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>건강보험료</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>식대 등 복리후생비</td>
                    
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>일반사무용품비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>도서인쇄비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>여비교통비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>전기료</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>통신료</td>
                    
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>우편료</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>제세공과등 등</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>피복비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>교육훈련비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>연료비</td>
                    
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>수리비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>보험료</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>기타차량유지비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>관리용품구입비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>전문가자문비 등</td>
                    
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>잡비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>청소비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>경비비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>소독비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>승강기유지비</td>
                    
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>지능형홈네트워크설비유지비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>수선비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>시설유지비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>안전점검비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>재해예방비</td>
                    
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>위탁관리수수료</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>난방공용</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>난방전용</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>급탕공용</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>급탕전용</td>
                    
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>가스공용</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>가스전용</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>전기공용</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>전기전용</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>수도공용</td>
                    
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>수도전용</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>정화조오물수수료</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>생활폐기물수수료</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>입주자대표회의 운영비</td>
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>건물보험료</td>
                    
                    <th style='vertical-align: bottom; border-bottom: 2px solid #ddd;padding: 8px;line-height: 1.6;'>선거관리위원회 운영비</td>
                </tr>
            </thead>
            <tbody>
        """
        distinct_row = 0
        for index in range(0, len(merged_data)):
            distinct_row += 1
            bgcolor = distinct_row % 2 == 1 and "background-color: #ddd;" or ""
            html += """
                <tr style='{0} text-align: center;'>
                    <td style='padding: 8px 12px;;line-height: 1.6;vertical-align: top; text-align: left;'>{1}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{2}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{3}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{4}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{5}</td>
                    
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{6}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{7}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{8}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{9}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{10}</td>
                    
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{11}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{12}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{13}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{14}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{15}</td>
                    
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{16}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{17}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{18}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{19}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{20}</td>
                    
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{21}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{22}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{23}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{24}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{25}</td>
                    
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{26}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{27}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{28}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{29}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{30}</td>
                    
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{31}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{32}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{33}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{34}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{35}</td>
                    
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{36}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{37}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{38}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{39}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{40}</td>
                    
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{41}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{42}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{43}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{44}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{45}</td>
                    
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{46}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{47}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{48}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{49}</td>
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{50}</td>
                    
                    <td style='padding: 8px 12px;line-height: 1.6;vertical-align: top;'>{51}</td>
                </tr>
                """.format(bgcolor,

                           merged_data[index]['아파트명'],
                           merged_data[index]['급여'],
                           merged_data[index]['제수당'],
                           merged_data[index]['상여금'],
                           merged_data[index]['퇴직금'],

                           merged_data[index]['산재보험료'],
                           merged_data[index]['고용보험료'],
                           merged_data[index]['국민연금'],
                           merged_data[index]['건강보험료'],
                           merged_data[index]['식대 등 복리후생비'],

                           merged_data[index]['일반사무용품비'],
                           merged_data[index]['도서인쇄비'],
                           merged_data[index]['여비교통비'],
                           merged_data[index]['전기료'],
                           merged_data[index]['통신료'],

                           merged_data[index]['우편료'],
                           merged_data[index]['제세공과등 등'],
                           merged_data[index]['피복비'],
                           merged_data[index]['교육훈련비'],
                           merged_data[index]['연료비'],

                           merged_data[index]['수리비'],
                           merged_data[index]['보험료'],
                           merged_data[index]['기타차량유지비'],
                           merged_data[index]['관리용품구입비'],
                           merged_data[index]['전문가자문비 등'],

                           merged_data[index]['잡비'],
                           merged_data[index]['청소비'],
                           merged_data[index]['경비비'],
                           merged_data[index]['소독비'],
                           merged_data[index]['승강기유지비'],

                           merged_data[index]['지능형홈네트워크설비유지비'],
                           merged_data[index]['수선비'],
                           merged_data[index]['시설유지비'],
                           merged_data[index]['안전점검비'],
                           merged_data[index]['재해예방비'],

                           merged_data[index]['위탁관리수수료'],
                           merged_data[index]['난방공용'],
                           merged_data[index]['난방전용'],
                           merged_data[index]['급탕공용'],
                           merged_data[index]['급탕전용'],

                           merged_data[index]['가스공용'],
                           merged_data[index]['가스전용'],
                           merged_data[index]['전기공용'],
                           merged_data[index]['전기전용'],
                           merged_data[index]['수도공용'],

                           merged_data[index]['수도전용'],
                           merged_data[index]['정화조오물수수료'],
                           merged_data[index]['생활폐기물수수료'],
                           merged_data[index]['입주자대표회의 운영비'],
                           merged_data[index]['건물보험료'],

                           merged_data[index]['선거관리위원회 운영비'],
                           )
        html += """
        </tbody>
        </table>
        """

        return html

    if __name__ == "__main__":
        apt_list = AptList()
        load_code = "1130510100"  # 미아동
        content = apt_list.get_legal_dong_apt_list(load_code)
        items = apt_list.get_items_from_parsed_content(content)
        pprint(items)
