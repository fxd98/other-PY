# srcfile 需要复制、移动的文件
# dstpath 目的地址
import os,glob,shutil

# def mymovefile(srcfile, dstpath):  # 移动函数
#     if not os.path.isfile(srcfile):
#         print("%s not exist!" % (srcfile))
#     else:
#         fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
#         print(fname)
#         if not os.path.exists(dstpath):
#             os.makedirs(dstpath)  # 创建路径
#         shutil.move(srcfile, dstpath + fname)  # 移动文件
#         print("move %s -> %s" % (srcfile, dstpath + fname))


src_dir = 'PIC_640/'
# dst_dir = 'PIC_640/'  # 目的路径记得加斜杠
files = os.listdir(src_dir)
name_list_1_9 = ['GuiY_1_','GuiY_2_', 'GuiY_3_', 'GuiY_4_', 'GuiY_5_', 'GuiY_6_', 'GuiY_7_', 'GuiY_8_', 'GuiY_9_']
name_list = ['GuiY_10_', 'GuiY_11_', 'GuiY_12_', 'GuiY_13_', 'GuiY_14_', 'GuiY_15_', 'GuiY_16_', 'GuiY_17_', 'GuiY_18_', 'GuiY_19_','GuiY_20_', 'GuiY_21_', 'GuiY_22_']

for file in files:
    if file[-4:] == '.png':
        # print(file[:7])
        # name_img = file[:-4]
        if file[:7] in name_list_1_9:
            shutil.move(src_dir+file, os.path.join(src_dir,file[:6] , file))  # 移动文件
            print("move %s -> %s" % (src_dir + file, os.path.join(src_dir, file[:6], file)))
        else:
            shutil.move(src_dir+file, os.path.join(src_dir, file[:7] , file))  # 移动文件
            print("move %s -> %s" % (src_dir + file, os.path.join(src_dir, file[:7], file)))