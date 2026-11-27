from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path(
        'lista/',
        views.lista_equipamentos,
        name='lista_equipamentos'
    ),

    path(
        'novo/',
        views.novo_equipamento,
        name='novo_equipamento'
    ),

    path(
        '<int:id>/editar/',
        views.editar_equipamento,
        name='editar_equipamento'
    ),

    path(
        '<int:id>/excluir/',
        views.excluir_equipamento,
        name='excluir_equipamento'
    ),

    path(
        '<int:id>/',
        views.detalhes_equipamento,
        name='detalhes_equipamento'
    ),
]