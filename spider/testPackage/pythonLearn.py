# -*- coding: utf-8 -*-

# 字符串截取
s = '86426元/平米'
s = s[0:s.index('元')]
print s

d = u'朝阳 垡头 四至五环'
# d = 'abc defg'
temp = d.split()

print temp[0], temp[1], temp[2]
