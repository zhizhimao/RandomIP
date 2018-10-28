#!/usr/bin/python 
# -*- coding: utf-8 -*-
"""
创建时间：Sun Aug  5 09:42:55 2018
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：headers随机IP.py
"""
import requests
import random

url = 'http://2018.ip138.com/ic.asp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400'}
headers['X-Forwarded-For'] = (str(random.randint(1, 255))+'.')+(str(random.randint(1, 255))+'.')+(str(random.randint(1, 255))+'.')+str(random.randint(1, 255))  # 随机生成IP
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
html = response.text
print(html)
