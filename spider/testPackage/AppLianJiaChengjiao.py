# encoding:utf-8
import requests
import cookielib
from spider.AgentAndProxies import GetIpProxy

cookieJar = cookielib.CookieJar()

headers = {
    'Page-Schema': 'tradedSearch%2Flist',
    'Referer': 'homepage%3F',
    'Cookie': 'lianjia_udid=6fc5da9bec827948;lianjia_token=2.007d00a43c04bd8bd26cad8d0d82a4302c;lianjia_ssid=a3c137a9-c77c-438a-a6c0-27c160707d7c;lianjia_uuid=39d20bd7-28a5-4ffa-bbac-dd70d6eaf2cd',
    'Lianjia-Access-Token': '2.007d00a43c04bd8bd26cad8d0d82a4302c',
    'User-Agent': 'HomeLink8.2.1;generic Custom+Phone+-+5.0.0+-+API+21+-+768x1280; Android 5.0',
    'Lianjia-Channel': 'Android_Anzhi',
    'Lianjia-Device-Id': '6fc5da9bec827948',
    'Lianjia-Version': '8.2.1',
    'Authorization': 'MjAxNzAzMjRfYW5kcm9pZDpkNWMxMTQ5NTQ5OGU2OGJhZjkxYWRmMjNiYzNjMjA4M2ZlMGZmZDQ1',
    'Lianjia-Im-Version': '2.4.4',
    'Host': 'app.api.lianjia.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}
str = 'https://app.api.lianjia.com/house/ershoufang/searchv4?city_id=110000&priceRequest=&limit_offset=2100&moreRequest=&communityRequset=&has_recommend=1&is_suggestion=0&limit_count=20&sugQueryStr=&comunityIdRequest=&areaRequest=&is_history=0&schoolRequest=&condition=&roomRequest=&isFromMap=false&request_ts=1511776535',

GetIpProxy = GetIpProxy()
result = requests.get(
    # 'https://app.api.lianjia.com/house/chengjiao/search?city_id=110000&limit_offset=20&limit_count=20&request_ts=1511170093',
    # 'https://app.api.lianjia.com/house/chengjiao/search?city_id=110000&limit_offset=0&limit_count=10&request_ts=1511232061',
    'https://app.api.lianjia.com/house/ershoufang/searchv4?city_id=110000&priceRequest=&limit_offset=2100&moreRequest=&communityRequset=&has_recommend=1&is_suggestion=0&limit_count=20&sugQueryStr=&comunityIdRequest=&areaRequest=&is_history=0&schoolRequest=&condition=&roomRequest=&isFromMap=false&request_ts=1511776535',
    headers=headers)

print result.text
