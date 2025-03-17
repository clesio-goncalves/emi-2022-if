from django.urls import path
from apps.aluno.views import index, listar

urlpatterns = [
    path("", index, name="index"),
    path("lista", listar, name="aluno/lista")
]