#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pykml import parser

kml_file = open("C:\\Users\\zhouwei\\Desktop\\zzs.kml", "r",encoding='UTF-8')
out_file = open("C:\\Users\\zhouwei\\Desktop\\test.txt", "w",encoding='UTF-8')

kml = parser.parse(kml_file).getroot()
for each in kml.Document.Folder.Placemark:
    out_file.write(each.name.text)
    out_file.write(each.MultiGeometry.Polygon.outerBoundaryIs.LinearRing.coordinates.text.replace(',0 ',':').replace(':\n','').replace('	',''))
    out_file.write('\n')

out_file.close()
kml_file.close()


