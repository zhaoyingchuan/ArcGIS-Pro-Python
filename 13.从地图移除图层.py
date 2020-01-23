# coding=utf-8
import arcpy
aprx = arcpy.mp.ArcGISProject('CURRENT')
maplist = aprx.listMaps()
for map in maplist:
    for lyr in map.listLayers():
        if lyr.name == '水域单元':
            removelayer = map.listLayers('水域单元')[0]
            map.removeLayer(removelayer)
aprx.save()