import cv2,  numpy as np,  matplotlib.pyplot as plt
img = cv2.imread('1.jpg',0) 
height,width = img.shape
fft = np.fft.fftshift(np.fft.fft2(img))####傅里叶变换
########################################创建模板
mask1 = np.ones(img.shape,np.uint8)  ###全1矩阵
r=4
for i in range(0,height):
    for j in range(0,width):
        if ((i-height/2)**2+(j-width/2)**2)<r**2:
            mask1[i,j]=0
p0 = fft*mask1 #################################相乘
new0 = np.abs(np.fft.ifft2(np.fft.ifftshift(p0)))
#调整大小范围便于显示
new0 = (new0-np.amin(new0))/(np.amax(new0)-np.amin(new0))
plt.figure(),plt.imshow(img,'gray'),plt.xticks([]),plt.yticks([])
plt.figure(),plt.imshow(new0,'gray'),plt.xticks([]),plt.yticks([])
plt.show()
