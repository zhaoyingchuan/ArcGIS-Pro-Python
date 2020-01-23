# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject("CURRENT")
lyt = aprx.listLayouts("最大覆盖范围和最大人流量选址")[0]
mflist = lyt.listElements("MAPFRAME_ELEMENT")
mapsource = aprx.listMaps("各类球类场所1")[0]
lyrsource = mapsource.listLayers("15分钟已覆盖范围")[0]

for mf in mflist:
    map = mf.map
    lyr = map.listLayers('*已覆盖范围')[0]
    lyr.visible = True
    lyr.symbology = lyrsource.symbology
aprx.save()