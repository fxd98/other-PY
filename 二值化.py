import cv2,os
path = 'train/SegmentationClass/'
new_path = 'train/new/'
files = os.listdir(path)
file_new = os.listdir(new_path)
for file in files:
    if file not in file_new:
        print(file)
        img = cv2.imread(path + file)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,img = cv2.threshold(img,32,255,cv2.THRESH_BINARY)

        cv2.imwrite('train/new/{}'.format(file), img)
        # cv2.imshow('title',img)
        #
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()