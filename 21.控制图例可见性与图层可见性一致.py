import arcpy
aprx = arcpy.mp.ArcGISProject('CURRENT')

lyt = aprx.listLayouts("最大覆盖范围和最大人流量选址")[0]
legendlist = lyt.listElements("LEGEND_ELEMENT")
for legend in legendlist:
    legend.syncLayerVisibility == 'True'
aprx.save()
