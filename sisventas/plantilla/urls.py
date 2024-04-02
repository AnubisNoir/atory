from django.urls import path
from . import views

urlpatterns=[
    path('', views.login, name= 'Login'),
    path('home', views.home, name='Home'),
    path('facturas', views.facturas, name='Factura'),

]