import requests
import json
import re

geturl = requests.get("https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list")
partent = re.compile('{(.*?)}')

result = re.findall(partent, geturl.text)
for item in result:
    json_source = json.loads('{' + item + '}')
    protocal = json_source.get('type')
    if protocal is not None and protocal != 'socks4/5':
        print(json_source['host'])
