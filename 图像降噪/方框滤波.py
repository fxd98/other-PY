# 我们只需要在均值滤波函数的基础上，增加一个normalize参数，
# 通过normalize参数进行分支语句判断，实现对方框滤波函数的功能编写！

import cv2
import numpy as np
#方框滤波
# 自定义方框滤波函数
# def boxFiltering1(img, size,normalize): #img输入，size均值滤波器的尺寸，>=3，且必须为奇数
#     num = int((size - 1) / 2)  # 输入图像需要填充的尺寸
#     img = cv2.copyMakeBorder(img, num, num, num, num, cv2.BORDER_REPLICATE)#对传入的图像进行扩充，尺寸为num
#     h1, w1 = img.shape[0:2]
#     # 高斯滤波
#     img1 = np.zeros((h1, w1, 3), dtype="uint8") #定义空白图像，用于输出中值滤波后的结果
#     for i in range(num, h1-num): #对扩充图像中的原图进行遍历
#         for j in range(num, w1-num):
#             sum=0
#             sum1=0
#             sum2=0
#             for k in range(i-num,i+num+1):  #求中心像素周围size*size区域内的像素的平均值
#                 for l in range(j-num,j+num+1):
#                     sum=sum+img[k,l][0] #B通道
#                     sum1=sum1+img[k,l][1] #G通道
#                     sum2=sum2+img[k,l][2]  #R通道
#             if normalize==True:#均一化处理，和均值滤波一样，除以25
#                 sum = sum / (size ** 2)
#                 sum1 = sum1 / (size ** 2)
#                 sum2 = sum2 / (size ** 2)
#             else: #非均一化处理，溢出部分设置为255
#                 if sum2>255:
#                     sum2=255
#                 else:
#                     sum=sum2
#                 if sum1 > 255:
#                     sum1 = 255
#                 else:
#                     sum1 = sum1
#                 if sum>255:
#                     sum=255
#                 else:
#                     sum=sum
#             img1[i, j]=[sum,sum1,sum2] #复制给空白图像
#     img1=img1[(0+num):(h1-num),(0+num):(h1-num)] #从滤波图像中裁剪出原图像
#     return img1
# #读取图像
# img=cv2.imread("g.jpg")
# #获取图像属性
# h, w = img.shape[0:2]
# #加噪声
# for i in range(3000):    #添加3000个噪声点
#     x = np.random.randint(0, h) 
#     y = np.random.randint(0, w)    
#     img[x,y,:] = 255
# #调用均值滤波函数
# result=boxFiltering1(img, 5,normalize=True) #传入读取的图像和核尺寸
# result1=boxFiltering1(img, 5,normalize=False) #传入读取的图像和核尺寸
# cv2.imshow("src",img)
# cv2.imshow("JunYIHua",result)
# cv2.imshow("NoJunYIHua",result1)
# cv2.waitKey(0)

#方框滤波OpenCV库
import cv2
import numpy as np
#读取图像
img=cv2.imread("1.jpg")
#获取图像属性
h, w = img.shape[0:2]
#加噪声
for i in range(3000):    #添加3000个噪声点
    x = np.random.randint(0, h) 
    y = np.random.randint(0, w)    
    img[x,y,:] = 255
#调用均值滤波函数
result=cv2.boxFilter(img, -1, (5,5), normalize=1) #传入读取的图像和核尺寸
result1=cv2.boxFilter(img, -1, (5,5), normalize=0) #传入读取的图像和核尺寸
cv2.imshow("src",img)
cv2.imshow("JunYIHua-opencv",result)
cv2.imshow("NoJunYIHua-opencv",result1)
cv2.waitKey(0)
