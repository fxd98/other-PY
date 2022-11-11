import Augmentor

# 确定原始图像存储路径以及掩码文件路径
JPEG = Augmentor.Pipeline("Bijie-landslide-dataset\landslide\image")
JPEG.ground_truth("Bijie-landslide-dataset\landslide\mask")

# 图像旋转：按照概率0.8执行，最大左旋角10，最大右旋角
JPEG.rotate(probability=0.8,max_left_rotation=10,max_right_rotation=10)

# 图像左右互换：按照概率0.5执行
JPEG.flip_left_right(probability=0.5)

# 图像放大缩小：按照概率0.8执行，面积为原始图像的0.8倍
JPEG.zoom_random(probability=0.8,percentage_area=0.8)
JPEG.zoom(probability=0.3,min_factor=1.1,max_factor=1.6)

# 透视变形-垂直方向形变：magnitude 取（0，1），指的是形变程度
JPEG.skew_tilt(probability=0.7,magnitude=1)

# 透视形变-斜四角形变形变：magnitude 取（0，1），指的是形变程度
JPEG.skew_corner(probability=0.7,magnitude=1)

# 弹性扭曲，类似区域扭曲的感觉
JPEG.random_distortion(probability=1,grid_height=5,grid_width=16,magnitude=8)

# 错位变化
JPEG.shear(probability=1,max_shear_left=15,max_shear_right=15)

# 随即区域擦除
JPEG.random_erasing(probability=1,rectangle_area=0.5)

# # 亮度
# JPEG.random_brightness(probability=0.5,min_factor=0.3,max_factor=1.2)

# 颜色
JPEG.random_color(probability=1,min_factor=0,max_factor=1)

# # 对比度
# JPEG.random_contrast(probability=1,min_factor=0.7,max_factor=1.2)

# 最终扩充的数据样本
JPEG.sample(20)
JPEG.process()
