from django import forms
from .models import Document_Model

class Document_Form(forms.ModelForm):
    class Meta:
        model = Document_Model
        fields = ['image']
