from django.urls import path
from . import views

urlpatterns = [
    path('', views.reportes_home, name='reportes_home'),
        path('ventas/', views.reporte_ventas, name='reporte_ventas'),
    path('inventario/', views.reporte_inventario, name='reporte_inventario'),
]
