#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 同地名数据合并

input_file = open("C:\\Users\\zhouwei\\Desktop\\test.txt", "r",encoding='UTF-8')
output_file = open("C:\\Users\\zhouwei\\Desktop\\test1.txt", "w",encoding='UTF-8')

a = 1
list1 = []
list2 = []
for li in input_file.readlines():
    list1.append(li.strip())
for line in list1:
    if a%2 == 1:
        if line in list2:
            pos = list2.index(line)
            list2[pos+1] = list2[pos+1].strip()+'@'+list1[a]
        else:
            list2.append(line.strip())
            list2.append(list1[a])
    else:
        pass
    a = a+1
for li in list2:
    output_file.write(li+'\n')
input_file.close()
output_file.close()

