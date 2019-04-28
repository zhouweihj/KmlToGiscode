#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 将长字段按4k字节截成多段,并拼接成sql

input_file = open("C:\\Users\\zhouwei\\Desktop\\test1.txt", "r",encoding='UTF-8')
output_file = open("C:\\Users\\zhouwei\\Desktop\\sql.txt", "w",encoding='UTF-8')

a = 1
b = ''

for line in input_file.readlines():
    length = int(len(line)/4000)
    if a%2 == 1:
        b = line
        output_file.write('/*'+b.strip()+'*/\n')
    else:
        for i in range(length+1):
            output_file.write('update td_sm_organization set remark1=remark1||\'')
            output_file.write(line[4000*i:4000*(i+1)].strip())
            output_file.write('\' where org_name=\'')
            output_file.write(b.strip())
            output_file.write('\';\n')
        output_file.write('commit;\n')
    a = a+1
input_file.close()
output_file.close()

