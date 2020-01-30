import arcpy

# Create a Describe object from the GDB table.
#
desc = arcpy.Describe(r"D:\\Documents\\ArcGIS\\Projects\\安远县两规融合数据审查\\安远县两规融合数据审查.gdb\\土规\\安远县土规调出地块（逻辑）")

# Print GDB Table properties
#
print("%-22s %s" % ("AliasName:", desc.aliasName))
print("%-22s %s" % ("DefaultSubtypeCode:", desc.defaultSubtypeCode))
print("%-22s %s" % ("GlobalIDFieldName:", desc.globalIDFieldName))
print("%-22s %s" % ("ModelName:", desc.modelName))
print("%-22s %s" % ("RasterFieldName:", desc.rasterFieldName))
print("%-22s %s" % ("RelationshipClassNames:", desc.relationshipClassNames))
