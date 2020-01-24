# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject(r"D:\Desktop\德安土规修改1113\德安土规修改.aprx")
lyt = aprx.listLayouts("3核减地块位置图（修改前后）")[0]

map1 = aprx.listMaps("4核减地块位置图（修改前）")[0]
lyr1 = map1.listLayers("调出地块1113")[0]
rows1 = arcpy.SearchCursor(lyr1,'','','','地块名')

map2 = aprx.listMaps("5核减地块位置图（修改后）")[0]
lyr2 = map2.listLayers("调出地块1113")[0]

for row1 in rows1:
    # i = ["13"]
    # if row1.getValue("Layer") in i:
        mf1 = lyt.listElements("MAPFRAME_ELEMENT", "地图框1")[0]
        lyr1.definitionQuery = "地块名 = " + "'" + row1.getValue("地块名") + "'"
        extent1 = mf1.getLayerExtent(lyr1, "False", "True")
        mf1.camera.setExtent(extent1)
        mf1.camera.scale = 10000

        mf2 = lyt.listElements("MAPFRAME_ELEMENT", "地图框2")[0]
        lyr2.definitionQuery = "地块名 = " + "'" + row1.getValue("地块名") + "'"
        extent2 = mf2.getLayerExtent(lyr2, "False", "True")
        mf2.camera.setExtent(extent2)
        mf2.camera.scale = 10000
        lyt.exportToJPEG(r"D:\\Desktop\\德安两规融合成果\\土规调出附图\\" + str(row1.getValue("地块名")), resolution=300)

del rows1
