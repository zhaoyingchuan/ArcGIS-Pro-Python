#coding=utf-8
import arcpy
fc = r"D:\\Desktop\\南昌市健康资源分析\\设施点及原始数据.gdb\\公共康体保健\\各类球类场所"
field = "type_"
cursor = arcpy.SearchCursor(fc)
uniqueList = []
SQL = ''
for row in cursor:
    v = row.getValue(field)
    if v not in uniqueList:
        uniqueList.append(v)
        SQL = SQL + "type_ = '" + str(v) + "' OR "
print(SQL)