#coding=gbk
import arcpy

# Create a Describe object from the feature class
#
desc = arcpy.Describe("D:\\Desktop\\南昌市健康资源分析\\江西.gdb\\江西_transportation\\车行线")

# Print some feature class properties
#
print("Feature Type:  " + desc.featureType)
print("Shape Type :   " + desc.shapeType)
print("Spatial Index: " + str(desc.hasSpatialIndex))