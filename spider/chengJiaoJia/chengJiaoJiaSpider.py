# -*- coding: utf-8 -*-
import time
import requests
import base64
import hashlib
import json
import sys

sys.path.append('/home/lijuntao/PycharmProjects/LianJiaSpider')

from cheng_jiao_data_analysis import cheng_jiao_data_analysis
from spider.generate_excle import generate_excle
from chengjiao_constant import chengjiao_constant
from spider.AgentAndProxies import GetIpProxy


class chengJiao:
    def __init__(self):
        # # 爬取页数
        # self.count = 300
        # # 一页一共多少数据
        # self.limit_count = 100
        # # 第几页（页数*一页一共多少数据）
        # self.limit_offset = -100
        # # 当前时间
        # self.request_ts = 0
        # 当前是第几页 从第0页开始
        self.current_page = 0
        # 由android JNI逆向得出的链家apk秘钥
        # self.Authorization = '93273ef46a0b880faf4466c48f74878fcity_id=110000limit_count=10limit_offset=0request_ts=1511232061'
        # 成交只需要Authorization网关认证
        self.headers = {
            # 'Page-Schema': 'tradedSearch%2Flist',
            # 'Referer': 'homepage%3F',
            # 'Cookie': 'lianjia_udid=6fc5da9bec827948;lianjia_token=2.007d00a43c04bd8bd26cad8d0d82a4302c;lianjia_ssid=a3c137a9-c77c-438a-a6c0-27c160707d7c;lianjia_uuid=39d20bd7-28a5-4ffa-bbac-dd70d6eaf2cd',
            # 'Lianjia-Access-Token': '2.007d00a43c04bd8bd26cad8d0d82a4302c',
            # 'User-Agent': 'HomeLink8.2.1;generic Custom+Phone+-+5.0.0+-+API+21+-+768x1280; Android 5.0',
            # 'Lianjia-Channel': 'Android_Anzhi',
            # 'Lianjia-Device-Id': '6fc5da9bec827948',
            # 'Lianjia-Version': '8.2.1',
            'Authorization': '93273ef46a0b880faf4466c48f74878fcity_id=110000limit_count=10limit_offset=0request_ts=1511232061',
            # 'Lianjia-Im-Version': '2.4.4',
            # 'Host': 'app.api.lianjia.com',
            # 'Connection': 'Keep-Alive',
            # 'Accept-Encoding': 'gzip'
        }
        self.cheng_jiao_data_analysis = cheng_jiao_data_analysis()
        self.GetIpProxy = GetIpProxy()

    def start(self):
        # 爬取页数
        self.count = input('输入请求页数:')
        # 一页一共多少数据
        self.limit_count = input('输入每页请求多少数据:')
        # 第几页（页数*一页一共多少数据） 起始数据
        self.limit_offset = input('输入请求起始数据:')
        excleName = raw_input('输入要保存的文件名称:')

        self.excle_init_title()
        for i in range(self.count):
            self.current_page = i
            # time.sleep(1)
            self.request_url_list()
        # 完成循环后保存excle
        self.generate_excle.saveExcle(excleName + '.xls')

    def request_url_list(self):
        self.limit_offset = self.limit_offset + self.limit_count
        self.request_ts = int(time.time())
        source_Authorization = '93273ef46a0b880faf4466c48f74878fcity_id=110000limit_count=' + str(
            self.limit_count) + 'limit_offset=' + str(self.limit_offset) + 'request_ts=' + str(self.request_ts)

        # print source_Authorization

        self.generate_authorization(source_Authorization)

        url = 'https://app.api.lianjia.com/house/chengjiao/search?city_id=110000&limit_offset=' + str(
            self.limit_offset) + '&limit_count=' + str(self.limit_count) + '&request_ts=' + str(self.request_ts)

        # print headers.get('Authorization')
        print(url)
        self.get_result_json_list(url)

    def get_result_json_list(self, url):
        # 替换代理模式
        # result_list = requests.get(url, headers=self.headers)
        result_list = self.GetIpProxy.requestUrlForRe(url, self.headers)

        # print result_list.text
        jsonsource = json.loads(result_list.text, encoding='utf-8')
        if jsonsource["data"]['list'] is not None:
            for index in range(len(jsonsource["data"]['list'])):
                # print jsonsource["data"]['list']
                self.request_ts = int(time.time())
                er_shou_pruduct_url_authorization = '93273ef46a0b880faf4466c48f74878fhouse_code=' + str(
                    jsonsource["data"]['list'][index]['house_code']) + 'request_ts=' + str(self.request_ts)
                # 生成证书认证
                self.generate_authorization(er_shou_pruduct_url_authorization)

                chengjiao_pruduct_url = 'https://app.api.lianjia.com/house/chengjiao/detailpart1?house_code=' + str(
                    jsonsource["data"]['list'][index]['house_code']) + '&request_ts=' + str(self.request_ts)

                # todo 网络访问增加代理请求
                # 替换代理模式
                # result_product = requests.get(er_shou_pruduct_url, headers=self.headers)
                result_product = self.GetIpProxy.requestUrlForRe(chengjiao_pruduct_url, self.headers)

                # print "result_product:" + result_product.text

                product_json = json.loads(result_product.text, encoding='utf-8')
                self.cheng_jiao_data_analysis.chengjiao_product(product_json['data'])

                # 获取更多
                self.request_ts = int(time.time())
                chengjiao_pruduct_more_authorization = '93273ef46a0b880faf4466c48f74878fhouse_code=' + str(
                    jsonsource["data"]['list'][index]['house_code']) + 'request_ts=' + str(self.request_ts)
                # 生成证书认证
                self.generate_authorization(chengjiao_pruduct_more_authorization)

                chengjiao_more_url = 'https://app.api.lianjia.com/house/house/moreinfo?house_code=' + str(
                    jsonsource["data"]['list'][index]['house_code']) + '&request_ts=' + str(self.request_ts)

                # todo 网络访问增加代理请求
                # 替换代理模式
                # result_product_more = requests.get(chengjiao_more_url, headers=self.headers)
                result_product_more = self.GetIpProxy.requestUrlForRe(chengjiao_more_url, self.headers)

                product_json_more = json.loads(result_product_more.text, encoding='utf-8')

                row = row = index + self.current_page * self.limit_count

                print 'row:' + str(row) + '   url:' + chengjiao_pruduct_url

                self.cheng_jiao_data_analysis.chengjiao_more_infos(product_json_more, row, self.generate_excle)

                # print result_product_more.text


                # print product_json['data']

    def generate_authorization(self, str):
        sha1 = hashlib.sha1(str).hexdigest()
        temp = '20170324_android:' + sha1
        Authorization = base64.b64encode(temp)
        self.headers['Authorization'] = Authorization

    def excle_init_title(self):
        self.generate_excle = generate_excle()
        self.generate_excle.addSheetExcle('chengjiao')
        self.chengjiao_constant = chengjiao_constant()
        for itemKey in self.chengjiao_constant.chengjiao_source_data.keys():
            self.generate_excle.writeExclePositon(0, self.chengjiao_constant.chengjiao_source_data.get(itemKey),
                                                  itemKey)


pachong = chengJiao()
pachong.start()
