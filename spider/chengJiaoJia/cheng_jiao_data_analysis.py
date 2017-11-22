# -*- coding: utf-8 -*-
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class cheng_jiao_data_analysis:
    def __init__(self):
        self.er_shou_product_entity = {}
        pass

    def chengjiao_product(self, json):
        basic_info = json['basic_info']
        self.er_shou_product_entity['标题'] = str(basic_info['title'])
        self.er_shou_product_entity['city_id'] = str(basic_info['city_id'])
        self.er_shou_product_entity['house_code'] = str(basic_info['house_code'])
        self.er_shou_product_entity['community_id'] = str(basic_info['community_id'])
        self.er_shou_product_entity['community_name'] = str(basic_info['community_name'])
        self.er_shou_product_entity['price'] = str(basic_info['price'])
        self.er_shou_product_entity['unit_price'] = str(basic_info['unit_price'])
        self.er_shou_product_entity['floor_state'] = str(basic_info['floor_state'])
        self.er_shou_product_entity['blueprint_hall_num'] = str(basic_info['blueprint_hall_num'])
        self.er_shou_product_entity['blueprint_bedroom_num'] = str(basic_info['blueprint_bedroom_num'])
        self.er_shou_product_entity['area'] = str(basic_info['area']) + '㎡'
        self.er_shou_product_entity['orientation'] = str(basic_info['orientation'])

        basic_list_data = json['basic_list']
        for item in basic_list_data:
            self.er_shou_product_entity[str(item['name'])] = str(item['value'])

        info_list_data = json['info_list']
        for item in info_list_data:
            self.er_shou_product_entity[item['name']] = str(item['value'])

        print self.er_shou_product_entity

    def chengjiao_more_infos(self, json):
        pass
