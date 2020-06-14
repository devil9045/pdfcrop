import glob
from PyPDF2 import PdfFileReader

pdf_name = glob.glob("*.pdf")
pdf_num = len(pdf_name)

for num in range(pdf_num):
    reader = PdfFileReader(f'{pdf_name[num]}', 'r')
    print(pdf_name[num])
    for i in range(0, reader.getNumPages()):
        page = reader.getPage(i)
        orientation = page.cropBox.getUpperRight()
        print(f"{i+1}-->{orientation}")
    print("")
