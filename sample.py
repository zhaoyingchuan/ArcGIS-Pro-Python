# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject('D:\Documents\ArcGIS\Projects\万年县两规融合数据审查\万年县两规融合数据审查.aprx')
map = aprx.listMaps('地图')[0]
for lyr in map.listLayers():
    if lyr.isFeatureLayer:
        print(arcpy.Describe(lyr).aliasName)
