import arcpy

# "序号"是你编号需要依据的字段。注意数据类型
rows = arcpy.UpdateCursor(r"D:\\Desktop\\进贤县\\Default.gdb\\面", "", "", "", "OBJECTID")
i = 1
for row in rows:
    # BH是你想要自动连续编号的字段。注意数据类型
    row.setValue("序号", i)
    rows.updateRow(row)
    i=i+1
