from django.contrib import admin

from app_cursos.models import Estudante, Cursos, Avaliacoes


@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']


@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug']


@admin.register(Avaliacoes)
class AvaliacoesAdmin(admin.ModelAdmin):
    list_display = ['curso', 'avaliacao']
