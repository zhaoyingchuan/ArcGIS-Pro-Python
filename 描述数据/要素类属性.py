#coding=gbk
import arcpy

# Create a Describe object from the feature class
#
desc = arcpy.Describe("D:\\Desktop\\�ϲ��н�����Դ����\\����.gdb\\����_transportation\\������")

# Print some feature class properties
#
print("Feature Type:  " + desc.featureType)
print("Shape Type :   " + desc.shapeType)
print("Spatial Index: " + str(desc.hasSpatialIndex))