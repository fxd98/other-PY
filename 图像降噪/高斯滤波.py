import cv2
import numpy as np
import math

# 定义高斯核函数，计算高斯核
#计算高斯卷积核
# def gausskernel(size):
#     sigma = 1.0 #设置σ=1.0
#     gausskernel = np.zeros((size, size), np.float32) #通过传递的参数尺寸设置高斯核模板
#     for i in range(size): #对高斯核进行遍历
#         for j in range(size):
#             norm = math.pow(i - 1, 2) + pow(j - 1, 2) #求解x平方加y平方的值
#             gausskernel[i, j] = math.exp(-norm / (2 * math.pow(sigma, 2)))  # 求高斯卷积
#     sum = np.sum(gausskernel)  # 求和
#     kernel=gausskernel/sum # 归一化
#     return kernel

# #自定义高斯滤波函数
# def Gaussian(img,size):
#     num = int((size - 1) / 2)  # 输入图像需要填充的尺寸
#     img = cv2.copyMakeBorder(img, num, num, num, num, cv2.BORDER_REPLICATE)#对原图像进行扩充，处理黑边
#     h, w = img.shape[0:2]  # 获取输入图像的长宽和高
#     # 高斯滤波
#     img1 = np.zeros((h, w, 3), dtype="uint8")
#     kernel =gausskernel(size)  # 计算高斯卷积核
#     for i in range(num, h - num):
#         for j in range(num, w - num):
#             sum = 0
#             q=0
#             p=0
#             for k in range(i-num, i+num+1):
#                 for l in range(j-num, j+num+1):
#                     sum = sum + img[k,l] * kernel[q,p]  # 高斯滤波
#                     p=p+1 #进行高斯核的列计数
#                 q=q+1 #进行高斯核的行计数
#                 p=0#内层循环执行完毕，将列计数为0，下次循环便可以再次从0开始
#             img1[i, j] = sum
#     img1 = img1[(0 + num):(h-num), (0+num):(h-num)]#裁剪原图
#     return img1

# #读取图像
# img=cv2.imread("1.jpg")
# #获取图像属性
# h, w = img.shape[0:2]
# #加噪声
# for i in range(3000):    #添加3000个噪声点
#     x = np.random.randint(0, h) 
#     y = np.random.randint(0, w)    
#     img[x,y,:] = 255
# #调用OpenCV库函数中的均值滤波函数
# result=Gaussian(img, 5) #传入读取的图像和核尺寸
# cv2.imshow("src",img)
# cv2.imshow("Gaussian",result)
# cv2.waitKey(0)

#OpenCV高斯滤波库函数使用
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
#调用OpenCV库函数中的高斯滤波函数
result=cv2.GaussianBlur(img,(5,5),1,1) #传入读取的图像和核尺寸
cv2.imshow("src",img)
cv2.imshow("GaussianBlur-opencv",result)
cv2.waitKey(0)
