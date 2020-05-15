import arcpy

p = arcpy.mp.ArcGISProject('CURRENT')
m = p.listMaps('地图')[0]
l = m.listLayers('DLTB')[0]
sym = l.symbology

cursor = arcpy.SearchCursor(l,'','','',sort_fields='DLBM')
uniqueList = []
for row in cursor:
    v = row.getValue('DLMC')
    if v not in uniqueList:
        uniqueList.append(v)

for grp in sym.renderer.groups:
    i=0
    for itm in grp.items:
        itm.label = uniqueList[i]
        i=i+1
l.symbology = sym