from django.urls import path
from . import views

urlpatterns = [
    path('', views.soporte_home, name='soporte_home'),
    path('crear_ticket/', views.crear_ticket, name='crear_ticket'),
    path('ver_tickets/', views.ver_tickets, name='ver_tickets'),
]
