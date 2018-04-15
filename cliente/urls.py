"""platformciber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cliente.views import (Register,IndexView, DetalleClienteView, ExitoRegistro)
from django.contrib.auth.decorators import login_required
app_name="cliente"
urlpatterns = [
    path('create/', login_required(Register.as_view()),name="create_cliente"),
    path("",login_required(IndexView.as_view()),name="index_cliente"),
    path("<pk>",login_required(DetalleClienteView.as_view()),name="detalle_cliente"),
    path("exito/",login_required(ExitoRegistro.as_view()),name="exito_registro")
]
