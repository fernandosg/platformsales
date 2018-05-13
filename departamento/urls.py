from django.urls import path
from departamento.views import IndexView, DetalleDepartamentoView, Register, ExitoRegistro
from django.contrib.auth.decorators import login_required
app_name="departamento"
urlpatterns=[
    path("",login_required(IndexView.as_view()),name="index_departamento"),
    path("crear/",login_required(Register.as_view()),name="crear_departamento"),
    path("editar/<pk>/",login_required(DetalleDepartamentoView.as_view()),name="editar_departamento")
]
