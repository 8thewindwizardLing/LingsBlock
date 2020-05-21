import xlwt
import xlrd
import os
import sys
import re
import tkinter
import numpy as np
import pandas as pd
from tkinter import filedialog
from xlutils.copy import copy


class Log():

    
    Title = ['ID','Name','Description','Detail','ToMMS','ToATS','ToDMI','IsDisplay','RelateDevice','Level','Priority','Type','Parameter Count','Parameter Content','Parameter Remark']


    def __init__(self, filename):
        print (filename)
        #f = open(filename)

        #execl = xlwt.Workbook()

        #sheet = execl.add_sheet('日志表', cell_overwrite_ok=True)

        logInfo = pd.DataFrame(columns = self.Title)
        
        print (logInfo)
        for x in range(len(self.Title)):
            logInfo.loc[x] = 1
        print (logInfo)


        #for x in range(4):
            #sheet.write(0, i, list(xls_Info.keys())[x])
            #i += 1

   #    execl.save('测试工作.xls')
   #    count = 0
   #    countFlag = 0

   #    for line in f.readlines():
   #        if line.startswith('/** Log ID.*/'):
   #            countFlag = 1

   #        elif countFlag == 1:
   #            if line.startswith('#define'):
   #                count += 1
   #                self.Log_Info.append(line)

   #        if line.startswith('/** Offline log.*/'):
   #            countFlag = 0

   #    f.close()


def function():
    Filepath = filedialog.askopenfilename()
    print('Filepath:',Filepath)

def Rox():
    Tkwindow = tkinter.Tk()
    Tkwindow.title("日志集成工具")
    B = tkinter.Button(Tkwindow,text = "选择文件",command = function)
    B.pack()
    Tkwindow.mainloop()

if __name__ == '__main__':
    Log(os.getcwd() +"\CbiLog.h")

    
    
    
    
