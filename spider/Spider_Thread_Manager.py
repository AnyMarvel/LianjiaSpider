# -*- coding: utf-8 -*-
from multiprocessing import Process
import sys, os
import time
from zaishou.zaiShouSpider import zaishou
from chengJiaoJia.chengJiaoJiaSpider import chengJiao


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
