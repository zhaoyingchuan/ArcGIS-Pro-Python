import arcpy, os, sys

p = arcpy.mp.ArcGISProject("CURRENT")
m = p.listMaps('地图')[0]
l = m.listLayers('生态保护红线优化成果202101')[0]
sym = l.symbology

sym.updateRenderer('UniqueValueRenderer')
sym.renderer.fields = ['名称']
for grp in sym.renderer.groups:
    for itm in grp.items:
        transVal = itm.values[0][0] #Grab the first "percent" value in the list of potential values
        itm.symbol.color = {'RGB': [255, 0, 0, int(transVal)]}
        itm.label = str(transVal) + '%'

l.symbology = sym 