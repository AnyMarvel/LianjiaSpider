# -*- coding: utf-8 -*-
import sys

import os
from os import path

d = path.dirname(__file__)
parent_path = os.path.dirname(d)  # 获得d所在的目录,即d的父级目录
parent_path = os.path.dirname(parent_path)  ##获得parent_path所在的目录即parent_path的父级目录
sys.path.append('/home/lijuntao/PycharmProjects/LianJiaSpider')

from spider.generate_excle import generate_excle


# 修改默认抓取数据,进行数据优化

class ElementConstant:
    def __init__(self):
        self.data_constant = {}
        self.init_source_data()
        index = 0

    def init_source_data(self):
        #
        self.data_constant['序号'] = 0  # 第一个需要进行排序操作
        # 链家编号 链家编号
        self.data_constant['链家编号'] = 1
        #
        self.data_constant['状态'] = 2  # 状态需要进行手动输入判断
        # 每平方售价 单价（元/平米）
        self.data_constant['单价（元/平米）'] = 3
        # 建筑面积 建筑面积：平米
        self.data_constant['建筑面积：平米'] = 4
        # 挂牌时间 挂牌时间
        self.data_constant['挂牌时间'] = 5
        # 上次交易 上次交易时间
        self.data_constant['上次交易时间'] = 6
        # 房子类型 建成时间：年 注释：房屋类型包含　　1990年建/塔楼　需要进行元组分割
        self.data_constant['建成时间：年'] = 7
        #
        self.data_constant['城市'] = 8  # 城市需要进行默认转化
        # 详细区域 '朝阳 垡头 四至五环'　以空格区分进行匹配
        # example ：所属下辖区  朝阳
        # 所属商圈　垡头
        # 所属环线　四至五环
        self.data_constant['所属下辖区'] = 9
        self.data_constant['所属商圈'] = 10
        # 小区名称　所属小区
        self.data_constant['所属小区'] = 11
        self.data_constant['所属环线'] = 12
        # 房屋户型 户型
        self.data_constant['房屋户型'] = 13
        # 朝向 朝向
        self.data_constant['朝向'] = 14
        # 梯户比例 梯户比例
        self.data_constant['梯户比例'] = 15
        # 房屋用途 房屋用途 15
        self.data_constant['房屋用途'] = 16
        # 产权年限 产权年限
        self.data_constant['产权年限'] = 17
        # 建筑类型 建筑类型
        self.data_constant['建筑类型'] = 18
        # 交易权属 交易权属
        self.data_constant['交易权属'] = 19
        # 装修情况 装修情况
        self.data_constant['装修情况'] = 20
        # 建筑结构 建筑结构
        self.data_constant['建筑结构'] = 21
        # 供暖方式 供暖方式
        self.data_constant['供暖方式'] = 22
        # 产权所属 产权所属
        self.data_constant['产权所属'] = 23
        # 户型结构 户型结构 23
        self.data_constant['户型结构'] = 24
        # 配备电梯 配备电梯
        self.data_constant['配备电梯'] = 25
        # 所在楼层 楼层
        self.data_constant['楼层'] = 26
        # 房屋年限 房屋年限
        self.data_constant['房屋年限'] = 27
        # 标题 标题
        self.data_constant['标题'] = 28
        # 网址 网址
        self.data_constant['网址'] = 29
        # 关注房源 关注（人）
        self.data_constant['关注（人）'] = 30
        # 看过房源 看过房源：人
        self.data_constant['看过房源：人'] = 31

    def column_position(self, temp_data):
        return self.data_constant.get(temp_data)

    # 检测匹配是否包含
    def unit_check_name(self, temp_data):
        if self.data_constant.has_key(temp_data):
            return temp_data
        else:
            if temp_data == '每平方售价':
                return '单价（元/平米）'
            if temp_data == '建筑面积':
                return '建筑面积：平米'
            if temp_data == '上次交易':
                return '上次交易时间'
            if temp_data == '房子类型':
                return '建成时间：年'
            if temp_data == '小区名称':
                return '所属小区'
            if temp_data == '房屋户型':
                return '户型'
            # if temp_data == '所在楼层':
            #     return '楼层'
            if temp_data == '关注房源':
                return '关注（人）'
            if temp_data == '看过房源':
                return '看过房源：人'

# Element_Constant = ElementConstant()
# Element_Constant.excleTest()
