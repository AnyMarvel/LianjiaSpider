# -*- coding: utf-8 -*-
import random
import re
import requests
from bs4 import BeautifulSoup
from generate_excle import generate_excle
from AgentAndProxies import hds
from  AgentAndProxies import GetIpProxy


class salingInfo:
    # 初始化构造函数
    def __init__(self):
        self.getIpProxy = GetIpProxy()
        self.url = "http://bj.lianjia.com/ershoufang/pg{}/"
        self.infos = {}
        self.proxyServer = ()
        # 传参使用进行excle生成
        self.list = []
        self.generate_excle = generate_excle()

    # 生成需要生成页数的链接
    def generate_allurl(self, user_in_nub):
        for url_next in range(1, int(user_in_nub) + 1):
            self.page = url_next
            yield self.url.format(url_next)

    # 开始函数
    def start(self):
        self.generate_excle.addSheetExcle(u'在售列表')
        user_in_nub = input('输入生成页数：')

        for i in self.generate_allurl(user_in_nub):
            self.get_allurl(i)

            # print(i)
        self.generate_excle.saveExcle()

    def get_allurl(self, generate_allurl):

        geturl = self.requestUrlForRe(generate_allurl)
        if geturl.status_code == 200:
            # 提取title跳转地址　对应每个商品
            re_set = re.compile('<li.*?class="clear">.*?<a.*?class="img.*?".*?href="(.*?)"')
            re_get = re.findall(re_set, geturl.text)
            for index in range(len(re_get)):
                self.open_url(re_get[index], index)
                # print re_get[index]

    def open_url(self, re_get, index):
        res = self.requestUrlForRe(re_get)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'lxml')
            self.infos['标题'] = soup.select('.main')[0].text
            self.infos['总价'] = soup.select('.total')[0].text + u'万'
            self.infos['每平方售价'] = soup.select('.unitPriceValue')[0].text
            self.list = [re_get, self.infos['标题'], self.infos['总价'], self.infos['每平方售价']]

            row = index + (self.page - 1) * 30
            self.generate_excle.writeExcle(row, self.list)
            print row, re_get, self.infos['标题'], self.infos['总价'], self.infos['每平方售价']

            return self.infos

    # 封装统一request请求,采取动态代理和动态修改User-Agent方式进行访问设置,减少服务端手动暂停的问题
    def requestUrlForRe(self, url):

        if len(self.proxyServer) == 0:
            tempProxyServer = self.getIpProxy.get_random_ip()
        else:
            tempProxyServer = self.proxyServer

        proxy_dict = {
            tempProxyServer[0]: tempProxyServer[1]
        }
        tempUrl = requests.get(url, headers=hds[random.randint(0, len(hds) - 1)], proxies=proxy_dict)

        code = tempUrl.status_code
        if code >= 200 or code < 300:
            self.proxyServer = tempProxyServer
            return tempUrl
        else:
            self.proxyServer = self.getIpProxy.get_random_ip()
            self.requestUrlForRe(url)


spider = salingInfo()
spider.start()
