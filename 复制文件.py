import os,shutil
from random import sample

path_jpeg = r'D:/桌面/Data_augment/all/JPEG'
path_mask = r'D:/桌面/Data_augment/all/MASK'

#获取该目录下所有文件，存入列表中
fileList_JPEG = os.listdir(path_jpeg)
fileList_MASK = os.listdir(path_mask)
name_all = []
for name in fileList_JPEG:
    if name not in name_all:
        name_all.append(name)
print('需要移动的图片数量为：',len(name_all))

train_num = 0.8
test_num  = 0.2

train_list = sample(name_all,int(len(name_all) * train_num))
test_list  = []
for name in name_all:
    if name not in train_list:
        test_list.append(name)
print('训练集数量：',len(train_list))
print('测试集数量：',len(test_list))


# 开始复制文件
# 训练集
train_jpeg = 'D:/桌面/Data_augment/all/train/JPEG'
train_mask = 'D:/桌面/Data_augment/all/train/MASK'
train_jpeg_file = os.listdir(train_jpeg)
train_mask_file = os.listdir(train_mask)
for name in train_list:
    if name not in train_jpeg_file:
        shutil.copy(path_jpeg + '/' + name,train_jpeg + '/' + name)
        shutil.copy(path_mask + '/' + name, train_mask + '/' + name)
print('训练集复制完成')

# 测试集
test_jpeg = 'D:/桌面/Data_augment/all/test/JPEG'
test_mask = 'D:/桌面/Data_augment/all/test/MASK'
test_jpeg_file = os.listdir(test_jpeg)
test_mask_file = os.listdir(test_mask)
for name in test_list:
    if name not in test_jpeg_file:
        shutil.copy(path_jpeg + '/' + name,test_jpeg + '/' + name)
        shutil.copy(path_mask + '/' + name, test_mask + '/' + name)

print('测试集复制完成')