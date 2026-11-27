from django.contrib import admin
from .models import Categoria, Equipamento, Kit, ItemKit, Atividade, Etapa


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'categoria',
        'quantidade',
        'unidade_medida',
    )
    list_filter = ('categoria', 'unidade_medida')
    search_fields = ('nome', 'descricao')


class ItemKitInline(admin.TabularInline):
    model = ItemKit
    extra = 1


@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    search_fields = ('nome', 'descricao')
    inlines = [ItemKitInline]


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'kit', 'organizacao')
    list_filter = ('kit',)
    search_fields = ('titulo', 'objetivo', 'descricao')


@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'atividade', 'ordem')
    list_filter = ('atividade',)
    search_fields = ('titulo', 'descricao')