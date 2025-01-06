from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def redirect_to_home(request):
    return redirect('/image_caption/home/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_home), 
    path('image_caption/', include('caption_generator.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)