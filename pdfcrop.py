from PyPDF2 import PdfFileReader, PdfFileWriter, PageRange
import glob
import single_pdf
import all_pdf

while True:
    inp = input("""PDF CROPPER PLEASE PUT THOSE PDF'S AND THIS PYPROGRAMME IN SAME FOLDER
TYPE 1 IF YOU WANT TO CROP JUST ONE PDF.
TYPE 2 IF YOU WANT TO CROP ALL THE PDF'S IN THE FOLDER.
TYPE STOP TO STOP THE PROGRAM
>>>""")
    pdf_name = glob.glob("*.pdf")
    pdf_num = len(pdf_name)
    pdf_writer = PdfFileWriter()

    if inp == '1':
        pdf_name0 = input("PDF NAME: ")
        lower = float(input("ENTER INCHES YOU WANT TO CUT FROM LOWER SIDE: "))
        right = float(input("ENTER INCHES YOU WANT TO CUT FROM RIGHT SIDE: "))
        upper = float(input("ENTER INCHES YOU WANT TO CUT FROM UPPER SIDE: "))
        left = float(input("ENTER INCHES YOU WANT TO CUT FROM LEFT SIDE: "))

        single_pdf.single(left, right, lower, upper, pdf_name0)

    elif inp == '2':
        lower = float(input("ENTER INCHES YOU WANT TO CUT FROM LOWER SIDE: "))
        right = float(input("ENTER INCHES YOU WANT TO CUT FROM RIGHT SIDE: "))
        upper = float(input("ENTER INCHES YOU WANT TO CUT FROM UPPER SIDE: "))
        left = float(input("ENTER INCHES YOU WANT TO CUT FROM LEFT SIDE: "))

        all_pdf.all(left, right, lower, upper)

    elif (inp.upper() == 'QUIT') or (inp == '1'):
        break

    else:
        print("ENTER VALID VALUE")