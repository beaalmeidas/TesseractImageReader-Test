from django.shortcuts import render
from .forms import Document_Form
from .models import Document_Model
import pytesseract
from PIL import Image


def extract_img_data(request):
    if request.method == 'POST':
        form = Document_Form(request.POST, request.FILES)
        if form.is_valid():
            print("Form data is valid. Now processing...")
            document = form.save()
            
            extracted_data = pytesseract.image_to_string(Image.open(document.image))
            document.extracted_data = extracted_data
            document.save()
            return render(request, 'ocr_result.html', {'document': document})
    else:
        print("Form data not valid, try again.")
        form = Document_Form()
    return render(request, 'upload_document.html', {'form': form})
