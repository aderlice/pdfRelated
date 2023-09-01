from PyPDF2 import PdfWriter, PdfReader, Transformation

import reportlab
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

def save(reader, file_name):
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with open(file_name, "wb") as f:
        writer.write(f)

def createPagePdf(num, tmp):
    c = canvas.Canvas(tmp)
    for i in range(1,num+1): 
        c.drawString((210//2)*mm, (4)*mm, str(i))
        c.showPage()
    c.save()
    return 

def combine(reader):
    reader_page = PdfReader("page.pdf")
    writer = PdfWriter()
    for i in range(len(reader.pages)):
        reader.pages[i].merge_page(reader_page.pages[i])
        writer.add_page(reader.pages[i])
    with open("combine.pdf", "wb") as fp:
        writer.write(fp)

def test_rotate():
    reader = PdfReader("origin.pdf")
    right = reader.pages[0].mediabox.right
    top = reader.pages[0].mediabox.top
    reader.pages[0].rotate(180)
    reader.pages[2].rotate(180)
    op = Transformation()
    op = op.translate(tx = 0 - (int)(right/2), ty = 0 - (int)(top/2))
    reader.pages[0].add_transformation(op)
    save(reader, "2.pdf")
    op = Transformation().rotate(180)
    reader.pages[0].add_transformation(op)
    save(reader, "3.pdf")
    op = Transformation().translate(tx = 0 + (int)(right/2), ty = 0 + (int)(top/2))
    reader.pages[0].add_transformation(op)
    save(reader, "4.pdf")

    # op = op.translate(tx = 0 - (int)(right/2), ty = 0 - (int)(top/2)).rotate(180).translate(tx = (int)(right/2), ty = (int)(top/2))
    # reader.pages[0].rotate(180)
    # reader.pages[2].rotate(180)

if __name__ == "__main__":
    test_rotate()