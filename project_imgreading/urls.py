from django.contrib import admin
from django.urls import path, include
from app_imgreading import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_imgreading.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ^^^^ This points to where django should send the image to be stored
