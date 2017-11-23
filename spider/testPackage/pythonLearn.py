# -*- coding: utf-8 -*-

# # 字符串截取
# s = '86426元/平米'
# s = s[0:s.index('元')]
# print s
#
# d = u'朝阳 垡头 四至五环'
# # d = 'abc defg'
# temp = d.split()
#
# print temp[0], temp[1], temp[2]



# import base64
# import hashlib
import time

##链家加密处理
# str = '93273ef46a0b880faf4466c48f74878fhouse_code=101101703001request_ts=1511334292'
# sha1 = hashlib.sha1(str).hexdigest()
#
# temp = '20170324_android:' + sha1
#
# print base64.b64encode(temp)
# # 打印当前时间
# print int(time.time())

# 时间格式化
print time.strftime('%Y-%m-%d', time.localtime(1504863733))
