import arcpy

feature_class = arcpy.GetParameterAsText(0)

# Create a list of fields using the ListFields function
fields = arcpy.ListFields(feature_class)

for field in fields:
    if field.name==arcpy.GetParameterAsText(1) :
        newFieldName=arcpy.GetParameterAsText(2)
        arcpy.AddField_management(feature_class, newFieldName, field.type, field.precision, field.scale, field.length, newFieldName)
        arcpy.CalculateField_management(feature_class, newFieldName, "!"+field.name+"!", "PYTHON3")
        arcpy.DeleteField_management(feature_class, field.name)