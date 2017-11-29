# -*- coding: utf-8 -*-
import sys

import xlwt

from chengjiao_constant import chengjiao_constant

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class cheng_jiao_data_analysis:
    def __init__(self):
        self.chengjiao_product_entity = {}
        self.chengjiao_constant = chengjiao_constant()

    def chengjiao_product(self, json):
        if json is not None:
            basic_info = json.get('basic_info')
            if basic_info.get('title') is not None:
                self.chengjiao_product_entity['标题'] = str(basic_info.get('title'))
            self.chengjiao_product_entity['城市'] = '北京'
            # self.chengjiao_product_entity['链家编号'] = str(basic_info.get('house_code'])#重复值,不需要解析
            # self.chengjiao_product_entity['community_id'] = str(basic_info.get('community_id'])
            if basic_info.get('community_name') is not None:
                self.chengjiao_product_entity['小区'] = str(basic_info.get('community_name'))
            if basic_info.get('price') is not None:
                self.chengjiao_product_entity['总价(元)'] = str(basic_info.get('price'))
            if basic_info.get('unit_price') is not None:
                self.chengjiao_product_entity['成交价(元/平)'] = str(basic_info.get('unit_price'))
            if basic_info.get('floor_state') is not None:
                self.chengjiao_product_entity['楼层状态'] = str(basic_info.get('floor_state'))
            # self.chengjiao_product_entity['blueprint_hall_num'] = str(basic_info.get('blueprint_hall_num'))
            # self.chengjiao_product_entity['blueprint_bedroom_num'] = str(basic_info.get('blueprint_bedroom_num'))
            # self.chengjiao_product_entity['面积(㎡)'] = str(basic_info.get('area')) + '㎡'
            # self.chengjiao_product_entity['朝向'] = str(basic_info.get('orientation'))#重复值,不需要解析

            basic_list_data = json.get('basic_list')
            if basic_list_data is not None:
                for item in basic_list_data:
                    if item.get('name') is not None and item.get('value') is not None:
                        self.chengjiao_product_entity[str(item['name'])] = str(item['value'])

            info_list_data = json.get('info_list')
            if info_list_data is not None:
                for item in info_list_data:
                    if item.get('name') is not None and item.get('value') is not None:
                        self.chengjiao_product_entity[item['name']] = str(item['value'])

            # 位置
            location_info = json.get('location')
            if location_info is not None and location_info.get('title') is not None:
                local_temp = str(location_info['title']).split('，')
                if local_temp[0] is not None:
                    self.chengjiao_product_entity['下辖区'] = local_temp[0]
                if local_temp[1] is not None:
                    self.chengjiao_product_entity['商圈'] = local_temp[1]

            # 本房成交信息回顾
            if json.get('deal_info') is not None and json.get('deal_info').get('review') is not None and json.get(
                    'deal_info').get('review').get('list') is not None:
                deal_info = json['deal_info']['review']['list']
                for item in deal_info:
                    if item.get('name') is not None and item.get('value') is not None:
                        self.chengjiao_product_entity[item['name']] = str(item['value'])

        # 历史成交 先判断是否有历史成交记录
        history_info = json.get('history')
        if history_info is not None:
            if history_info.get('name') is not None and history_info.get('list') is not None:
                self.chengjiao_product_entity[history_info['name']] = str(history_info['list'])
                # print self.chengjiao_product_entity

    # 更多信息中的json结构解析
    def chengjiao_more_infos(self, json, row, generate_excle):
        if json.get('data') is not None:
            more_list_info = json.get('data').get('list')
            if more_list_info is not None:
                for item in more_list_info:
                    if item.get('list') is not None:
                        for children_item in item['list']:
                            if children_item.get('name') is not None and children_item.get('value') is not None:
                                self.chengjiao_product_entity[children_item['name']] = str(children_item['value'])
        #
        # for item in self.chengjiao_product_entity.keys():
        #     print item + self.chengjiao_product_entity.get(item)

        for item in self.chengjiao_product_entity.keys():
            tempdata = self.chengjiao_constant.chengjiao_check_name(item.replace('：', '').encode('utf-8'))
            if tempdata is not None:
                column = self.chengjiao_constant.chengjiao_source_data.get(tempdata)
                data = self.chengjiao_product_entity.get(item)

                if tempdata == '建筑面积' or tempdata == '售价(万)' or tempdata == '挂牌价格(万)':
                    if tempdata == '建筑面积':
                        if data.find('㎡') != -1:
                            data = data[0:data.index('㎡')]
                    elif tempdata == '售价(万)':
                        if data.find('万') != -1:
                            data = data[0:data.index('万')]
                    # print data
                    generate_excle.style.num_format_str = '0.00'
                    try:
                        generate_excle.wirte_Excle_In_style(row + 1, column, float(data), generate_excle.style)
                    except Exception as e:
                        pass
                elif tempdata == '成交时间':
                    data = data.replace('.', '/')
                    generate_excle.style.num_format_str = 'YYYY/MM/DD'
                    generate_excle.wirte_Excle_In_style(row + 1, column, data, generate_excle.style)
                elif tempdata == '成交价(元/平)' or tempdata == '关注(人)' or tempdata == '带看(次)' or tempdata == '浏览(次)' \
                        or tempdata == '成交周期(天)' or tempdata == '调价(次)' \
                        or tempdata == '建成时间':
                    try:
                        if tempdata == '建成时间':
                            if data.find('年') != -1:
                                data = data[0:data.index('年') - 1]
                        generate_excle.style.num_format_str = '0'
                        # print data
                        generate_excle.wirte_Excle_In_style(row + 1, column, int(data), generate_excle.style)
                    except Exception as e:
                        pass
                else:
                    generate_excle.writeExclePositon(row + 1, column, data)
                    # generate_excle.writeExclePositon(row + 1, column, data)
