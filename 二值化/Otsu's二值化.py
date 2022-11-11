# encoding: utf-8
 
import cv2
import matplotlib.pyplot as plt
import math
import copy
import numpy as np
 
path = r"1.jpg"
img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#简单滤波
ret, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Otsu 滤波
ret2, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
 
plt.figure()
plt.subplot(221), plt.imshow(gray,'gray')
# .ravel方法将矩阵转化为一维,画出灰度直方图
plt.subplot(222), plt.hist(gray.ravel(), 256)
plt.subplot(223), plt.imshow(th1,'gray')
plt.subplot(224), plt.imshow(th2,'gray')
plt.show()