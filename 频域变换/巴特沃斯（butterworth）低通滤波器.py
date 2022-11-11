import cv2,  numpy as np,  matplotlib.pyplot as plt
img = cv2.imread('1.jpg',0) 
height,width = img.shape
fft = np.fft.fftshift(np.fft.fft2(img))####傅里叶变换
###########################################创建模板
mask0 = np.zeros(img.shape,np.float32)
R0 = 35  #截止频率
n  = 1 #阶数
for i in range(0,height):
    for j in range(0,width):
         Rxy = ((i-height/2)**2+(j-width/2)**2)**(1/2)
         mask0[i,j]=1/(1+(Rxy/R0)**(2*n))

p0 = fft*mask0 #################################### 相乘
new0 = np.abs(np.fft.ifft2(np.fft.ifftshift(p0))) # 反变换
new0 = (new0-np.amin(new0))/(np.amax(new0)-np.amin(new0))#调整大小范围便于显示
plt.figure(),plt.imshow(img,'gray'),plt.xticks([]),plt.yticks([])
plt.figure(),plt.imshow(new0,'gray'),plt.xticks([]),plt.yticks([])
plt.show()
