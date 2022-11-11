# encoding: utf-8
 
import cv2
import matplotlib.pyplot as plt
import math
import copy
import numpy as np
 
def show_img(name="test",img=None):
    plt.figure()
    plt.imshow(img)
    plt.title(name)
    plt.show()
 
path = r"1.jpg"
img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# 第一个参数为原始图像矩阵，第二个参数为像素值上限，第三个是自适应方法（adaptive method）：
#           -----cv2.ADAPTIVE_THRESH_MEAN_C:领域内均值
#           -----cv2.ADAPTIVE_THRESH_GAUSSIAN_C:领域内像素点加权和，权重为一个高斯窗口
# 第四个值的赋值方法：只有cv2.THRESH_BINARY和cv2.THRESH_BINARY_INV
# 第五个Block size：设定领域大小（一个正方形的领域）
# 第六个参数C，阈值等于均值或者加权值减去这个常数（为0相当于阈值，就是求得领域内均值或者加权值）
# 这种方法理论上得到的效果更好，相当于在动态自适应的调整属于自己像素点的阈值，而不是整幅图都用一个阈值
th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)
th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th4 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
 
show_img('img', img)
show_img('th1', th1)
show_img('th2', th2)
show_img('th3', th3)
show_img('th4', th4)