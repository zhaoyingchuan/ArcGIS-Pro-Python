import os
import arcpy

gdblist=[]
file_dir="D:\\Desktop"
dirlist=os.listdir(file_dir) #获取 D:\\Desktop 下一层级目录的路径
for dir in dirlist:
    if ".gdb" in dir:
        gdblist.append(file_dir+"\\"+dir)
print(gdblist)

outpath="D:\\Desktop"
outgdbname="汇总数据库"
if arcpy.Exists(outpath+"\\"+outgdbname+".gdb"):
    pass
else:
    arcpy.CreateFileGDB_management(outpath,outgdbname) #建立输出地理数据库

for gdb in gdblist:
    print(gdb)
    arcpy.env.workspace = gdb
    datasets = arcpy.ListDatasets()
    for ds in datasets:
        if arcpy.Exists(outpath + "\\" + outgdbname + ".gdb"+"\\"+ds):
            pass
        else:
            desc = arcpy.Describe(ds)
            sr = desc.spatialReference
            arcpy.CreateFeatureDataset_management(outpath+"\\"+outgdbname+".gdb",ds,sr)  # 建立输出地理数据库
            print("    "+ds)

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

