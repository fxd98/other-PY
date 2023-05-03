import pandas as pd
from get_information import get_path, get_lat_lon, get_zi_xinxi, data_write

data_all = pd.read_excel('毕节市--图片信息.xlsx')

# path_frcnn = 'frcnn/'
path_ssd   = 'D:/FuXiaodi/####/##/#object_dection/yuce/ssd-pytorch/pred_4.10/640/'
path_yolov3   = 'D:/FuXiaodi/####/##/#object_dection/yuce/yolo3-pytorch/pred_4.10/640/'
path_yolov6   = 'D:/FuXiaodi/####/##/#object_dection/yuce/yolov5-v6.1-pytorch/pred_4.10/640/'

# 获取所有预测子图片名称、位置
# all_jpg_frcnn = get_path(path_frcnn)
all_jpg_ssd  = get_path(path_ssd)
all_jpg_yolov3 = get_path(path_yolov3)
all_jpg_yolov6 = get_path(path_yolov6)


# 获取预测结果位置信息
# frcnn_note = 'txt/notes_frcnn.txt'
ssd_note   = 'txt/notes_ssd.txt'
yolov3_note= 'txt/notes_yolov3.txt'
yolov6_note= 'txt/notes_yolov6.txt'

zi_xinxi_ssd = get_zi_xinxi(ssd_note)
zi_xinxi_yolov3 = get_zi_xinxi(yolov3_note)
zi_xinxi_yolov6 = get_zi_xinxi(yolov6_note)

ssd_all = pd.DataFrame(get_lat_lon(all_jpg_ssd,data_all,zi_xinxi_ssd))
ssd_all.to_excel("ssd--图片信息.xlsx")

yolov3_all = pd.DataFrame(get_lat_lon(all_jpg_yolov3,data_all,zi_xinxi_yolov3))
yolov3_all.to_excel("yolov3--图片信息.xlsx")

yolov6_all = pd.DataFrame(get_lat_lon(all_jpg_yolov6,data_all,zi_xinxi_yolov6))
yolov6_all.to_excel("yolov6--图片信息.xlsx")
print('表已经生成')

