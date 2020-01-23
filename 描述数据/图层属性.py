# coding=gbk
import arcpy

# Create a Describe object from a .lyr file.
#
desc = arcpy.Describe("C:\Data\各类球类场所.lyrx")

# Print some properties of the feature layer
#
print("Name String:        " + desc.nameString)
print("Where Clause:       " + desc.whereClause)

# Find out if the layer represents a feature class
if desc.dataElement.dataType == "FeatureClass":
    print("Feature class:      " + desc.dataElement.catalogPath)
    print("Feature class Type: " + desc.featureClass.featureType)
else:
    print("Not a regular feature class")
