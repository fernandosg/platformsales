from django.urls import path
from django.contrib.auth.decorators import login_required
from edificio.views import IndexView, DetalleEdificioView, Register
app_name='edificio'
urlpatterns=[
    path("",login_required(IndexView.as_view()),name="index_edificio"),
    path("crear/",login_required(Register.as_view()),name="crear_edificio"),
    path("editar/<pk>/",login_required(DetalleEdificioView.as_view()),name="editar_edificio")
]
