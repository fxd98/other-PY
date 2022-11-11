import Augmentor

# 确定原始图像存储路径以及掩码文件路径
JPEG = Augmentor.Pipeline("D:/FuXiaodi/####/PY/data_augment/jpeg")
# JPEG.ground_truth("D:/桌面/Data_augment/Bijie-landslide-dataset/landslide/mask")

# # 弹性扭曲，类似区域扭曲的感觉
JPEG.random_distortion(probability=1,grid_height=5,grid_width=16,magnitude=8)

# 图像旋转：按照概率0.8执行，最大左旋角10，最大右旋角
# JPEG.rotate(probability=1,max_left_rotation=10,max_right_rotation=10)

# # 颜色
JPEG.random_color(probability=1,min_factor=0,max_factor=1)

# 最终扩充的数据样本
JPEG.sample(10)