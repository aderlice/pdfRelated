# https://pypdf2.readthedocs.io/en/3.0.0/user/cropping-and-transforming.html

from PyPDF2 import PdfWriter, PdfReader, Transformation

scale_size = 0.7

reader_base = PdfReader("origin.pdf")
writer = PdfWriter()

for page_base in reader_base.pages:
    # op = Transformation().scale(sx=0.5, sy=0.5).rotate(90).translate(tx=100, ty=10).rotate(90)
    op = Transformation().scale(sx=scale_size, sy=scale_size).translate(tx=float(page_base.mediabox.right)*(1 - scale_size)/2.0, ty = float(page_base.mediabox.top)*(1 - scale_size)/2.0)
    page_base.add_transformation(op)
    page_base.rotate(90)
    writer.add_page(page_base)


with open("1.pdf", "wb") as fp:
    writer.write(fp)