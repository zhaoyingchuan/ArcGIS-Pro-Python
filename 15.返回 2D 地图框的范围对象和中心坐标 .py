# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject(r"D:\Desktop\南昌市健康资源分析\南昌市健康资源分析\南昌市健康资源分析.aprx")
lyt = aprx.listLayouts("固定时段服务区")[0]
mflist = lyt.listElements("MAPFRAME_ELEMENT")
for mf in mflist:
    print(mf.name + '\n' +str(mf.camera.X) + '  ' + str(mf.camera.Y))
    print(mf.camera.getExtent())

