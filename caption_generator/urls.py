from django.urls import path
from .views import upload_image

urlpatterns = [
    path('home/', upload_image, name='upload_image'),
    path('about/', upload_image, name='about_project'),

]
