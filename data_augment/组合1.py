import Augmentor

# 确定原始图像存储路径以及掩码文件路径
JPEG = Augmentor.Pipeline("D:/FuXiaodi/####/PY/data_augment/jpeg/4")
# JPEG.ground_truth("D:/桌面/Data_augment/Bijie-landslide-dataset/landslide/mask")

# # 颜色
# JPEG.random_color(probability=1,min_factor=0,max_factor=1)

# 透视形变-斜四角形变形变：magnitude 取（0，1），指的是形变程度
JPEG.skew_corner(probability=1,magnitude=1)
#
# # 图像放大缩小：按照概率0.8执行，面积为原始图像的0.8倍
# JPEG.zoom(probability=1,min_factor=1.1,max_factor=1.6)

# 最终扩充的数据样本
JPEG.sample(3)