# 中值滤波是一种常用的图像降噪方法，对于一幅带噪声的图像 1（设分辨率为 w×h），降噪方法如下：
# 　　1）将图像1转换成灰度图，仍称为图像1；
# 　　2）新建图像2，图像2为灰度图，分辨率与图像1相同；
# 　　3）对于图像 1 中坐标为 (x,y) 的像素 p，求 p 的中值 c，然后将图像 2 中 (x,y) 处的像素值设置成 c，其中，1≤x≤w−2、1≤y≤h−2；
# 　　4）保存图像 2，图像 2 即存放了降噪后的结果
from PIL import Image


# 求图像img中(x,y)处像素的中值c
def median(img, x, y):
    ########## Begin ##########
    L = []
    xl = [x-1,x,x+1]
    yl = [y-1,y,y+1]
    for i in xl:
        for j in yl:
            gray = img.getpixel((i, j))  # 取出灰度值
            L.append(gray)
    L.sort()
    c = L[4]
    ########## End ##########
    return c


# 对图像文件1进行降噪，并将结果保存为图像文件2
# 图像文件1和2的路径分别为path1和path2
def denoise(path1, path2):
    img1 = Image.open(path1)  # 图像1
    img1 = img1.convert('L')  # 将图像1转换为灰度图
    w, h = img1.size
    img2 = Image.new('L', (w, h), 'white')  # 图像2
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            c = median(img1, x, y)  # 求中值
            img2.putpixel((x, y), c)  # 将灰度设置为中值
    img2.save(path2)


path1 = '1.jpg'  # 带噪声的图像
path2 = '图像降噪/图像降噪.jpg'  # 降噪后的图像
denoise(path1, path2)

