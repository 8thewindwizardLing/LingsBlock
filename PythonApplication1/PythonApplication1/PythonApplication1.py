import xlwt
import xlrd
import os
import sys
import re
from xlutils.copy import copy 

class Log():

    Log_Info = []

    def __init__(self,filename):
        
        f = open(filename)
        execl = xlwt.Workbook()
        sheet = execl.add_sheet('日志表',cell_overwrite_ok=True)
        
        Name = []
        ID = []
        Description = []
        Detail = []
        i = 0

        xls_Info = {'ID':ID,'Name':Name,'Description':Description,'Detail':Detail}

        for x in range(4):
            sheet.write(0,i,list(xls_Info.keys())[x])
            i += 1
        
        execl.save('E:\开发\Python Scripts\测试工作.xls')
        
        count = 0
        countFlag = 0

        for line in f.readlines():
            if line.startswith('/** Log ID.*/'):
                countFlag = 1
            elif countFlag == 1:
                if line.startswith('#define'):
                    count += 1
                    self.Log_Info.append(line)
            
            if line.startswith('/** Offline log.*/'):
                countFlag = 0
        print(self.Log_Info)

        f.close()





if __name__ == '__main__':
    filename = 'E:\开发\Python Scripts\CbiLog.h'
    log = Log(filename)

