import geopandas
from osgeo import gdal
from pylab import *  # 支持中文
from shapely import geometry
import fiona
import rasterio as rio
import rasterio.mask
import pyproj
import sys
from osgeo import gdal
import os
mpl.rcParams['font.sans-serif'] = ['SimHei']
from openpyxl import Workbook
import os, numpy as np, pandas as pd
from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None
# 创建一个Workbook对象
work = Workbook()


def weizhi(begin,text,yuzhi):
    Height,Weight,Jing_du,Wei_du,w,n = begin
    L_Jing_du,L_Wei_du,R_Jing_du,R_Wei_du,Hei_,Wei_ = text
    all_jw = []
    for i in range(Height):
        Wei = Wei_du + (i * n)
        if abs(Wei - L_Wei_du) < yuzhi:
            all_jw.append(i)
            break

        if abs(Wei - R_Wei_du) < yuzhi:
            all_jw.append(i)
            break

    for j in range(Weight):
        Jin = Jing_du + j * w
        if abs(Jin - L_Jing_du) < 0.00007:
            all_jw.append(j)
            break

        if abs(Jin - R_Jing_du) < 0.00007:
            all_jw.append(j)
            break

    return [all_jw[2], all_jw[0],
            all_jw[1], all_jw[3]]  #先左上角后右下角，先经度后维度

def get_data(path):
    print('正在处理：', path)
    dataset = gdal.Open(path)  # 打开tif

    geo_information = dataset.GetGeoTransform()
    A1 = path
    B1 = dataset.RasterYSize
    C1 = dataset.RasterXSize
    D1 = geo_information[0]
    E1 = geo_information[3]
    F1 = geo_information[1]
    G1 = geo_information[5]
    return [A1, B1, C1, D1, E1, F1, G1]

def fenge(image,text,save_path):
    img = Image.open(image)
    save_name = text[0]
    weizhi    = text[1:]
    new_img = img.crop((int(weizhi[0][0]),
                        int(weizhi[0][1]),
                        int(weizhi[0][2]),
                        int(weizhi[0][3])))
    new_img.save(save_path + 'GC_' + save_name)

def create_shp(all_txt):
    name,L_Jing_du,L_Wei_du,R_Jing_du,R_Wei_du,Hei_,Wei_ = all_txt
    cq = geopandas.GeoSeries([geometry.Polygon([(L_Jing_du, L_Wei_du),
                                                (R_Jing_du, L_Wei_du),
                                                (R_Jing_du, R_Wei_du),
                                                (L_Jing_du, R_Wei_du)])],
                             # index=['简单面', '复杂面', 'c区'],  # 构建一个索引字段
                             crs='EPSG:4326',  # 坐标系是：WGS 1984
                             )
    cq.to_file('shp/{}.shp'.format(name),
               driver='ESRI Shapefile',
               encoding='utf-8')


def clipRasterByShapefile(src, shpdatafile, dst, nodata=0):
    # 读取shp
    with fiona.open(shpdatafile, "r") as shapefile:
        features = [feature["geometry"] for feature in shapefile]
    # 读取原始影像
    src = rio.open(src)

    # 调用函数执行裁剪
    out_image, out_transform = rio.mask.mask(src, features,
                                             all_touched=True,
                                             crop=True,
                                             nodata=nodata)
    # 元数据信息复制
    out_meta = src.meta.copy()
    out_meta.update({"driver": "GTiff",
                     "height": out_image.shape[1],
                     "width": out_image.shape[2],
                     "transform": out_transform})
    # 输出文件
    output_file = rasterio.open(dst, "w", compress="LZW", **out_meta)
    output_file.write(out_image)
    output_file.close()