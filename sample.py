#coding=utf-8
import arcpy
# 设置输入要素
inputFeatures = arcpy.GetParameterAsText(0)
# 设置裁剪要素
clipFeatures = arcpy.GetParameterAsText(1)
# 设置输出要素
outFeatures = arcpy.GetParameterAsText(2)
# Use scratchGDB environment to write intermediate data
tempData = arcpy.CreateScratchName(workspace=arcpy.env.scratchGDB)
try:
      clipOutFeatureClass = arcpy.Clip_analysis(inputFeatures, clipFeatures, tempData, 1.5)
      arcpy.Buffer_analysis(clipOutFeatureClass, outFeatures, "10 Kilometers", "FULL", "ROUND", "NONE")
except Exception as err:
    arcpy.AddError(err)
    print(err)