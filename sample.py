# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject('CURRENT')
map = aprx.listMaps('地图')[0]
addTab = arcpy.mp.Table(r"C:\Projects\YosemiteNP\Data_Vector\YosemiteData.gdb\NHDFCode")
for tab in map.listTables():
    map.addTable (tab)
aprx.save()
