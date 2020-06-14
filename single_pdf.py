import os
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_writer = PdfFileWriter()


def single(left, right, lower, upper, pdf_name0):
    pdf_reader = PdfFileReader(f'{pdf_name0}', 'r')
    page = pdf_reader.getPage(0)

    left *= 72
    right *= 72
    lower *= 72
    upper *= 72

    for i in range(0, pdf_reader.getNumPages()):
        pdf_page1 = pdf_reader.getPage(i)
        orientation = pdf_page1.cropBox.getUpperRight()
        print(f"{i}-->{orientation}")

        pdf_page1.cropBox.setLowerLeft((0 + left), (0 + lower))
        pdf_page1.cropBox.setLowerRight((float(orientation[0]) - right), (0 + lower))
        pdf_page1.cropBox.setUpperLeft((0 + left), (float(orientation[1]) - upper))
        pdf_page1.cropBox.setUpperRight((float(orientation[0]) - right), (float(orientation[1]) - upper))
        pdf_writer.addPage(pdf_page1)

    outstream = open(f'00{pdf_name0}', 'wb')
    pdf_writer.write(outstream)
    outstream.close()
