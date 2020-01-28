import arcpy
feature_class =  arcpy.GetParameterAsText(0)
fields = arcpy.ListFields(feature_class)
uniquelist = []
for field in fields:
    uniquelist.append(field.name)
print(uniquelist)
fid = arcpy.GetParameterAsText(1)
if fid in uniquelist:
    t = 'true'
else:
    t = 'False'
arcpy.SetParameterAsText(2, t)
