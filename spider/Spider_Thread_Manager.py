# -*- coding: utf-8 -*-
import sys, os
import time
sys.path.append(os.path.abspath(os.path.join(sys.argv[0], "../..")))

from multiprocessing import Process
from zaishou.zaiShouSpider import zaishou
from chengJiaoJia.chengJiaoJiaSpider import chengJiao

# 在售和成交（基于移动端接口数据）加入工作线程爬虫
#
class spider_Process_Manager:
    def __init__(self):
        self.zaishou = zaishou()
        self.chengJiao = chengJiao()
        self.proc_record = []

    def works(self):
        p1 = Process(target=self.zaishou)
        p2 = Process(target=self.chengJiao)
        self.proc_record.append(p1)
        self.proc_record.append(p2)

        for p in self.proc_record:
            p.join()

    def start(self):
        self.works()


spider = spider_Process_Manager()
spider.start()
