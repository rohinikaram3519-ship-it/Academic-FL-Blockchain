from pdf2image import convert_from_path
import pytesseract

pages = convert_from_path(
    "../certificates/generated/CERT_11391.pdf"
)

text = ""

for page in pages:

    text += pytesseract.image_to_string(page)

print(text)