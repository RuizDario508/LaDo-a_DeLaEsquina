from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Bienvenido a La Doña de la Esquina!")


def dashboard(request):
    contexto = {
        'total_productos': 120,
        'total_ventas_mes': 45320,
        'total_clientes': 87,
        'crecimiento': 12,
    }
    return render(request, 'dashboard.html', contexto)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from django.http import HttpResponse
from django.urls import reverse
def home(request):
    return render(request, 'productos/home.html')
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        imagen = request.FILES.get('imagen')

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            imagen=imagen
        )
        return redirect('/productos/')
    
    return render(request, 'productos/agregar.html')
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')

        if request.FILES.get('imagen'):
            producto.imagen = request.FILES.get('imagen')

        producto.save()
        return redirect('/productos/')
    
    return render(request, 'productos/editar.html', {'producto': producto})
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('/productos/')
    return render(request, 'productos/eliminar.html', {'producto': producto})
