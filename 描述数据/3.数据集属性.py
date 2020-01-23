# coding=gbk
import arcpy

# Create a Describe object from the shapefile
#
desc = arcpy.Describe("D:\\Desktop\\�ϲ��н�����Դ����\\����.gdb\\����_transportation")
# Print dataset properties
#
print(("Dataset Type: {0}".format(desc.datasetType)))
print(("Extent:\n  XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(
    desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax)))
print(("MExtent: {0}".format(desc.MExtent)))
print(("ZExtent: {0}".format(desc.ZExtent)))

print(("Spatial reference name: {0}:".format(desc.spatialReference.name)))
