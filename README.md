# 链家 （python）爬虫  成交数据 及 在售数据 爬取

开源地址：
#前言：链家数据爬虫，本文采用两种方式

1.常见的分析PC端HTML进行数据爬取（简单实现在售数据爬取，成交数据需要在移动端查看）

2.破解链家移动端签名密钥，使用客户端接口进行爬取（在售数据及成交数据爬取）

实现功能：

一. web界面爬取

爬取web界面在售内容 https://bj.lianjia.com/ershoufang/ 仅爬取在售内容

```
python LianjiaSpider/spider/salingInfoSpider.py

```

二.移动端数据爬取（在售，成交）

基于链家app:https://bj.lianjia.com/ 针对其签名校验进行破解

获取对应的json内容，进行自动爬取（仅做技术交流，请勿进行商业应用或其他侵权行为）

在售数据爬取：
```
python LianjiaSpider/spider/zaishou/zaiShouSpider.py
```
成交数据爬取：
```
python LianjiaSpider/spider/zaishou/chengJiaoJiaSpider.py
```


在售及成交数据自动爬取：
```
python LianjiaSpider/spider/Spider_Thread_Manager.py
```
