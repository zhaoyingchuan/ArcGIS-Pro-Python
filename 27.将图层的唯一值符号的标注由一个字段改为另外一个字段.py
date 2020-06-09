import arcpy

p = arcpy.mp.ArcGISProject('CURRENT')
m = p.listMaps('地图')[0]
l = m.listLayers('DLTB')[0]
sym = l.symbology

cursor = arcpy.SearchCursor(l)
uniqueDict={}
uniqueDLBM = []
for row in cursor:
    key = row.getValue('DLBM')
    value=row.getValue('DLMC')
    if key not in uniqueDLBM:
        uniqueDLBM.append(key)
        uniqueDict[key] = value
print(uniqueDict)

for grp in sym.renderer.groups:
    for itm in grp.items:
        v=itm.label
        itm.label = uniqueDict[v]
        print(v+"---"+itm.label)

l.symbology = sym