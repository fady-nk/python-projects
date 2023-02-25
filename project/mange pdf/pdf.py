import PyPDF2

new_pdf = open('/media/fady/MiNa/fnct/IT pdf/chap5.pdf', 'rb') #file object creation

reading_pdf = PyPDF2.PdfFileReader(new_pdf) #reading the file
print(reading_pdf.numPages) #number of pages in the file

"""this is for extracting all the pages
num=reading_pdf.numPages
for i in range(num):
    pdf_page = reading_pdf.getPage(i) #getting the first page
    print(pdf_page.extractText()) #extracting the text from the page
"""

pdf_page = reading_pdf.getPage(0) #getting the first page
print(pdf_page.extractText()) #extracting the text from the page

new_pdf.close() #closing the file