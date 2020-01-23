# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject(r"D:\Desktop\南昌市健康资源分析\南昌市健康资源分析\南昌市健康资源分析.aprx")
for m in aprx.listMaps():
    print("Map: " + m.name)
    for lyr in m.listLayers():
        print("  " + lyr.name)
