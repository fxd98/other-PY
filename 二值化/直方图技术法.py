# 直方图技术法就是先找到这两个峰值，然后取两个峰值之间的波谷对应的灰度值，就是所要的阈值。
# 由于灰度值在直方图中的随机波动，两个波峰（局部最大值）和它们之间的波谷都不能很好的确定，
# 比如在两个峰值之间可能会出现两个最小值，所以希望通过鲁棒的方法选定与最小值对应的阈值。
# 一种常用的方法是先对直方图进行高斯平滑处理，逐渐增大高斯滤波器的标准差，
# 直到能从平滑后的直方图中得到两个唯一的波峰和它们之间唯一的最小值。
# 但这种方式需要手动调节，下面介绍一种规则自动选取波峰和波谷的方式。

# import numpy as np
# import cv2

# def threshold_two_peak(image):
#     # 计算灰度直方图
#     histogram = calcGrayHist(image)
#     # 找到灰度直方图的最大峰值对应的灰度值
#     maxLoc = np.where(histogram==np.max(histogram))
#     firstPeak = maxLoc[0][0]
#     # 寻找灰度直方图的第二个峰值对应的灰度值
#     measureDists = np.zeros([256], np.float32)
#     for k in range(256):
#         measureDists[k] = pow(k-firstPeak, 2) * histogram[k]
#     maxLoc2 = np.where(measureDists==np.max(measureDists))
#     secondPeak = maxLoc2[0][0]
#     # 找到两个峰值之间的最小值对应的灰度值，作为阈值
#     thresh = 0
#     if firstPeak > secondPeak:  # 第一个峰值在第二个峰值的右侧
#         temp = histogram[int(secondPeak):int(firstPeak)]
#         minLoc = np.where(temp==np.min(temp))
#         thresh = secondPeak + minLoc[0][0] + 1
#     else:                       # 第一个峰值在第二个峰值的右侧
#         temp = histogram[int(firstPeak):int(secondPeak)]
#         minLoc = np.where(temp==np.min(temp))
#         thresh = firstPeak + minLoc[0][0] + 1
#     # 找到阈值后进行阈值处理，得到二值图
#     threshImage = image.copy()
#     threshImage[threshImage>thresh] = 255
#     threshImage[threshImage<=thresh] = 0
#     print(firstPeak, secondPeak, thresh)
#     return thresh, threshImage
  
# def calcGrayHist(I):
#     # 计算灰度直方图
#     h, w = I.shape[:2]
#     grayHist = np.zeros([256], np.uint64)
#     for i in range(h):
#         for j in range(w):
#             grayHist[I[i][j]] += 1
#     return grayHist
# image = cv2.imread("1.jpg")
# threshold_two_peak(image)

from matplotlib import pyplot as plt
import cv2
 
img = cv2.imread(r'1.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap=plt.cm.gray)
 
#images，必须用方括号括起来。
#channels，是用于计算直方图的通道，这里使用灰度图计算直方图，所以就直接使用第一个通道。
#Mask，图像掩模，没有使用则填写None。
#histSize，表示这个直方图分成多少份（即多少个直方柱）。
#ranges，表示直方图中各个像素的值，[0.0, 256.0]表示直方图能表示像素值从0.0到256的像素。
#accumulate，为一个布尔值，用来表示直方图是否叠加。
 
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
 
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("gray Level")
plt.ylabel("number of pixels")
 
plt.plot(hist)
plt.xlim([0, 256])
plt.show()