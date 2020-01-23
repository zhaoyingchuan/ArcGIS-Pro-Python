# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject('CURRENT')
lyt = aprx.listLayouts('最大覆盖范围和最大人流量选址')[0]
mflist = lyt.listElements("MAPFRAME_ELEMENT")
for mf in mflist:
    if mf.name == '各类球类场所 地图框':
        mf.visible = false
