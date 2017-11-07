# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from generate_excle import generate_excle

class salingInfo:
    # 初始化构造函数
    def __init__(self):
        self.url = "http://bj.lianjia.com/ershoufang/pg{}/"
        self.infos = {}

    # 生成需要生成页数的链接
    def generate_allurl(self, user_in_nub):
        for url_next in range(1, int(user_in_nub) + 1):
            yield self.url.format(url_next)

    # 开始函数
    def start(self):
        user_in_nub = input('输入生成页数：')
        for i in self.generate_allurl(user_in_nub):
            self.get_allurl(i)
            print(i)

    def get_allurl(self, generate_allurl):
        geturl = requests.get(generate_allurl)
        if geturl.status_code == 200:
            # 提取title跳转地址　对应每个商品
            re_set = re.compile('<li.*?class="clear">.*?<a.*?class="img.*?".*?href="(.*?)"')
            re_get = re.findall(re_set, geturl.text)
            for item in re_get:
                self.open_url(item)
                # print item

    def open_url(self, re_get):
        res = requests.get(re_get)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'lxml')
            self.infos['标题'] = soup.select('.main')[0].text
            self.infos['总价'] = soup.select('.total')[0].text + u'万'
            self.infos['每平方售价'] = soup.select('.unitPriceValue')[0].text
            print re_get, self.infos['标题'], self.infos['总价'], self.infos['每平方售价']

            return self.infos


# spider = salingInfo()
# spider.start()
spider=generate_excle()
spider.start()
