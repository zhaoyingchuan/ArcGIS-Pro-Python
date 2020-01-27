import arcpy

feature_class = r"D:\\Desktop\\南昌市健康资源分析\\固定时段服务区.gdb\\公共康体保健\\各类球类场所步行15分钟"
fields = arcpy.ListFields(feature_class)
uniqueList = []
for field in fields:
    if field.name not in uniqueList:
        uniqueList.append(field.name)
print(uniqueList)
if "总人" in uniqueList:
    print("True")
else:
    print("False")
    print(feature_class)