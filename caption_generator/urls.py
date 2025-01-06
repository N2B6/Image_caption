from django.urls import path
from .views import upload_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', upload_image, name='upload_image'),
    path('about/', upload_image, name='about_project'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)