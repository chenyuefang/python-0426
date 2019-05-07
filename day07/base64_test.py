#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2019/5/7 10:52
# @Author : mingfei.net@gmail.com
# @FileName : base64_test.py
# @GitHub : https://github.com/thu/python-0426

import base64

s = b'Hello, World!'

print(base64.encodebytes(s))

print(base64.decodebytes(b'SGVsbG8sIFdvcmxkIQ==\n'))