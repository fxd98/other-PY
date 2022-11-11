import cv2, numpy as np, matplotlib.pyplot as plt
img = np.float32(cv2.imread('1.jpg',0)) # 将数值精度调整为32位浮点型
#----------------------------------------------------------------------------
img_dct = cv2.dct(img) # 使用dct获得img的频域图像    
plt.xticks([])
plt.yticks([]) 
plt.imshow(np.log(np.abs(img_dct)),'gray')
#---------------------------------------------------------------------------
img_back = cv2.idct(img_dct)  # 使用反dct从频域图像恢复出原图像(有损) 
plt.figure()
plt.xticks([])
plt.yticks([])
plt.imshow(img_back,'gray')