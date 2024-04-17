from django.db import models


class Document_Model(models.Model):
    image = models.ImageField(upload_to='documents/')
    extracted_data = models.TextField(blank=True)
