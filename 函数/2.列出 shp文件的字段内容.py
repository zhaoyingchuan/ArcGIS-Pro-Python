# coding=gbk
import arcpy

# Open a searchcursor
#  Input: C:/Data/Counties.shp
#  Fields: NAME; STATE_NAME; POP2000
#  Sort fields: STATE_NAME A; POP2000 D
rows = arcpy.SearchCursor("C:\\Data\\火车线.shp",
                          fields="FID; name; type",
                          sort_fields="type")
# Iterate through the rows in the cursor and print out the
# state name, county and population of each.
for row in rows:
    print("FID: {0}, name: {1}, type: {2}".format(
        row.getValue("FID"),
        row.getValue("name"),
        row.getValue("type")))
