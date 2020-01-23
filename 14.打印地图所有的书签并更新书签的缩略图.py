# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject(r"D:\Desktop\南昌市健康资源分析\南昌市健康资源分析\南昌市健康资源分析.aprx")
map = aprx.listMaps("度假休闲场所")[0]

bkmks = map.listBookmarks()
for bkmk in bkmks:
    print(bkmk.name)
    if bkmk.hasThumbnail == False:
        bkmk.updateThumbnail()
aprx.save()