import arcpy

cursor = arcpy.SearchCursor(fc)
i=0
for row in cursor:
    if i>o:
        cursor.deleteRow(row)