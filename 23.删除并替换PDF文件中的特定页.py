import arcpy
pdfDoc = arcpy.mp.PDFDocumentOpen(r"D:\Desktop\Google Play服务条款.pdf")
pdfDoc.deletePages("3, 5-7")
pdfDoc.insertPages(r"D:\Desktop\3.pdf", 3)
pdfDoc.insertPages(r"D:\Desktop\5-7.pdf", 5)
pdfDoc.saveAndClose()
del pdfDoc