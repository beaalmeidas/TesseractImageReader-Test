import pytesseract
from PIL import Image


# Only works for images added through code (from the data folder)

img_file = "data/image2.jpeg"

img = Image.open(img_file)

ocr_result = pytesseract.image_to_string(img)

print(ocr_result)