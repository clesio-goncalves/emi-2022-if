from django.contrib import admin
from apps.aluno.models import Aluno

class ListandoAlunos(admin.ModelAdmin):
    list_display = ("id", "nome", "matricula", "telefone", "status")
    list_display_links = ("matricula", "nome")
    search_fields = ("nome", "matricula")
    list_filter = ("status",)
    list_per_page = 10

admin.site.register(Aluno, ListandoAlunos)
