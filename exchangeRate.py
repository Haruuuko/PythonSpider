#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import urllib2
import re
import os

response = urllib2.urlopen('http://www.boc.cn/sourcedb/whpj/')
content = response.read()

money = u'欧元'.encode('utf-8')
pattern = re.compile('<td>'+money+'</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>(.*?)</td>.*?<td>.*?</td>.*?<td>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)

items = re.findall(pattern,content)
title = ['现汇卖出价','发布时间']

date = datetime.date.today().strftime('%Y%m%d')

fileExist = os.path.isfile('/Users/Haruko/Desktop/Python_code/bankRate'+date)

for item in items: 
    print item
    bankFile = open('/Users/Haruko/Desktop/Python_code/bankRate'+date,'a+')

    if not fileExist:
        bankFile.write(money+'\n'+'  '.join(title)+'\n')
    
    bankFile.write('      '.join(item)+'\n')  
    bankFile.close()

