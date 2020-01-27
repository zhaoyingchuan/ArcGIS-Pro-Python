import arcpy
feature_class = r'D:\Desktop\南昌市健康资源分析\固定时段服务区.gdb\公共康体保健\各类球类场所步行15分钟'
fields = arcpy.ListFields(feature_class)
for field in fields:
    print(field.name)



