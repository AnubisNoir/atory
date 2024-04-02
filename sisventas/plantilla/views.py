from django.shortcuts import render


def home (request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def facturas (request):
    return render (request, 'facturas.html' )
def usuarios (request):
    return render (request, 'usuarios.html')
def planes (request):
    return render (request, 'planes.html')
def cliente (request):
    return render (request, 'cliente.html')
