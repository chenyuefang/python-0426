#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2019/5/7 10:42
# @Author : mingfei.net@gmail.com
# @FileName : datetime_test.py
# @GitHub : https://github.com/thu/python-0426

from datetime import datetime, timedelta

print(datetime.now())
print(type(datetime.now()))

now = datetime(2019, 5, 7, 11, 0, 0)
print(now)

print(now.timestamp())

print(datetime.fromtimestamp(1543249292.559023))
print(datetime.utcfromtimestamp(1543249292.559023))

time = '1987-09-23 00:00:00'
print(datetime.strptime(time, '%Y-%m-%d %H:%M:%S'))

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

print(now)
print(now - timedelta(days=1))