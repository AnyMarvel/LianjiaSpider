# -*- coding: utf-8 -*-
import time
import sys

import xlwt

from zaishou_constant import zaishou_constant

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class zaishou_data_analysis:
    def __init__(self):
        self.zaishou_product_entity = {}
        self.zaishou_constant = zaishou_constant()

    def zaishou_product(self, json):
        basic_info = json['basic_info']

        # self.zaishou_product_entity['is_focus'] = basic_info['is_focus']
        # self.zaishou_product_entity['is_off_sale'] = basic_info['is_off_sale']
        self.zaishou_product_entity['标题'] = basic_info['title']
        # self.zaishou_product_entity['city_id'] = basic_info['city_id']
        self.zaishou_product_entity['城市'] = '北京'
        # self.zaishou_product_entity['链家编号'] = basic_info['house_code']#重复值,不需要解析
        # self.zaishou_product_entity['community_id'] = basic_info['community_id']
        self.zaishou_product_entity['小区'] = basic_info['community_name']
        self.zaishou_product_entity['售价（元）'] = basic_info['price']
        self.zaishou_product_entity['在售价(元/平)'] = basic_info['unit_price']
        self.zaishou_product_entity['楼层状态'] = basic_info['floor_state']
        # 三室一厅
        # self.zaishou_product_entity['blueprint_hall_num'] = basic_info['blueprint_hall_num']
        # self.zaishou_product_entity['blueprint_bedroom_num'] = basic_info['blueprint_bedroom_num']
        self.zaishou_product_entity['面积(㎡)'] = basic_info['area']
        # self.zaishou_product_entity['朝向'] = basic_info['orientation']#重复值,不需要解析
        # self.zaishou_product_entity['has_frame_points'] = basic_info['has_frame_points']

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
                try:
                    self.zaishou_product_entity[str(item['name'])] = item['value']
                except Exception as e:
                    pass
        # community_name中对应的是小区名称
        # info_jump_list = json.get('info_jump_list')
        # if info_jump_list is not None:
        #     for item in info_list:
        #         self.zaishou_product_entity[item['name']] = basic_info[item['value']]
        frame_cell = json.get('frame_cell')
        if frame_cell is not None:
            self.zaishou_product_entity[frame_cell['name']] = ','.join(frame_cell['cell_info'])

        # 位置
        location_info = json['location']
        local_temp = str(location_info['title']).split('，')

        self.zaishou_product_entity['下辖区'] = local_temp[0]
        self.zaishou_product_entity['商圈'] = local_temp[1]

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

    def zaishou_product_moire(self, json, row, generate_excle):
        more_list_info = json['data']['list']
        for item in more_list_info:
            for children_item in item['list']:
                if children_item.get('name') is not None and children_item.get('value') is not None:
                    if children_item['name'].encode('utf-8') != '建筑面积：':
                        self.zaishou_product_entity[children_item['name']] = str(children_item['value'])

        # for item in self.zaishou_product_entity.keys():
        #     print item + str(self.zaishou_product_entity.get(item))

        # excle写入单元内容
        for item in self.zaishou_product_entity.keys():
            tempdata = self.zaishou_constant.zaishou_check_name(item.replace('：', '').encode('utf-8'))
            if tempdata is not None:
                column = self.zaishou_constant.zaishou_source_data.get(tempdata)  # 得到数据源所对应的列的位置
                data = self.zaishou_product_entity.get(item)  # 得到数据源
                if tempdata == '建筑面积' or tempdata == '售价(万)':
                    if tempdata == '建筑面积':
                        if data.find('㎡') != -1:
                            data = data[0:data.index('㎡')]
                    else:
                        if data.find('万') != -1:
                            data = data[0:data.index('万')]
                    generate_excle.style.num_format_str = '0.00'
                    generate_excle.wirte_Excle_In_style(row + 1, column, float(data), generate_excle.style)
                elif tempdata == '挂牌时间' or tempdata == '上次交易':
                    data = data.replace('.', '/')
                    generate_excle.style.num_format_str = 'YYYY/MM/DD'
                    generate_excle.wirte_Excle_In_style(row + 1, column, data, generate_excle.style)
                elif tempdata == '在售价(元/平)' or tempdata == '关注房源(人)' or tempdata == '近30日带看(次)' or tempdata == '近7日带看(次)' or tempdata == '建成时间':
                    try:
                        if tempdata == '建成时间':
                            if data.find('年') != -1 and data.find('.') == -1:
                                data = data[0:data.index('年')]
                        generate_excle.style.num_format_str = '0'
                        # print data
                        generate_excle.wirte_Excle_In_style(row + 1, column, int(data), generate_excle.style)
                    except Exception as e:
                        pass
                else:
                    generate_excle.writeExclePositon(row + 1, column, data)
