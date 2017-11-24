# -*- coding: utf-8 -*-
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class zaishou_constant:
    def __init__(self):
        self.zaishou_source_data = {}
        self.init_source_data()

    def init_source_data(self):
        self.zaishou_source_data['链家编号'] = 0
        self.zaishou_source_data['建筑面积'] = 1
        self.zaishou_source_data['朝向'] = 2
        self.zaishou_source_data['户型'] = 3
        self.zaishou_source_data['在售价(元/平)'] = 4
        self.zaishou_source_data['城市'] = 5
        self.zaishou_source_data['下辖区'] = 6
        self.zaishou_source_data['商圈'] = 7
        self.zaishou_source_data['小区'] = 8
        self.zaishou_source_data['挂牌时间'] = 9
        self.zaishou_source_data['关注房源(人)'] = 10
        self.zaishou_source_data['近30日带看(次)'] = 11
        self.zaishou_source_data['近7日带看(次)'] = 12
        self.zaishou_source_data['售价(万)'] = 13
        self.zaishou_source_data['建成时间'] = 14
        self.zaishou_source_data['户型格局'] = 15
        self.zaishou_source_data['户型结构'] = 16
        self.zaishou_source_data['套内面积'] = 17
        self.zaishou_source_data['电梯'] = 18
        self.zaishou_source_data['梯户比例'] = 19
        self.zaishou_source_data['供暖方式'] = 20
        self.zaishou_source_data['装修'] = 21
        self.zaishou_source_data['楼型'] = 22
        self.zaishou_source_data['楼层状态'] = 23
        self.zaishou_source_data['上次交易'] = 24
        self.zaishou_source_data['房屋年限'] = 25
        self.zaishou_source_data['房屋用途'] = 26
        self.zaishou_source_data['交易权属'] = 27
        self.zaishou_source_data['产权所属'] = 28
        self.zaishou_source_data['抵押信息'] = 29
        self.zaishou_source_data['土地年限'] = 30
        self.zaishou_source_data['标题'] = 31

    def zaishou_check_name(self, temp_data):
        if self.zaishou_source_data.has_key(temp_data):
            return temp_data
        else:
            if temp_data == '房源户型':
                return '户型'
            if temp_data == '挂牌':
                return '挂牌时间'
            if temp_data == '年代':
                return '建成时间'
            if temp_data=='售价':
                return '售价(万)'
