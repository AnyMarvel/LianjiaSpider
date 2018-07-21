# -*- coding: utf-8 -*-

class chengjiao_constant:
    def __init__(self):
        self.chengjiao_source_data = {}
        self.init_source_data()

    def init_source_data(self):
        self.chengjiao_source_data['链家编号'] = 0
        self.chengjiao_source_data['建筑面积'] = 1
        self.chengjiao_source_data['朝向'] = 2
        self.chengjiao_source_data['户型'] = 3
        self.chengjiao_source_data['成交价(元/平)'] = 4
        self.chengjiao_source_data['城市'] = 5
        self.chengjiao_source_data['下辖区'] = 6
        self.chengjiao_source_data['商圈'] = 7
        self.chengjiao_source_data['小区'] = 8
        self.chengjiao_source_data['成交时间'] = 9
        self.chengjiao_source_data['关注(人)'] = 10
        self.chengjiao_source_data['带看(次)'] = 11
        self.chengjiao_source_data['浏览(次)'] = 12
        self.chengjiao_source_data['成交周期(天)'] = 13
        self.chengjiao_source_data['挂牌价格(万)'] = 14
        self.chengjiao_source_data['售价(万)'] = 15
        self.chengjiao_source_data['调价(次)'] = 16
        self.chengjiao_source_data['建成时间'] = 17
        self.chengjiao_source_data['户型结构'] = 18
        self.chengjiao_source_data['套内面积'] = 19
        self.chengjiao_source_data['电梯'] = 20
        self.chengjiao_source_data['梯户比例'] = 21
        self.chengjiao_source_data['供暖方式'] = 22
        self.chengjiao_source_data['装修'] = 23
        self.chengjiao_source_data['楼型'] = 24
        self.chengjiao_source_data['楼层状态'] = 25
        # self.chengjiao_source_data['上次交易'] = 26
        self.chengjiao_source_data['房屋年限'] = 26
        self.chengjiao_source_data['房屋用途'] = 27
        self.chengjiao_source_data['交易权属'] = 28
        self.chengjiao_source_data['产权所属'] = 29
        self.chengjiao_source_data['土地年限'] = 30
        self.chengjiao_source_data['标题'] = 31
        self.chengjiao_source_data['来源'] = 32

    def chengjiao_check_name(self, temp_data):
        if self.chengjiao_source_data.has_key(temp_data):
            return temp_data
        else:
            if temp_data == '房源户型':
                return '户型'
            if temp_data == '成交':
                return '成交时间'
            if temp_data == '成交价格':
                return '售价(万)'
            if temp_data == '年代':
                return '建成时间'
