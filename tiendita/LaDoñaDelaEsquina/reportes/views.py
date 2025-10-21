from django.shortcuts import render

def reportes_home(request):
    return render(request, 'reportes/reportes_home.html')

from django.shortcuts import render

def reporte_ventas(request):
    # Puedes reemplazar esto con tu lógica real más adelante
    return render(request, 'reportes/reporte_ventas.html')
from django.shortcuts import render

def reporte_inventario(request):
    # Aquí va la lógica para mostrar el reporte de inventario
    return render(request, 'reportes/reporte_inventario.html')


# Create your views here.
