import Augmentor

# 确定原始图像存储路径以及掩码文件路径
JPEG = Augmentor.Pipeline("D:/桌面/Data_augment/Bijie-landslide-dataset/landslide/image")
JPEG.ground_truth("D:/桌面/Data_augment/Bijie-landslide-dataset/landslide/mask")

# 错位变化
JPEG.shear(probability=1,max_shear_left=15,max_shear_right=15)

# 图像旋转：按照概率0.8执行，最大左旋角10，最大右旋角
JPEG.rotate(probability=0.8,max_left_rotation=10,max_right_rotation=10)

# 透视形变-斜四角形变形变：magnitude 取（0，1），指的是形变程度
JPEG.skew_corner(probability=0.3,magnitude=1)

# 最终扩充的数据样本
JPEG.sample(300)