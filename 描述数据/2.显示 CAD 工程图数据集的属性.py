# coding=gbk
import arcpy

# Create a describe object
#
desc = arcpy.Describe(r"D:\Desktop\樟树市两规衔接项目\城规成果（樟树市城规院提供资料）\城规CAD图件\6中心城区土地利用现状图80.dwg")

# Print Cad Drawing Dataset properties
#
print("%-12s %s" % ("is2D:", desc.is2D))
print("%-12s %s" % ("is3D:", desc.is3D))
print("%-12s %s" % ("isAutoCAD:", desc.isAutoCAD))
print("%-12s %s" % ("isDGN:", desc.isDGN))
