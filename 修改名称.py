import os
path=r'TIF/'

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)

for i in range(len(fileList)):
    # name = fileList[i].replace('.JPEG','')
    # name  = name1.replace('.','') 
    # print(name)
    #name = fileList[i].replace('.txt','')
    #设置旧文件名（就是路径+文件名）
    oldname=path+ os.sep + fileList[i]   # os.sep添加系统分隔符
    #设置新文件名
    newname=path + os.sep + 'GuiY_' + str(i+1) +'.tif'
        
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)