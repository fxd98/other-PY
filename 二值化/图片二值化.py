#（一）简单阈值
# cv2.threshold( )  这个函数有四个参数，第一个是原图像矩阵，第二个是进行分类的阈值，第三个是高于（低于）阈值时赋予的新值，第四个是一个方法选择参数，常用的有：

# cv2.THRESH_BINARY（黑白二值）

# cv2.THRESH_BINARY_INV（黑白二值翻转）

# cv2.THRESH_TRUNC（得到额图像为多像素值）

# cv2.THRESH_TOZERO（当像素高于阈值时像素设置为自己提供的像素值，低于阈值时不作处理）

# cv2.THRESH_TOZERO_INV（当像素低于阈值时设置为自己提供的像素值，高于阈值时不作处理）
# encoding: utf-8
 
import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from PIL import Image

def show_img(name="test",img=None):
    plt.figure()
    plt.imshow(img)
    plt.title(name)
    plt.show()
 
path = r"1.jpg"
img = cv2.imread(path,0)
 
# binary （黑白二值）0,255

ret1, thresh1 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY) 
# （黑白二值反转）255,0
ret2, thresh2 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY_INV)  
# 得到的图像为多像素值
ret3, thresh3 = cv2.threshold(img, 180, 255, cv2.THRESH_TRUNC)  
# 高于阈值时像素设置为255，低于阈值时不作处理
ret4, thresh4 = cv2.threshold(img, 180, 255, cv2.THRESH_TOZERO)  
# 低于阈值时设置为255，高于阈值时不作处理
ret5, thresh5 = cv2.threshold(img, 185, 255, cv2.THRESH_TOZERO_INV)  
 

# matplotlib.image.imsave('out/二值化.jpg',thresh5)

show_img('thresh1', thresh1)
show_img('thresh2', thresh2)
show_img('thresh3', thresh3)
show_img('thresh4', thresh4)
show_img('thresh5', thresh5)#这个处理后的图片最适合
show_img('grey-map', img)