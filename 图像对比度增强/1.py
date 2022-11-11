# 绘制直方图

# 使用Matplotlib绘制函数
# matplotlib.pyplot.hist()  它直接找到histogram然后绘制
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg',0)
plt.hist(img.ravel(),256,[0,256]); plt.show()#将多维数组降位一维 numpy.ravel()返回视图，在原图操作  与numpy.flatten()返回拷贝，对原图没影响

import cv2 as cv
#全局直方图均衡化
def eaualHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)    #opencv的直方图均衡化要基于单通道灰度图像
#     cv.namedWindow('input_image', cv.WINDOW_NORMAL)
#     cv.imshow('input_image', gray)
    dst = cv.equalizeHist(gray)                #自动调整图像对比度，把图像变得更清晰
    cv.namedWindow("eaualHist_demo", cv.WINDOW_NORMAL)
    cv.imshow("eaualHist_demo", dst)
    cv2.imwrite('图像对比度增强/1.jpg',dst)
    return dst

#局部直方图均衡化
# def clahe_demo(image):
#     gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
#     clahe = cv.createCLAHE(5, (8,8))
#     dst = clahe.apply(gray)
#     cv.namedWindow("clahe_demo", cv.WINDOW_NORMAL)
#     cv.imshow("clahe_demo", dst)
# clahe_demo(src)
src=cv2.imread('1.jpg')

dst = eaualHist_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()
