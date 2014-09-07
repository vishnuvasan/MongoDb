
def To_PDF(pdfname="Auto_Generated_",imagename="a.jpg",x=0,y=0):
	from reportlab.pdfgen import canvas
	from reportlab.lib.unit import inch,cm
	global sheet
	sheet=canvas.Canvas(pdfname+".pdf")
	sheet.drawString(-1,-1,"Hello")
	sheet.showPage()
	sheet.drawImage(imagename,x,y)
	sheet.showPage()
	sheet.save()


def Merge_PDF(filename):
	import os
	from pyPdf import PdfFileWriter,PdfFileReader
	output = PdfFileWriter()
	files=find_pdf_files
	input = PdfFileReader(open(filename,"rb"))
	for page in range(0,input.getNumPages()):
         	output.addPage(input.getPage(page))
	
	out=open(outputFile,"wb")
	output.write(out)
	out.close()

def find_pdf_files(basepath):
	"Find all the PDF Files in the folder"
