import arcpy
aprx = arcpy.mp.ArcGISProject('CURRENT')
m = aprx.listMaps("康复与预防机构")[0]

for lyr in m.listLayers():
    if lyr.supports("SHOWLABELS"):
        if lyr.showLabels:
            print("Layer name: " + lyr.name)
            for lblClass in lyr.listLabelClasses():
                print("\t Class Name: \t" + lblClass.name)
                print("\t Expression: \t" + lblClass.expression)
                print("\t SQL Query:  \t" + lblClass.SQLQuery)
del aprx
