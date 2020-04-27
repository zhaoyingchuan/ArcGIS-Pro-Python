import arcpy
import os
file_dir="D:\\Documents\\ArcGIS\\Projects"

for root, dirs, files in os.walk(file_dir):
    if ".gdb" in root:
        print(root)

        # arcpy.env.workspace = root
        # for fc in arcpy.ListFeatureClasses():#未指定feature_dataset则表示只列出独立要素类
        #     arcpy.Delete_management(fc)
        #     print("  已删除  "+fc)
        # for fc in arcpy.ListTables():
        #     arcpy.Delete_management(fc)
        #     print("  已删除  "+fc)



        arcpy.env.workspace = root
        datasets = arcpy.ListDatasets("基础数据", "Feature")
        for dataset in datasets:
            arcpy.Delete_management(dataset)
            print("  已删除  "+dataset)
