# coding=gbk
import arcpy

# Create a Describe object
desc = arcpy.Describe("D:\\Desktop\\�ϲ��н�����Դ����\\����.gdb")

# Print some Describe Object properties
# hasattr�����ж϶����Ƿ���и������Ƶ�����
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