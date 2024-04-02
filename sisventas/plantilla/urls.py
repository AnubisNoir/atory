from django.urls import path
from . import views

urlpatterns=[
    path('', views.login, name= 'Login'),
    path('home', views.home, name='Home'),
    path('facturas', views.facturas, name='Factura'),
    path('usuarios', views.usuarios, name='Usuario'),
    path('planes', views.planes, name='Plan'),
    path('clientes', views.cliente, name='Cliente'),
    
]