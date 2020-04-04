# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject(r"D:\Documents\ArcGIS\Projects\MyProject\MyProject.aprx")
for m in aprx.listMaps():
    print("Map: " + m.name)
    for lyr in m.listLayers():
        print("  " + lyr.name)
