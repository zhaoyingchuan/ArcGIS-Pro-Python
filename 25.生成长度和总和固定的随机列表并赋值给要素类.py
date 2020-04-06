import random
import bs4
total = 2000
n = 400
x = [random.random() for i in range(n)]
e = [int(i / sum(x) * (total - n)) + 1 for i in x] #每人留一分,剩余随机分，用四舍五入可能会超过总数
re = total - sum(e)
u = [random.randint(0, n - 1) for i in range(re)] #截断取整剩的零头再随机给各人 1 分
for i in range(re):
    e[u[i]] += 1

print(e)
print(sum(e))

import time
import arcpy
aprx = arcpy.mp.ArcGISProject("CURRENT")
map=aprx.listMaps("地图")[0]
# Create update cursor for feature class
rows = arcpy.UpdateCursor("D:\\Documents\\ArcGIS\\Projects\\MyProject\\MyProject.gdb\\南昌市渔网_label")
# Update the field used in buffer so the distance is based on the
# road type. Road type is either 1, 2, 3, or 4. Distance is in meters.
i=0
for row in rows:
    # Fields from the table can be dynamically accessed from the
    # row object. Here fields named BUFFER_DISTANCE and ROAD_TYPE
    # are used
    row.setValue("value", e[i])
    rows.updateRow(row)
    i=i+1
# Delete cursor and row objects to remove locks on the data.
del row
del rows