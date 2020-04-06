#coding=utf-8
import arcpy

# Create insert cursor for table
rows = arcpy.InsertCursor("D:\\Documents\\ArcGIS\\Default.gdb\\南昌市渔网_label")
# Create 25 new rows. Set the initial row ID and distance values
for x in range(1, 10):
    row = rows.newRow()
    row.setValue("OID", 500)
    row.setValue("value", 100)
    rows.insertRow(row)
# Delete cursor and row objects to remove locks on the data
del row
del rows

