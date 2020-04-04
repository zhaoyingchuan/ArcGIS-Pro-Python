# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject('CURRENT')
map = aprx.listMaps()
for m in map:
    lyr = m.listLayers()
    for l in lyr:
        if l.name == '公交线':
            l.visible = False
aprx.save()
