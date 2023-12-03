import io, sys
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

IN_FILEPATH = open("mypdf.pdf","rb") 
OUT_FILEPATH = 'output.pdf'

def new_content(cnt):
    row = 1
    col = 0
    offsetX = 1
    offsetY = 2
    size = 4.75

    pdf = FPDF()
    pdf.add_page() # first page
    pdf.set_font('Arial', '', 14)
    pdf.text(37 , 287 , str(cnt))

    pdf.add_page() # second page
    pdf.text(80 , 137 , str(cnt))
    for i in range(3):
        
        # Then put a blue underlined link
        
        pdf.text(117 + (i*(size+offsetX)) , 195 , str(cnt//10**(2 - i)))
        pdf.ellipse(116 + (i*(size+offsetX)), 197 + ((cnt//10**(2 - i))*(size + offsetY)), size, size, 'FD')
        cnt %= 10**(2 - i)
    
    pdf_content = pdf.output('temp1.pdf')

def buildPage(cnt):
    reader = PdfReader(IN_FILEPATH)
    new_content(cnt)
    print(cnt)

    for i in range(2):
        page_overlay = PdfReader('temp1.pdf').pages[i]
        reader.pages[i].merge_page(page_overlay)

    writer =  PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.write('temp2.pdf')

writerf =  PdfWriter()
for ID in range(1,551):
    buildPage(ID)
    writerf.append('temp2.pdf')
    
writerf.write(OUT_FILEPATH)
