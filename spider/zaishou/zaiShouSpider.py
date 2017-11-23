# -*- coding: utf-8 -*-
import time
import requests
import base64
import hashlib
import json
import sys
from zaishou_data_analysis import zaishou_data_analysis


class zaishou:
    def __init__(self):
        # 爬取页数
        self.count = 1
        # 一页一共多少数据
        self.limit_count = 10
        # 第几页（页数*一页一共多少数据）
        self.limit_offset = -10
        # 当前时间
        self.request_ts = 0
        # 由android JNI逆向得出的链家apk秘钥
        # self.Authorization = '93273ef46a0b880faf4466c48f74878fcity_id=110000limit_count=10limit_offset=0request_ts=1511232061'
        self.headers = {
            'Page-Schema': 'tradedSearch%2Flist',
            'Referer': 'homepage%3F',
            'Cookie': 'lianjia_udid=6fc5da9bec827948;lianjia_token=2.007d00a43c04bd8bd26cad8d0d82a4302c;lianjia_ssid=a3c137a9-c77c-438a-a6c0-27c160707d7c;lianjia_uuid=39d20bd7-28a5-4ffa-bbac-dd70d6eaf2cd',
            'Lianjia-Access-Token': '2.007d00a43c04bd8bd26cad8d0d82a4302c',
            'User-Agent': 'HomeLink8.2.1;generic Custom+Phone+-+5.0.0+-+API+21+-+768x1280; Android 5.0',
            'Lianjia-Channel': 'Android_Anzhi',
            'Lianjia-Device-Id': '6fc5da9bec827948',
            'Lianjia-Version': '8.2.1',
            'Authorization': '93273ef46a0b880faf4466c48f74878fcity_id=110000limit_count=10limit_offset=0request_ts=1511232061',
            'Lianjia-Im-Version': '2.4.4',
            'Host': 'app.api.lianjia.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }
        self.zaishou_data_analysis = zaishou_data_analysis()

    def start(self):
        for i in range(self.count):
            time.sleep(1)
            self.request_url_list()

    def request_url_list(self):
        self.limit_offset = self.limit_offset + self.limit_count
        self.request_ts = int(time.time())
        source_Authorization = '93273ef46a0b880faf4466c48f74878fcity_id=110000limit_count=' + str(
            self.limit_count) + 'limit_offset=' + str(self.limit_offset) + 'request_ts=' + str(self.request_ts)

        source_Authorization = '93273ef46a0b880faf4466c48f74878fareaRequest=city_id=110000communityRequset=' \
                               'comunityIdRequest=condition=has_recommend=1isFromMap=falseis_history=0is_suggestion=0limit_count=' + str(
            self.limit_count) + 'limit_offset=' + str(self.limit_offset) + 'moreRequest=priceRequest=request_ts=' + str(
            self.request_ts) + 'roomRequest=schoolRequest=sugQueryStr='
        # print source_Authorization

        self.generate_authorization(source_Authorization)
        url = 'https://app.api.lianjia.com/house/ershoufang/searchv4?city_id=110000&priceRequest=&limit_offset=' + str(
            self.limit_offset) + '&moreRequest=&communityRequset=&has_recommend=1&is_suggestion=0&limit_count=' + str(
            self.limit_count) + '&sugQueryStr=&comunityIdRequest=&areaRequest=&' \
                                'is_history=0&schoolRequest=&condition=&roomRequest=&isFromMap=false&request_ts=' + str(
            self.request_ts)
        # print headers.get('Authorization')
        print(url)
        self.get_result_json_list(url)

    def get_result_json_list(self, url):
        result_list = requests.get(url, headers=self.headers)
        # print result_list.text
        jsonsource = json.loads(result_list.text, encoding='utf-8')

        for i in jsonsource["data"]['list']:
            # print jsonsource["data"]['list']
            self.request_ts = int(time.time())
            zaishou_pruduct_url_authorization = '93273ef46a0b880faf4466c48f74878fagent_type=1house_code=' + str(
                i['house_code']) + 'request_ts=' + str(self.request_ts)
            # 生成证书认证
            self.generate_authorization(zaishou_pruduct_url_authorization)

            zaishou_pruduct_url = 'https://app.api.lianjia.com/house/ershoufang/detailpart1?house_code=' + str(
                i['house_code']) + '&agent_type=1&request_ts=' + str(self.request_ts)
            result_product = requests.get(zaishou_pruduct_url, headers=self.headers)
            print zaishou_pruduct_url
            # print result_product.text

            product_json = json.loads(result_product.text, encoding='utf-8')
            self.zaishou_data_analysis.zaishou_product(product_json['data'])

            # 获取更多
            self.request_ts = int(time.time())
            chengjiao_pruduct_more_authorization = '93273ef46a0b880faf4466c48f74878fhouse_code=' + str(
                i['house_code']) + 'request_ts=' + str(self.request_ts)
            # 生成证书认证
            self.generate_authorization(chengjiao_pruduct_more_authorization)
            chengjiao_more_url = 'https://app.api.lianjia.com/house/house/moreinfo?house_code=' + str(
                i['house_code']) + '&request_ts=' + str(self.request_ts)

            result_product_more = requests.get(chengjiao_more_url, headers=self.headers)

            product_json_more = json.loads(result_product_more.text, encoding='utf-8')

            self.zaishou_data_analysis.zaishou_product_moire(product_json_more)

            print result_product_more.text

    def generate_authorization(self, str):
        sha1 = hashlib.sha1(str).hexdigest()
        temp = '20170324_android:' + sha1
        Authorization = base64.b64encode(temp)
        self.headers['Authorization'] = Authorization


zaishou = zaishou()
zaishou.start()
