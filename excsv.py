#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import csv
def add(info):
    info=map(unicode,info)
    with open('torrentinfo.csv', 'ab') as f:
        f.write(u'\ufeff'.encode('utf8'))
        w = csv.writer(f)
        w.writerow([item.encode('utf8') for item in info])

