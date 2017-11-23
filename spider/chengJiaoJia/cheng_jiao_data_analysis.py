# -*- coding: utf-8 -*-


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
            if item.get('name') is not None and item.get('value') is not None:
                self.er_shou_product_entity[str(item['name'])] = str(item['value'])

        info_list_data = json.get('info_list')
        if info_list_data is not None:
            for item in info_list_data:
                if item.get('name') is not None and item.get('value') is not None:
                    self.er_shou_product_entity[item['name']] = str(item['value'])

        # 位置
        location_info = json['location']
        self.er_shou_product_entity['location'] = str(location_info['title'])
        # 本房成交信息回顾
        deal_info = json['deal_info']['review']['list']
        for item in deal_info:
            if item.get('name') is not None and item.get('value') is not None:
                self.er_shou_product_entity[item['name']] = str(item['value'])
        # 历史成交 先判断是否有历史成交记录
        history_info = json.get('history')
        if history_info is not None:
            self.er_shou_product_entity[history_info['name']] = str(history_info['list'])
            # print self.er_shou_product_entity

    def chengjiao_more_infos(self, json):
        more_list_info = json['data']['list']
        for item in more_list_info:
            for children_item in item['list']:
                if children_item.get('name') is not None and children_item.get('value') is not None:
                    self.er_shou_product_entity[children_item['name']] = str(children_item['value'])

        for item in self.er_shou_product_entity.keys():
            print item + ":" + self.er_shou_product_entity.get(item)
