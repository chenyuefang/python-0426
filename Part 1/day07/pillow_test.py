#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2019/5/7 14:31
# @Author : mingfei.net@gmail.com
# @FileName : pillow_test.py
# @GitHub : https://github.com/thu/python-0426

from PIL import Image, ImageFilter

image = Image.open('1.jpg')
w, h = image.size
image.thumbnail((w//2, h//2))
image.save('new.jpg')

image = Image.open('1.jpg')
image_blur = image.filter(ImageFilter.BLUR)
image_blur.save('blur.jpg')