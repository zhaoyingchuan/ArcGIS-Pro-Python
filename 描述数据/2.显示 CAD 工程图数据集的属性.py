# coding=gbk
import arcpy

# Create a describe object
#
desc = arcpy.Describe(r"D:\Desktop\�����������ν���Ŀ\�ǹ�ɹ��������гǹ�Ժ�ṩ���ϣ�\�ǹ�CADͼ��\6���ĳ�������������״ͼ80.dwg")

# Print Cad Drawing Dataset properties
#
print("%-12s %s" % ("is2D:", desc.is2D))
print("%-12s %s" % ("is3D:", desc.is3D))
print("%-12s %s" % ("isAutoCAD:", desc.isAutoCAD))
print("%-12s %s" % ("isDGN:", desc.isDGN))
