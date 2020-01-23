import arcpy
aprx = arcpy.mp.ArcGISProject('CURRENT')
lyt = aprx.listLayouts("固定时段服务区")[0]
elmlist = lyt.listElements("MAPFRAME_ELEMENT")
for elm in elmlist:
    print(elm.name)
    elm.elementPositionX = elm.elementPositionX + 1
    elm.elementPositionY = elm.elementPositionY + 1
    print(elm.elementPositionX)
    print(elm.elementPositionY)
aprx.save()
del aprx

