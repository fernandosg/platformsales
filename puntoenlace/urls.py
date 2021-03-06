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
from puntoenlace.views import (IndexView,Crear,EditarView)
from django.contrib.auth.decorators import login_required
app_name="puntoenlace"
urlpatterns = [
    path("",login_required(IndexView.as_view()),name="index_puntoenlace"),
    path('crear/', login_required(Crear.as_view()),name="crear_puntoenlnace"),
    path('editar/<pk>/', login_required(EditarView.as_view()),name="editar_puntoenlnace")
]
