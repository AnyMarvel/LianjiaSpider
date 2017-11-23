# -*- coding: utf-8 -*-
import time
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class zaishou_data_analysis:
    def __init__(self):
        self.zaishou_product_entity = {}

    def zaishou_product(self, json):
        basic_info = json['basic_info']

        self.zaishou_product_entity['is_focus'] = basic_info['is_focus']
        self.zaishou_product_entity['is_off_sale'] = basic_info['is_off_sale']
        self.zaishou_product_entity['title'] = basic_info['title']
        self.zaishou_product_entity['city_id'] = basic_info['city_id']
        self.zaishou_product_entity['house_code'] = basic_info['house_code']
        self.zaishou_product_entity['community_id'] = basic_info['community_id']
        self.zaishou_product_entity['community_name'] = basic_info['community_name']
        self.zaishou_product_entity['price'] = basic_info['price']
        self.zaishou_product_entity['unit_price'] = basic_info['unit_price']
        self.zaishou_product_entity['floor_state'] = basic_info['floor_state']
        self.zaishou_product_entity['blueprint_hall_num'] = basic_info['blueprint_hall_num']
        self.zaishou_product_entity['blueprint_bedroom_num'] = basic_info['blueprint_bedroom_num']
        self.zaishou_product_entity['area'] = basic_info['area']
        self.zaishou_product_entity['orientation'] = basic_info['orientation']
        self.zaishou_product_entity['has_frame_points'] = basic_info['has_frame_points']

        basic_list = json.get('basic_list')
        if basic_list is not None:
            for item in basic_list:
                self.zaishou_product_entity[str(item['name'])] = item['value']

        color_tags = json.get('color_tags')
        if color_tags is not None:
            for item in color_tags:
                self.zaishou_product_entity["描述信息"] = item['desc']

        info_list = json.get('info_list')
        if info_list is not None:
            for item in info_list:
                self.zaishou_product_entity[str(item['name'])] = item['value']
        # community_name中对应的是小区名称
        # info_jump_list = json.get('info_jump_list')
        # if info_jump_list is not None:
        #     for item in info_list:
        #         self.zaishou_product_entity[item['name']] = basic_info[item['value']]
        frame_cell = json.get('frame_cell')
        if frame_cell is not None:
            self.zaishou_product_entity[frame_cell['name']] = ','.join(frame_cell['cell_info'])
        location = json.get('location')
        if location is not None:
            self.zaishou_product_entity['位置'] = location['title']

        house_news = json.get('house_news')
        if house_news is not None:
            house_news_list = house_news['list']
            for item in house_news_list:
                self.zaishou_product_entity[str(item['name'])] = item['value']

        timeline = json.get('timeline')
        if timeline is not None:
            timeline_list = timeline['list']
            for item in timeline_list:
                self.zaishou_product_entity[str(item['desc'])] = time.strftime('%Y-%m-%d', time.localtime(item['time']))

    def zaishou_product_moire(self, json):
        more_list_info = json['data']['list']
        for item in more_list_info:
            for children_item in item['list']:
                if children_item.get('name') is not None and children_item.get('value') is not None:
                    self.zaishou_product_entity[children_item['name']] = str(children_item['value'])
        for item in self.zaishou_product_entity.keys():
            print item, self.zaishou_product_entity.get(item)
