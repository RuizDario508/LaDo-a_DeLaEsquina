from django.contrib import admin
from django.urls import path, include
from productos import views as productos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', productos_views.home, name='home'),
    path('productos/', include('productos.urls')),
    path('reportes/', include('reportes.urls')),
    path('soporte/', include('soporte.urls')),
    
]

