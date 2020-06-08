import os
import arcpy

#合并多个GDB数据库的结构且不包含要素
gdblist=[] #新建空白列表 #关于列表的概念请移步https://www.runoob.com/python3/python3-list.html
file_dir="D:\\Desktop" #输入待合并GDB数据库所在的文件夹的路径
dirlist=os.listdir(file_dir) #获取 D:\\Desktop 下一层级目录的路径
for dir in dirlist: #循环dirlist列表
    if ".gdb" in dir: #如果路径名称中包含 .gdb 字符串
        gdblist.append(file_dir+"\\"+dir) #将待合并GDB数据库的路径添加到gdblist列表中
print(gdblist)

outpath="D:\\Desktop" #合并后GDB数据库所在的文件夹
outgdbname="汇总数据库" #合并后GDB数据库的名称
if arcpy.Exists(outpath+"\\"+outgdbname+".gdb"): #判断是否已存在将新建的GDB数据库
    pass
else:
    arcpy.CreateFileGDB_management(outpath,outgdbname) #建立输出地理数据库

for gdb in gdblist: #循环待合并GDB数据库
    print(gdb) #打印循环到的某个数据库的路径
    arcpy.env.workspace = gdb #将循环到的数据库作为工作空间
    datasets = arcpy.ListDatasets() #列出该数据库包含的要素数据集
    for ds in datasets: #循环要素数据集
        if arcpy.Exists(outpath + "\\" + outgdbname + ".gdb"+"\\"+ds): #判断汇总数据库中是否已存在同名要素数据集
            pass
        else: #如果不存在改要素数据集
            desc = arcpy.Describe(ds) #获取该要素数据集的描述
            sr = desc.spatialReference #获取该要素数据集的空间参考
            arcpy.CreateFeatureDataset_management(outpath+"\\"+outgdbname+".gdb",ds,sr)  #在汇总数据库中创建同名的要素数据集，并且空间参考与待合并GDB数据集中的要素数据集保持一致
            print("    "+ds) #打印该要素数据集的名称

        fcs=arcpy.ListFeatureClasses(feature_dataset=ds)
        for fc in fcs:
            if arcpy.Exists(outpath + "\\" + outgdbname + ".gdb"+"\\"+ds + "\\" + fc):
                pass
            else:
                arcpy.FeatureClassToFeatureClass_conversion(fc,outpath + "\\" + outgdbname + ".gdb"+"\\"+ds,fc)
                print("        " + fc)
                arcpy.DeleteFeatures_management(outpath + "\\" + outgdbname + ".gdb"+"\\"+ds + "\\" + fc)
            # if arcpy.Exists(gdb+"\\"+ds+"\\"+fc):
            #     arcpy.Append_management(gdb+"\\"+ds+"\\"+fc,outpath + "\\" + outgdbname + ".gdb" + "\\" + ds + "\\" + fc, "NO_TEST")

#将待合并GDB数据库中的多个同名要素类追加到汇总数据库中同名的要素类中
print('开始合并GDB数据库中的同名要素类')
arcpy.env.workspace = outpath+"\\"+outgdbname+".gdb"
datasets = arcpy.ListDatasets()
for ds in datasets:
    print('    '+ds)
    fcs=arcpy.ListFeatureClasses(feature_dataset=ds)
    for fc in fcs:
        for gdb in gdblist:
            if arcpy.Exists(gdb+"\\"+ds+"\\"+fc):
                arcpy.Append_management(gdb+"\\"+ds+"\\"+fc, outpath + "\\" + outgdbname + ".gdb" + "\\" + ds + "\\" + fc,"NO_TEST")
                print('        '+fc+'  '+'合并成功')

