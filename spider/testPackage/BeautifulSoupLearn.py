# -*- coding: utf-8 -*-
import re

import bs4
import requests
from bs4 import BeautifulSoup
import lxml

infos = {}
res = requests.get('https://bj.lianjia.com/ershoufang/101102204027.html')
list = []
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'lxml')
    infos['标题'] = soup.select('.main')[0].text
    infos['总价'] = soup.select('.total')[0].text + u'万'
    infos['每平方售价'] = soup.select('.unitPriceValue')[0].text
    infos['户型'] = soup.select('.mainInfo')[0].text
    infos['朝向'] = soup.select('.mainInfo')[1].text
    infos['大小'] = soup.select('.mainInfo')[2].text
    infos['楼层'] = soup.select('.subInfo')[0].text
    infos['装修'] = soup.select('.subInfo')[1].text
    infos['房子类型'] = soup.select('.subInfo')[2].text

    infos['小区名称'] = soup.select('.info')[0].text
    infos['区域'] = soup.select('.info > a')[0].text
    # infos['地区'] = soup.select('.info > a')[1].text
    infos['详细区域'] = soup.select('.info')[1].text
    infos['链家编号'] = soup.select('.info')[3].text
    infos['关注房源'] = soup.select('#favCount')[0].text + u"人关注"
    infos['看过房源'] = soup.select('#cartCount')[0].text + u"人看过"

    partent = re.compile('<li><span class="label">(.*?)</span>(.*?)</li>')
    result = re.findall(partent, res.text)

    for item in result:
        if item[0] != u"抵押信息" and item[0] != u"房本备件":
            infos[item[0]] = item[1]
            # print item[0], item[1]
    # infos['房屋特点介绍'] = soup.select('div[class="introContent showbasemore"]')[0].text

    for i in range(len(infos)):
        print infos.keys()[i], infos.get(infos.keys()[i])


        # print infos['标题'], infos['总价'], infos['每平方售价'], infos['户型'], infos['朝向'], infos['楼层'], infos['装修'], infos['房子类型'], \
        #     infos['小区名称'], infos['区域'], infos['链家编号'], infos['详细区域']
