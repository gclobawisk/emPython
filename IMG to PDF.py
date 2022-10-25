import img2pdf
from PIL import Image
import os

img_path = "C:/Users/Gabriel/Desktop/gabigol.jpg"
pdf_path = "C:/Users/Gabriel/Desktop/file.pdf"
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
file.close()
print("Conversão para PDF com sucesso!")