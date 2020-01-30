import os
import arcpy
# Get the input and output workspaces
#
arcpy.env.workspace = r"D:\\Documents\\ArcGIS\\Projects\\安远县两规融合数据审查\\安远县两规融合数据审查.gdb\\土规"

# Get a list of input feature classes to be copied and copy
#  to new output location
#
for fc in arcpy.ListFeatureClasses():
    out_fc = arcpy.ValidateTableName(fc)
    print(out_fc)