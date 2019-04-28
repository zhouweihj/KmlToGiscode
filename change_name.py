#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 按表格改地名
import xlrd
input_file1 = open("C:\\Users\\zhouwei\\Desktop\\bbb.txt", "r",encoding='UTF-8')
input_file2 = xlrd.open_workbook("C:\\Users\\zhouwei\\Desktop\\aaa.xlsx")
output_file = open("C:\\Users\\zhouwei\\Desktop\\test5.txt", "w",encoding='UTF-8')

a = 1
dict1 = {}
list1 = []
# 将表格提取为ditc数据
table1 = input_file2.sheet_by_name('Sheet1')
for r in range(table1.nrows):
    key1 = table1.cell_value(r,0)
    value1 = table1.cell_value(r,1)
    dict1[key1] = value1
# 文件中的地名与ditc匹配
for line in input_file1.readlines():
    if a%2 == 1:
        if line.strip() in dict1.keys():
            output_file.write(dict1[line.strip()] + "\n")
        else:
            output_file.write('注意：'+line)
    else:
        output_file.write(line)
    a = a+1

input_file1.close()
output_file.close()

