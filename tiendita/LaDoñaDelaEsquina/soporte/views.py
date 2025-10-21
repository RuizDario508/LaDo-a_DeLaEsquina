from django.shortcuts import render

def soporte_home(request):
    return render(request, 'soporte/soporte_home.html')

from django.shortcuts import render

def crear_ticket(request):
    return render(request, 'soporte/crear_ticket.html')

from django.shortcuts import render

def ver_tickets(request):
    # Esto puede mostrar una lista de tickets, por ahora solo una plantilla vacía
    return render(request, 'soporte/ver_tickets.html')


# Create your views here.
