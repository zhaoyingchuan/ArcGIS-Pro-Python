# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject('CURRENT')
map = aprx.listMaps('地图')[0]
for tab in map.listTables():
    text = arcpy.Describe(tab).aliasName
    tab.name = text
aprx.save()
