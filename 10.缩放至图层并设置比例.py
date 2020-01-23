# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject(r"D:\Desktop\南昌市健康资源分析\南昌市健康资源分析\南昌市健康资源分析.aprx")
lyt = aprx.listLayouts("固定时段服务区")[0]
mflist = lyt.listElements("MAPFRAME_ELEMENT")
for mf in mflist:
    map = aprx.listMaps(mf.name)[0]
    lyr = map.listLayers("中心城区")[0]
    extent = mf.getLayerExtent(lyr, "False", "True")
    mf.camera.setExtent(extent)
    mf.camera.scale = 200000
aprx.save()
