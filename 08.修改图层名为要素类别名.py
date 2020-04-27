# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject('CURRENT')
map = aprx.listMaps('地图')[0]
for lyr in map.listLayers():
    # if lyr.isFeatureLayer:
        text = arcpy.Describe(lyr).aliasName
        lyr.name = text
aprx.save()

