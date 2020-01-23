# coding=gbk
import arcpy

# Create a Describe object
desc = arcpy.Describe("D:\\Desktop\\南昌市健康资源分析\\江西.gdb")

# Print some Describe Object properties
# hasattr用于判断对象是否具有给定名称的属性
if hasattr(desc, "name"):
    print("Name:        " + desc.name)
if hasattr(desc, "dataType"):
    print("DataType:    " + desc.dataType)
if hasattr(desc, "catalogPath"):
    print("CatalogPath: " + desc.catalogPath)

# Examine children and print their name and dataType
print("Children:")
for child in desc.children:
    print("\t%s = %s" % (child.name, child.dataType))