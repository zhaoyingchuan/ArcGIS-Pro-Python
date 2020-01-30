# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject(r"D:\Desktop\德安土规修改1224\德安土规修改.aprx")
lyt = aprx.listLayouts("2新增建设用地位置图（修改前后）")[0]

map1 = aprx.listMaps("2新增建设用地位置图（修改前）")[0]
lyr1 = map1.listLayers("不符合土规项目1215")[0]
lyr2 = map1.listLayers("调入地块1220")[0]
rows1 = arcpy.SearchCursor(lyr1, '', '', '', '序号')

map2 = aprx.listMaps("3新增建设用地位置图（修改后）")[0]
lyr3 = map2.listLayers("不符合土规项目1215")[0]
lyr4 = map2.listLayers("调入地块1220")[0]

for row1 in rows1:
    mf1 = lyt.listElements("MAPFRAME_ELEMENT", "地图框1")[0]
    lyr1.definitionQuery = "项目名称 = " + "'" + row1.getValue("项目名称") + "'"
    lyr2.definitionQuery = "项目名称 = " + "'" + row1.getValue("项目名称") + "'"
    extent1 = mf1.getLayerExtent(lyr1, "False", "True")
    mf1.camera.setExtent(extent1)
    if row1.getValue("Layer") in ['18', '39', '44', '46-2', '46-3', '46-4', '52']:
        mf1.camera.scale = 1000
    elif row1.getValue("Layer") in ['29', '37']:
        mf1.camera.scale = 35000
    else:
        mf1.camera.scale = 10000

    mf2 = lyt.listElements("MAPFRAME_ELEMENT", "地图框2")[0]
    lyr3.definitionQuery = "项目名称 = " + "'" + row1.getValue("项目名称") + "'"
    lyr4.definitionQuery = "项目名称 = " + "'" + row1.getValue("项目名称") + "'"
    extent2 = mf2.getLayerExtent(lyr3, "False", "True")
    mf2.camera.setExtent(extent2)
    mf2.camera.scale = mf1.camera.scale

    lyt.exportToJPEG(r"D:\\Desktop\\德安两规融合成果\\土规调入附图\\" + str(row1.getValue("Layer")) + row1.getValue("项目名称"),
                     resolution=300)

del rows1
