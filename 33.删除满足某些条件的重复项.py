import arcpy

p = arcpy.mp.ArcGISProject('CURRENT')
m = p.listMaps('地图')[0]
l = m.listLayers('JMD')[0]

cursor = arcpy.SearchCursor(l)
uniqueArea = []

for row in cursor:
    value = row.getValue('Shape_Area')
    if value not in uniqueArea:
        uniqueArea.append(value)

for value in uniqueArea:
    cursor = arcpy.UpdateCursor(l, where_clause="Shape_Area = " + str(value), spatial_reference=None, fields=None,
                                sort_fields="Layer D")
    i = 0
    for row in cursor:
        if i > 0:
            cursor.deleteRow(row)
        i=i+1

