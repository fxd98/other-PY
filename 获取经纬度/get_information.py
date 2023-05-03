import os
import pandas as pd
import numpy as np
import re

# -*- coding:utf-8 -*-
# from pandas.tests.io.excel.test_xlrd import xlwt
import xlwt


def get_path(path):
    all_path = []
    for file1 in  os.listdir(path):
        if 'jpg' in file1:
            all_path.append(file1)
        else:
            new_path2 = path  + file1 + '/'
            for file2 in os.listdir(new_path2):
                if 'jpg' in file2:
                    all_path.append(file1 + '/' + file2)
                else:
                    new_path3 = new_path2 + file2 + '/'
                    for file3 in os.listdir(new_path3):
                        if 'jpg' in file3:
                            all_path.append(file1 + '/' + file2 + '/' + file3)
                        else:
                            new_path4 = new_path3 + file3 + '/'
                            for file4 in os.listdir(new_path4):
                                if 'jpg' in file4:
                                    all_path.append(file1 + '/' + file2 + '/' + file4)
                                else:
                                    new_path5 = new_path4 + file4 + '/'
                                    for file5 in os.listdir(new_path5):
                                        if 'jpg' in file5:
                                            all_path.append(file1 + '/' + file2 + '/' + file4 + file5)

    return all_path

# D:/FuXiaodi/####/##/BIJIE_ALL/NEW_FENGE/Image segmentation1/640/织金县/三塘镇_卫图/三塘镇_卫图_Level_18/0_33.jpg    [b'0.95', 18, 108, 154, 267]    [b'0.60', 545, 0, 585, 60]

def get_zi_xinxi(path):
    f = open(path,encoding='utf-8')
    # all_txt = np.ones([len(f.readlines()),1000])
    all_txt = []
    i = 0
    for line in f:
        if i > 0:
            new_fen = line.split('    ')
            all_txt.append(new_fen)
        i = i + 1
    return all_txt

def get_lat_lon(jpgs,data_all,zi_xinxi):

    # jpgs表示预测留下的图片位置【经过删除了】
    # data_all表示TIF文件的经纬度等信息
    # zi_xinxi表示在模型预测时记录的全部信息
    # lon  经度
    # lat 维度

    name = []
    zuo_lon = data_all['左上角经度']
    zuo_lat = data_all['左上角维度']
    weight = data_all['w - e像素分辨率 / 像素宽度']
    height = data_all['n - s像素分辨率 / 像素高度（北半球上图像为负值）']

    for i in range(data_all.shape[0]):
        name.append(data_all['位置'][i].replace('D:/FuXiaodi/####/##/BIJIE_ALL/NEW_FENGE/TIF/', ''))

    zi_all = []
    for jpg in jpgs:
        print('正在处理：',jpg)
        jpg_site = jpg[:jpg.index('/',10,)] + '.tif'
        jpg_name = re.sub('[\u4e00-\u9fa5]', '',jpg[jpg.rindex('/',):].replace('/','').replace('.jpg',''))
        tif_site = name.index(jpg_site)
        tif_jingdu = zuo_lat[tif_site]#该图片对应的左上角经度
        tif_weidu = zuo_lon[tif_site]#该图片对应的左上角维度
        tif_wei = weight[tif_site]#该图片对应的左上角宽度
        tif_hei = height[tif_site]#该图片对应的左上角高度

        hen,shu = jpg_name.split('_')
        jpg_weidu = tif_weidu + int(hen) *tif_wei#预测图片左上角经度
        jpg_jingdu  = tif_jingdu + tif_hei * (int(shu) - 1) * 200 #预测图片左上角维度
        m = 0
        for i in range(len(zi_xinxi)):
            zi_name = zi_xinxi[i][0].replace('D:/FuXiaodi/####/##/BIJIE_ALL/NEW_FENGE/NEW41/640/','')
            if zi_name in jpgs:
                zi_1 = [zi_name]
                for j in range(1,len(zi_xinxi[m])):
                    all_zi_l_l = zi_xinxi[m][j].split(', ') #预测框的信息 [b'0.58', 524, 399, 588, 507]
                    zi_zuo_shang_w = all_zi_l_l[1]
                    zi_zuo_shang_h = all_zi_l_l[2]
                    zi_yiu_xia_w = all_zi_l_l[3]
                    zi_yiu_xia_h = all_zi_l_l[4].replace(']','')

                    #计算左上角经纬度
                    zi_zuo_shang_weidu = jpg_weidu + int(zi_zuo_shang_w) * tif_wei  #维度
                    zi_zuo_shang_jingdu = jpg_jingdu + int(zi_zuo_shang_h) * tif_hei  #经度
                    #计算右下角经纬度
                    zi_yiu_xia_jingdu = jpg_jingdu - int(zi_yiu_xia_h) * tif_hei  #经度
                    zi_yiu_xia_weidu = jpg_weidu + int(zi_yiu_xia_w) * tif_wei  #维度
                    zi_1.append([zi_zuo_shang_jingdu,zi_zuo_shang_weidu,zi_yiu_xia_jingdu,zi_yiu_xia_weidu])
                zi_all.append(zi_1)
                m = m + 1
    return zi_all

def data_write(file_path, datas):
    # 方法1
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    #将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i,j,data[j])
        i = i + 1
    f.save(file_path) #保存文件

