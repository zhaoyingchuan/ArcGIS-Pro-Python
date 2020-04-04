import arcpy

feature_class = arcpy.GetParameterAsText(0) #arcpy.GetParameterAsText(0)为第一个输入的参数
fields = arcpy.ListFields(feature_class)
uniquelist = []
for field in fields:
    uniquelist.append(field.name)
print(uniquelist)
fid = arcpy.GetParameterAsText(1) #arcpy.GetParameterAsText(1)为第二个输入的参数
if fid in uniquelist:
    t = 'true'
else:
    t = 'False'
arcpy.SetParameterAsText(2, t) #arcpy.SetParameterAsText(2)为第一个输出的参数，输出t