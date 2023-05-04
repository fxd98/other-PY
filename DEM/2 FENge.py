from pylab import *  # 支持中文
from all import *
import os
mpl.rcParams['font.sans-serif'] = ['SimHei']
from openpyxl import Workbook
from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None
# 创建一个Workbook对象
work = Workbook()

path = '毕节/坡向.tif'
shp_all = 'shp/'


# # 第一、创建shp文件[可以使用]
# data_all = pd.read_excel('use.xlsx').values
# for i in range(0,data_all.shape[0]):
#     create_shp(data_all[i])

# # # 第二、 获得栅格图
# for file in os.listdir(shp_all):
#     if file[-3:] == 'shp':
#         if file[:-4] != 'Rectangle_#22_卫图_Level_19.tif':
#             print('正在处理文件:',file[:-4])
#             clipRasterByShapefile(path,shp_all + file,dst='all/坡向/PX_{}'.format(file[:-4]))

# 第三、改变图片大小
path_all = 'all/'
files = os.listdir(path_all)
data_all = pd.read_excel('use.xlsx')
for file in files:
    if '.tif' not in file:
        new_path = path_all + file + '/'
        for image in os.listdir(new_path):
            if '.tif' in image:
                print('正在处理', image)
                a,b = image.split('_',1)
                site = data_all['位置'].values.tolist().index(b)
                Height = data_all['图片高度'].values[site]
                Weight = data_all['图片宽度'].values[site]

                im = Image.open(new_path + image)
                out = im.resize((Weight,Height), Image.ANTIALIAS)
                out.save(new_path + image)