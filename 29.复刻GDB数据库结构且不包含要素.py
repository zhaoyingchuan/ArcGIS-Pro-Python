import os
import arcpy



outpath="D:\\Desktop"
outgdbname="汇总数据库"

if arcpy.Exists(outpath+"\\"+outgdbname+".gdb"):
    pass
else:
    arcpy.CreateFileGDB_management(outpath,outgdbname) #建立输出地理数据库

arcpy.env.workspace = "D:\\Desktop\\吉安市吉安县_生态保护红线基础数据要素图层.gdb"
datasets = arcpy.ListDatasets()
for ds in datasets:
    desc = arcpy.Describe(ds)
    sr = desc.spatialReference
    if arcpy.Exists(outpath + "\\" + outgdbname + ".gdb"+"\\"+ds):
        pass
    else:
        arcpy.CreateFeatureDataset_management(outpath+"\\"+outgdbname+".gdb",ds,sr)  # 建立输出地理数据库

    fcs=arcpy.ListFeatureClasses(feature_dataset=ds)
    for fc in fcs:
        print(fc)
        st = arcpy.Describe(fc).shapeType
        arcpy.CreateFeatureclass_management(outpath + "\\" + outgdbname + ".gdb"+"\\"+ds,fc,st)



# for workspace in workspaces:
#     arcpy.env.workspace = workspace
#     datasets = arcpy.ListDatasets()
#     for ds in datasets:
#         for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
#             path = os.path.join(arcpy.env.workspace, ds, fc)
#             print(path)

# import arcpy,os,string,sys
# from arcpy import env
# inpath=r"C：Users\Administrator\Desktop\mdb" #输入路径
# outpath=r"C：Users\Administrator\Desktop\mdb2" #输出路径
# outgdbname="cx"+".gdb" #输出数据库名称
# dbtype="mdb" #数据库类型
# fc="HYDA" #待合并图层
# fc_shapetype="POLYGON"#待合并图层形状：POLYGON,POLYLINE,POINT
# log=os.path.join(outpath,"%s's shapetype is not correct.TXT"%(fc)) #日志文件
# arcpy.CreateFileGDB_management(outpath,outgdbname) #建立输出地理数据库
# for root,dirs,files in os.walk(inpath): #解析输入文件夹下的文件的路径
#     str1 = ""  # 初始化字符串
#     for afile in files:  # 遍历文件
#         if afile[-3:].lower() == dbtype:  # 指定脚本处理的文件类型
#             mdb = os.path.join(root, afile)  # 获取待处理mdb 的绝对路径
#         env.workspace = mdb  # 指定工作空间
#         fcs = arcpy.ListFeatureClasses()  # 获取地理数据库下的图层列表
#         if fc in fcs or fc.lower() in fcs:  # 判断指定图层是否存在
#             fc_path = os.path.join(mdb, fc)  # 获取待处理图层的绝对路径
#             desc = arcpy.Describe(fc_path)  # 获取指定图层属性信息
#             if desc.shapetype.lower() == fc_shapetype.lower():  # 判断指定图层几何类型是否正确
#                 if arcpy.Exists(outpath+os.sep+outgdbname+os.sep+fc):
#                     pass  # 若输出数据库中已存在指定图层则pass
#             else:
#                 arcpy.CreateFeatureclass_management(outpath + os.sep + outgdbname, fc, fc_shapetype.upper(), fc_path)
#             # 若输出数据库中不存在指定图层则创建图层
#             arcpy.Append_management(fc_path, outpath + os.sep + outgdbname + os.sep + fc, "NO_TEST")  # 将输入路径下
#             的指定图层追加至输出数据库下的同名图层
#             if desc.shapetype.lower() != fc_shapetype.lower():
#                 str1 = str1 + '"' + afile + '"' + ","  # 记录几何类型不正确的指定图层
#             str = str1[:-1]
#             opfile = open(log, "a")  # 新建并打开日志文件
#             opfile.writelines(str)  # 将几何类型不正确的指定图层所在mdb 写入日志
#             opfile.close()  # 关闭文本