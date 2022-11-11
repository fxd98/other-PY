import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread('1.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
s = np.log(np.abs(fshift))
plt.imshow(s,'gray'),plt.xticks([]), plt.yticks([])
plt.show()
