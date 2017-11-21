# -*- coding: utf-8 -*-
import time
import requests
import base64
import hashlib

headers = {
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


class chengJiao:
    def __init__(self):
        # 爬取页数
        self.count = 5
        # 一页一共多少数据
        self.limit_count = 100
        # 第几页（页数*一页一共多少数据）
        self.limit_offset = 0
        # 当前时间
        self.request_ts = 0
        # 由android JNI逆向得出的链家apk秘钥
        # self.Authorization = '93273ef46a0b880faf4466c48f74878fcity_id=110000limit_count=10limit_offset=0request_ts=1511232061'

    def start(self):
        for i in range(self.count):
            time.sleep(1)
            self.generateAuthorization()

    def generateAuthorization(self):
        self.limit_offset = self.limit_offset + self.limit_count
        self.request_ts = str(int(time.time()))
        source_Authorization = '93273ef46a0b880faf4466c48f74878fcity_id=110000limit_count=' + str(
            self.limit_count) + 'limit_offset=' + str(self.limit_offset) + 'request_ts=' + str(self.request_ts)
        print source_Authorization

        sha1 = hashlib.sha1(source_Authorization).hexdigest()
        temp = '20170324_android:' + sha1
        Authorization = base64.b64encode(temp)
        headers['Authorization'] = Authorization

        url = 'https://app.api.lianjia.com/house/chengjiao/search?city_id=110000&limit_offset=' + str(
            self.limit_offset) + '&limit_count=' + str(self.limit_count) + '&request_ts=' + str(self.request_ts)

        print headers.get('Authorization')
        print(url)
        self.request_chengjiao(url)

    def request_chengjiao(self, url):
        result = requests.get(url, headers=headers)
        print result.text


pachong = chengJiao()
pachong.start()
