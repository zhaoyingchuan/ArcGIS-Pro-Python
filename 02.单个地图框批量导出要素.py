# coding=utf-8
import arcpy

aprx = arcpy.mp.ArcGISProject(r"D:\Desktop\德安土规修改1111\德安土规修改.aprx")
lyt = aprx.listLayouts("1项目图")[0]
map = aprx.listMaps("1项目图")[0]
lyr = map.listLayers("项目线1112")[0]
rows = arcpy.SearchCursor(lyr,'','','','序号')
for row in rows:
    # i = ['29','37']
    # if row.getValue("Layer") in i:
        lyr.definitionQuery = "Layer = " + "'" + row.getValue("Layer") + "'"
        mf = lyt.listElements("MAPFRAME_ELEMENT", "地图框")[0]
        extent = mf.getLayerExtent(lyr, "False", "True")
        mf.camera.setExtent(extent)
        mf.camera.scale = mf.camera.scale*1.2
        lyt.exportToJPEG(r"D:\\Desktop\\德安两规融合成果\\项目图\\城规图\\" + row.getValue("Layer") + row.getValue("项目名称"), resolution = 300)
        lyr.definitionQuery = ""
del rows
del aprx