#! usr/bin/env python3
# -*- coding:utf-8 -*-

# **第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

__author__ = 'jqbk'
__date__ = '2017-06-22'

import os
from PIL import Image

path = 'E:\\Software-Docs\\python_documents\\python-exercise\\play5\\背景图片\\'

print(os.listdir(path))