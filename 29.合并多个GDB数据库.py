import os #加载os库
import arcpy #加载arcpy库

gdblist=[] #新建空白列表 #关于列表的概念请移步 https://www.runoob.com/python3/python3-list.html
file_dir="D:\\Desktop" #输入待合并GDB数据库所在的文件夹的路径
dirlist=os.listdir(file_dir) #获取 D:\\Desktop 下一层级目录的路径
for dir in dirlist: #循环dirlist列表
    if ".gdb" in dir: #如果路径名称中包含 .gdb 字符串
        gdblist.append(file_dir+"\\"+dir) #将待合并GDB数据库的路径添加到gdblist列表中
print(gdblist)

outpath="D:\\Desktop" #合并后汇总数据库所在的文件夹
outgdbname="汇总数据库" #合并后汇总数据库的名称
allgdb=outpath+"\\"+outgdbname+".gdb" #汇总数据库的完整路径
if arcpy.Exists(allgdb): #判断是否已存在将新建的汇总数据库
    pass
else:
    arcpy.CreateFileGDB_management(outpath,outgdbname) #建立汇总数据库

for gdb in gdblist: #循环待合并GDB数据库
    print(gdb) #打印循环到的某个数据库的路径
    arcpy.env.workspace = gdb #将循环到的数据库作为工作空间
    datasets = arcpy.ListDatasets() #列出该数据库包含的要素数据集
    for ds in datasets: #循环要素数据集
        print("    " + ds)  # 打印该要素数据集的名称
        if arcpy.Exists(allgdb+"\\"+ds): #判断汇总数据库中是否已存在同名要素数据集
            pass
        else: #如果不存在改要素数据集
            desc = arcpy.Describe(ds) #获取该要素数据集的描述
            sr = desc.spatialReference #获取该要素数据集的空间参考
            arcpy.CreateFeatureDataset_management(allgdb,ds,sr)  #在汇总数据库中创建同名的要素数据集，并且空间参考与待合并GDB数据集中的要素数据集保持一致


        fcs=arcpy.ListFeatureClasses(feature_dataset=ds) #获取该要素数据集下的所有要素类
        for fc in fcs: #循环该要素数据集下的所有要素类
            print("        " + fc)  # 打印要素类名称便于查看进度
            if arcpy.Exists(allgdb+"\\"+ds + "\\" + fc): #如果汇总数据库下已存在该名称的要素类
                arcpy.Append_management(gdb + "\\" + ds + "\\" + fc,
                                        allgdb + "\\" + ds + "\\" + fc,
                                        "NO_TEST") #将该要素类追加到汇总数据库下同名的要素类中
            else: #如果汇总数据库下不存在该名称的要素类
                arcpy.FeatureClassToFeatureClass_conversion(fc,allgdb+"\\"+ds,fc) #复制该要素类至汇总数据库下的要素数据集中