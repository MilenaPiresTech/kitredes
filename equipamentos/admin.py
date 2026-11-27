from django.contrib import admin
from .models import Categoria, Equipamento, Kit


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'quantidade')
    list_filter = ('categoria',)
    search_fields = ('nome',)