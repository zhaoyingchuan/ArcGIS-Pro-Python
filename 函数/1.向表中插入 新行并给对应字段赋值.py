# coding=gbk
import arcpy

# Create insert cursor for table
rows = arcpy.InsertCursor("c:/base/data.gdb/roads_lut")
# Create 25 new rows. Set the initial row ID and distance values
for x in range(1, 26):
    row = rows.newRow()
    row.setValue("rowid", x)
    row.setValue("distance", 100)
    rows.insertRow(row)
# Delete cursor and row objects to remove locks on the data
del row
del rows
