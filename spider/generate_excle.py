# -*- coding: utf-8 -*-
import xlrd
import xlwt
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class generate_excle:
    def __init__(self):
        print sys.getdefaultencoding()
        if sys.getdefaultencoding() != 'utf-8':
            reload(sys)
            sys.setdefaultencoding('utf-8')
        self.raws = []
        self.wb = xlwt.Workbook(encoding='utf-8')

    def start(self):
        # self.write()
        list = []
        list.append("1")
        list.append("2")
        list.append("4")
        self.writeExcle(0, list)
        self.saveExcle()

    def writeExcle(self, rowNumber, list):
        for index in range(len(list)):
            self.ws.write(rowNumber, index, list[index])

    def saveExcle(self):
        self.wb.save(u'LianJiaSpider.xls')

    def addSheetExcle(self, sheetName):
        self.ws = self.wb.add_sheet(sheetName)
        # ##读文件占时未使用到
        # def readExcle(self):
        #     excleData = xlrd.open_workbook("example.xls")
        #     table = excleData.sheets()[0]
        #     # 获取整行数据
        #     tablerow = table.row_values(1)
        #     # 获取整列数据
        #     table_col = table.col_values(1)
        #     # 5、获取行数和列数　
        #     table.nrows
        #     table.ncols
        #     # 6、获取单元格
        #     table.cell(0, 0).value
        #     table.cell(0, 0).value
        #     print tablerow, table_col

# generate_excle = generate_excle()
#
# generate_excle.start()
