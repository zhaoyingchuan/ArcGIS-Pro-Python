# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject(r"D:\Desktop\南昌市健康资源分析\南昌市健康资源分析\南昌市健康资源分析.aprx")
map = aprx.listMaps('*1')
for m in map:
    lyr = m.listLayers()
    for l in lyr:
        l.updateConnectionProperties('固定时段服务区面', '固定时段服务区', '', 'False', '')
aprx.save()