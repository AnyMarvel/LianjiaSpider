# -*- coding: utf-8 -*-
import re
import requests


class LianjiaSpider:
    # 初始化构造函数
    def __init__(self):
        self.url = "http://bj.lianjia.com/ershoufang/pg{}/"
        self.infos = []

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
            # re_set = re.compile('<li.*?class="clear">.*?<a.*?class="img.*?".*?href="(.*?)"')
            re_set = re.compile(
                '<li class=\"clear.*?href=\"(.*?)\".*?region\">(.*?)<\/a>(.*?)<.*?span>(.*?)<.*?taxfree\">(.*?)<.*?totalPrice'
                '\"><span>(.*?)<.*?<span>(.*?)<')

            re_get = re.findall(re_set, geturl.text)
            for item in re_get:
                print item[0], item[1], item[2], item[3], item[4], item[5] + u"万", item[6]


spider = LianjiaSpider()
spider.start()
