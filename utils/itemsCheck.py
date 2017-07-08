#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/3 下午5:13
# @Author  : mrlittlepig
# @Site    : www.mrlittlepig.xyz
# @File    : itemsCheck.py
# @Software: PyCharm Community Edition

import numpy
import cv2
from PIL import Image


image_dir = './items.jpg'

# 灰度打开
image = Image.open(image_dir).convert('L')
img_ndarray = numpy.asarray(image, dtype='float32')
shape = img_ndarray.shape

# 二值化
for r in range(shape[0]):
    for c in range(shape[1]):
        if img_ndarray[r][c] <= 195:
            img_ndarray[r][c] = 0
        else:
            img_ndarray[r][c] = 255


# 计算连通域
img = cv2.imread(image_dir)
n = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(n)


tm_img = Image.fromarray(img_ndarray)
Image._show(tm_img)