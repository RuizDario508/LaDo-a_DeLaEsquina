# Estas son las urls generales del proyecto
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path('', include('productos.urls')),
    path('', home, name='home'),
path('productos/', include('productos.urls')),
    path('admin/', admin.site.urls),
    path('reportes/', include('reportes.urls')),
    path('soporte/', include('soporte.urls')),
]
