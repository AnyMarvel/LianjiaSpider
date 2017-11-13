# -*- coding: utf-8 -*-
# Some User Agents
# Agents  And proxies

import random
import re
import requests

hds = [{'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}, \
       {
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}, \
       {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}, \
       {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'}, \
       {
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}, \
       {
           'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}, \
       {
           'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}, \
       {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}, \
       {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}, \
       {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}, \
       {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}, \
       {'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'}, \
       {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]


# geturl = requests.get('http://www.xicidaili.com/', headers=hds[random.randint(0, len(hds) - 1)])
#
# # partent = re.compile('<tr class=.*?>.*?<td class="country"><img src=.*?td>(.*?)</tr>', re.S)
# partent = re.compile('<tr class=.*?>.*?<td class="country"><img src=.*?td>.*?<td>(.*?)'
#                      '</td>.*?<td>(.*?)</td>.*?td>.*?<td>(.*?)<.*?</tr>', re.S)
#
# result = re.findall(partent, geturl.text)
# infos = {}
# for item in result:
#     if item[2] != "socks4/5":
#         print u"地址:" + item[0], u"端口:" + item[1], u"协议:" + item[2]
#

class GetIpProxy():
    def __init__(self):
        self.infos = {}
        self.getIpPool()

    def getIpPool(self):
        geturl = requests.get('http://www.xicidaili.com/', headers=hds[random.randint(0, len(hds) - 1)])
        # partent = re.compile('<tr class=.*?>.*?<td class="country"><img src=.*?td>(.*?)</tr>', re.S)
        partent = re.compile('<tr class=.*?>.*?<td class="country"><img src=.*?td>.*?<td>(.*?)'
                             '</td>.*?<td>(.*?)</td>.*?td>.*?<td>(.*?)<.*?</tr>', re.S)
        result = re.findall(partent, geturl.text)
        for item in result:
            if item[2] != "socks4/5":
                # print u"地址:" + item[0], u"端口:" + item[1], u"协议:" + item[2]
                proxy_utl = '{0}://{1}:{2}'.format(item[2], item[0], item[1])
                self.infos[proxy_utl.lower()] = item[2].lower()

    def judge_ip(self, proxy_url, protocol):
        # 判断给出的代理 ip 是否可用
        http_url = 'http://www.163.com/'

        print("proxy_url", proxy_url)
        try:
            proxy_dict = {
                protocol: proxy_url
            }
            response = requests.get(http_url, proxies=proxy_dict, timeout=2)

        except Exception as e:
            print("[没有返回]代理{0} 端口号及ip不可用".format(proxy_url))
            return False
        else:
            code = response.status_code
            if code >= 200 or code < 300:
                print("代理  {0} 端口号及ip 可用".format(proxy_url))
                return True
            else:
                print("[有返回，但是状态码异常]代理 {0} 端口号及ip不可用".format(proxy_url))
                return False

    def get_random_ip(self):
        for i in range(len(self.infos.keys())):
            judge_ip_status = self.judge_ip(self.infos.keys()[i], self.infos.values()[i])
            if judge_ip_status:

                return self.infos.values()[i]


getIpProxy = GetIpProxy()
getIpProxy.get_random_ip()
