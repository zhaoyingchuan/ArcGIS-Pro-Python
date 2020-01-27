import arcpy
aprx = arcpy.mp.ArcGISProject(r"D:\Desktop\南昌市健康资源分析\南昌市健康资源分析\南昌市健康资源分析.aprx")
lyt = aprx.listLayouts("固定时段服务区")[0]
elmlist = lyt.listElements("MAPFRAME_ELEMENT")
for elm in elmlist:
    print(elm.name)
    elm.elementPositionX = elm.elementPositionX + 10
    elm.elementPositionY = elm.elementPositionY + 10
    print(elm.elementPositionX)
    print(elm.elementPositionY)
aprx.save()
del aprx

