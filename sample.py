import arcpy, os, sys

relpath = os.path.dirname(sys.argv[0])

p = arcpy.mp.ArcGISProject(os.path.join(relpath, 'SingleSymbol.aprx'))
m = p.listMaps('Map')[0]
l = m.listLayers('Airports*')[0]
sym = l.symbology

if sym.renderer.type == 'SimpleRenderer':
    sym.renderer.label = 'Airports'
    sym.renderer.description = 'Nonprimary and Primary'
    sym.renderer.symbol.applySymbolFromGallery('Airport')
    sym.renderer.symbol.size = 12

    l.symbology = sym

p.saveACopy(os.path.join(relpath, 'SavedOutput.aprx'))