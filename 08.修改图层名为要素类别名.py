# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject('CURRENT')
lyt = aprx.listLayouts('固定时段服务区')[0]
mflist = lyt.listElements("MAPFRAME_ELEMENT")
for mf in mflist:
    map = mf.map
    for lyr in map.listLayers():
        if lyr.isFeatureLayer:
            text = arcpy.Describe(lyr).aliasName
            lyr.name = text
aprx.save()

