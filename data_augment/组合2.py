import Augmentor

# 确定原始图像存储路径以及掩码文件路径
JPEG = Augmentor.Pipeline("D:/FuXiaodi/####/PY/data_augment/jpeg")
# JPEG.ground_truth("D:/桌面/Data_augment/Bijie-landslide-dataset/landslide/mask")

# 图像左右互换：按照概率0.5执行
JPEG.flip_left_right(probability=1)

# 错位变化
JPEG.shear(probability=1,max_shear_left=15,max_shear_right=15)

# 图像左右互换：按照概率0.5执行
JPEG.flip_left_right(probability=0.5)

# 最终扩充的数据样本
JPEG.sample(10)