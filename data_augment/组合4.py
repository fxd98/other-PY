import Augmentor

# 确定原始图像存储路径以及掩码文件路径
JPEG = Augmentor.Pipeline("D:/桌面/Data_augment/Bijie-landslide-dataset/landslide/image")
JPEG.ground_truth("D:/桌面/Data_augment/Bijie-landslide-dataset/landslide/mask")

# 透视形变-斜四角形变形变：magnitude 取（0，1），指的是形变程度
JPEG.skew_corner(probability=0.7,magnitude=1)

# 图像放大缩小：按照概率0.9执行，面积为原始图像的1.6倍
JPEG.zoom(probability=0.9,min_factor=1.1,max_factor=1.6)

# 图像左右互换：按照概率0.7执行
JPEG.flip_left_right(probability=0.7)

# 最终扩充的数据样本
JPEG.sample(300)