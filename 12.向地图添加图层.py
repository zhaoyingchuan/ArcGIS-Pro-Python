# coding=utf-8
import arcpy
aprx = arcpy.mp.ArcGISProject('CURRENT')
maplist = aprx.listMaps()
insertLyr = aprx.listMaps('康复与预防机构')[0].listLayers('水域单元')[0]
for map in maplist:
    refLyr = map.listLayers(map.name)[0]
    map.insertLayer(refLyr, insertLyr, "BEFORE")
aprx.save()