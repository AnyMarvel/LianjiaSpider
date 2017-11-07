# -*- coding: utf-8 -*-
import re
import requests

url = "https://bj.lianjia.com/ershoufang/pg2/"

geturl = requests.get(url)
re_set = re.compile('<li.*?class="clear">.*?<a.*?class="img.*?".*?href="(.*?)"')
re_get = re.findall(re_set, geturl.text)
print re_get
