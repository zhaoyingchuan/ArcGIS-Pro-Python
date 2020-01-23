import arcpy

lyr = r'D:\Desktop\德安土规修改0924\德安土规修改.gdb\总规图斑2018_1'
cursor = arcpy.UpdateCursor(lyr)

for row in cursor:
    my_value = row.getValue("DLMC")
    if row.getValue("DLMC") == "坑塘水面":
        row.setValue("土地用途分区", "一般农地区")
        cursor.updateRow(row)
del cursor
