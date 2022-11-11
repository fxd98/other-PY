import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread('1.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
s = np.log(np.abs(fshift))

f1shift = np.fft.ifftshift(fshift) #去中心化
img_back = np.abs(np.fft.ifft2(f1shift))

plt.subplot(1,2,1)
plt.imshow(img,'gray'),plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2)
plt.imshow(s,'gray'),plt.xticks([]), plt.yticks([])
plt.figure()
plt.subplot(1,1,1)
plt.imshow(img_back,'gray'),plt.xticks([]), plt.yticks([])
plt.show()
