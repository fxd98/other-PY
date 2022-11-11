import Augmentor

# 确定原始图像存储路径以及掩码文件路径
JPEG = Augmentor.Pipeline("D:/桌面/Data_augment/Bijie-landslide-dataset/landslide/image")
JPEG.ground_truth("D:/桌面/Data_augment/Bijie-landslide-dataset/landslide/mask")

# 弹性扭曲，类似区域扭曲的感觉
JPEG.random_distortion(probability=1,grid_height=5,grid_width=16,magnitude=8)

# 错位变化
JPEG.shear(probability=1,max_shear_left=15,max_shear_right=15)

# 图像放大缩小：按照概率0.8执行，面积为原始图像的0.8倍
JPEG.zoom(probability=0.3,min_factor=1.1,max_factor=1.6)

# 最终扩充的数据样本
JPEG.sample(300)