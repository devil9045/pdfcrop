import glob
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_writer = PdfFileWriter()


def all(left, right, lower, upper):
    pdf_name = glob.glob("*.pdf")
    num_pdf = len(pdf_name)
    left *= 72
    right *= 72
    lower *= 72
    upper *= 72

    for num in range(num_pdf):
        pdf_reader = PdfFileReader(f'{pdf_name[num]}', 'r')
        
        left *= 72
        right *= 72
        lower *= 72
        upper *= 72

        for i in range(0, pdf_reader.getNumPages()):
            page2 = pdf_reader.getPage(i)
            orientation = page2.cropBox.getUpperRight()
            print(f"{i}-->{orientation}")

            page2.cropBox.setLowerLeft((0 + left), (0 + lower))
            page2.cropBox.setLowerRight((float(orientation[0]) - right), (0 + lower))
            page2.cropBox.setUpperLeft((0 + left), (float(orientation[1]) - upper))
            page2.cropBox.getUpperRight((float(orientation[0]) - right), (float(orientation[1]) - upper))
            pdf_writer.addPage(page2)

        outstream = open(f'00{pdf_name}', 'wb')
        pdf_writer.write(outstream)
        outstream.close()


