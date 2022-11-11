# -*- coding: utf-8 -*-
import os
import shutil

path1 = r'D:/桌面/img/xiugai1/'
path2 = r'D:/桌面/img/anno/'

def file_name(image_dir,xml_dir):
    jpg_list = []
    xml_list = []
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            jpg_list.append(os.path.splitext(file)[0])
    for root, dirs, files in os.walk(xml_dir):
        for file in files:
            xml_list.append(os.path.splitext(file)[0])
    print(len(jpg_list))
    diff = set(xml_list).difference(set(jpg_list))  # 差集，在a中但不在b中的元素
    for name in diff:
        print("no jpg", name + ".xml")
    diff2 = set(jpg_list).difference(set(xml_list))  # 差集，在b中但不在a中的元素
    print(len(diff2))
    for name in diff2:
        print("no xml", name + ".jpg")
        # shutil.copy(path1 + name+ ".png", '1/' + name+ ".png")
        os.remove(path1 + name + ".jpg")
if __name__ == '__main__':

    file_name(path1,path2)
