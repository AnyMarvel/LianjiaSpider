# -*- coding: utf-8 -*-
import random
import re
import requests
from bs4 import BeautifulSoup
from generate_excle import generate_excle
from AgentAndProxies import hds
from AgentAndProxies import GetIpProxy
import lxml
import sys
from model.ElementConstant import ElementConstant

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class salingInfo:
    # 初始化构造函数
    def __init__(self):
        self.elementConstant = ElementConstant()
        self.getIpProxy = GetIpProxy()
        self.url = "http://bj.lianjia.com/ershoufang/pg{}/"
        self.infos = {}
        self.proxyServer = ()
        # 传参使用进行excle生成
        self.list = []
        self.generate_excle = generate_excle()
        self.elementConstant = ElementConstant()

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
            self.infos['网址'] = re_get
            self.infos['标题'] = soup.select('.main')[0].text
            self.infos['总价'] = soup.select('.total')[0].text + u'万'
            self.infos['每平方售价'] = soup.select('.unitPriceValue')[0].text

            self.infos['户型'] = soup.select('.mainInfo')[0].text
            self.infos['朝向'] = soup.select('.mainInfo')[1].text
            self.infos['大小'] = soup.select('.mainInfo')[2].text
            self.infos['楼层'] = soup.select('.subInfo')[0].text
            self.infos['装修'] = soup.select('.subInfo')[1].text
            self.infos['房子类型'] = soup.select('.subInfo')[2].text

            self.infos['小区名称'] = soup.select('.info')[0].text
            self.infos['区域'] = soup.select('.info > a')[0].text
            # infos['地区'] = soup.select('.info > a')[1].text
            self.infos['详细区域'] = soup.select('.info')[1].text
            self.infos['链家编号'] = soup.select('.info')[3].text
            self.infos['关注房源'] = soup.select('#favCount')[0].text + u"人关注"
            self.infos['看过房源'] = soup.select('#cartCount')[0].text + u"人看过"

            partent = re.compile('<li><span class="label">(.*?)</span>(.*?)</li>')
            result = re.findall(partent, res.text)

            for item in result:
                if item[0] != u"抵押信息" and item[0] != u"房本备件":
                    self.infos[item[0]] = item[1]

            # self.list = [re_get, self.infos['标题'], self.infos['总价'], self.infos['每平方售价']]

            # todo 计算页数,第一行填充key值,后续填充value值
            row = index + (self.page - 1) * 30
            print 'row:' + str(row)
            if row == 0:
                # self.list = []
                # for itemKey in self.infos.keys():
                #     self.list.append(itemKey)
                # self.generate_excle.writeExcle(0, self.list)
                for index_item in self.elementConstant.data_constant.keys():
                    self.generate_excle.writeExclePositon(0, self.elementConstant.data_constant.get(index_item),
                                                          index_item)
                # todo 修改适配excle格式的内容适配
                for itemKey in self.infos.keys():
                    if itemKey == '详细区域':
                        item_valus = self.infos.get(itemKey)
                        temps_item_valus = str(item_valus).split()
                        print temps_item_valus[0], temps_item_valus[1], temps_item_valus[2]
                        # self.generate_excle.writeExclePositon(1, self.elementConstant.data_constant.get('所属下辖区'),
                        #                                       temps_item_valus[0])
                        # self.generate_excle.writeExclePositon(1, self.elementConstant.data_constant.get('所属商圈'),
                        #                                       temps_item_valus[1])
                        # self.generate_excle.writeExclePositon(1, self.elementConstant.data_constant.get('所属环线'),
                        #                                       temps_item_valus[2])
                    else:

                        tempItemKey = self.elementConstant.unit_check_name(itemKey)
                        print tempItemKey, self.elementConstant.data_constant.get(str(tempItemKey)), itemKey

                        # self.generate_excle.writeExclePositon(1,
                        #                                       str(self.elementConstant.data_constant.get(tempItemKey)),
                        #                                       itemKey)

                        # self.wirte_source_data(1)
            else:
                row = row + 1
                self.wirte_source_data(row)
                # print str(self.list)[1:len(str(self.list)) - 1]
        return self.infos

    # 封装统一request请求,采取动态代理和动态修改User-Agent方式进行访问设置,减少服务端手动暂停的问题
    def requestUrlForRe(self, url):

        try:
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
                return self.requestUrlForRe(url)
        except Exception as e:
            self.proxyServer = self.getIpProxy.get_random_ip()
            s = requests.session()
            s.keep_alive = False
            return self.requestUrlForRe(url)

    # 源数据生成,写入excle中,从infos字典中读取数据,放置到list列表中进行写入操作,其中可修改规定写入格式
    def wirte_source_data(self, row):
        self.list = []
        for itemKey in self.infos.keys():
            if str(itemKey) == '每平方售价':
                item_value = self.infos.get(itemKey)[0:self.infos.get(itemKey).index('元')]
            else:
                item_value = self.infos.get(itemKey)
            self.list.append(item_value)
        self.generate_excle.writeExcle(row, self.list)


spider = salingInfo()
spider.start()
