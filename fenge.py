#将像素很大的图片切割成固定大小的多张图片，代码如下：
import numpy as np
import matplotlib
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None
# name = 'bridge'

def img_seg(dir):
    # j1 = 0
    files = os.listdir(dir)
    print(files)
    for file in files:
        if file[-4:] == '.tif':
            name = file[:-4]
            # j1 = j1 + 1
            # print(file)
            a, b = os.path.splitext(file)
            img = Image.open(os.path.join(dir+ file))
            # img.save("PNG/" + name + '.png')
            hight, width = img.size
            w = 640
            h = 640
            id = 1
            i = 0
            if name == 'GuiY_8' or name == 'GuiY_9':
                print(name)
                while (i + w <= hight):
                    j = 0
                    while (j + w <= width):
                        new_img = img.crop((i, j, i + w, j + h))
                        # rename = r"pic_tif/"
                        # new_img.save("pic_tif/" + name + "_" + str(j1) + "_" + str(id) + b)
                        if not os.path.exists("PIC_640/{}".format(name)):
                            save_path = os.mkdir("PIC_640/{}".format(name))
                        else:
                            save_path = "PIC_640/{}".format(name)
                        new_img.save(os.path.join(save_path , name + "_" + str(id) + '.png'))
                        id += 1
                        j += 400  #滑动步长
                    i = i + 400


if __name__ == '__main__':
    path = "TIF/"

    img_seg(path)
