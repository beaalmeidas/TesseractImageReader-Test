from django.urls import path
from . import views


urlpatterns = [
    path('', views.extract_img_data, name='home'),
    path('upload-document/', views.extract_img_data, name='upload_document'),
]
