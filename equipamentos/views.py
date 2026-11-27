from django.shortcuts import render, redirect, get_object_or_404

from .models import Equipamento
from .forms import EquipamentoForm


def dashboard(request):
    return render(request, 'equipamentos/dashboard.html')


def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()

    return render(
        request,
        'equipamentos/lista.html',
        {'equipamentos': equipamentos}
    )


def novo_equipamento(request):

    if request.method == 'POST':
        form = EquipamentoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_equipamentos')

    else:
        form = EquipamentoForm()

    return render(
        request,
        'equipamentos/formulario.html',
        {
            'form': form,
            'titulo': 'Adicionar equipamento'
        }
    )


def detalhes_equipamento(request, id):

    equipamento = get_object_or_404(
        Equipamento,
        id=id
    )

    return render(
        request,
        'equipamentos/detalhes.html',
        {'equipamento': equipamento}
    )


def editar_equipamento(request, id):

    equipamento = get_object_or_404(
        Equipamento,
        id=id
    )

    if request.method == 'POST':
        form = EquipamentoForm(
            request.POST,
            instance=equipamento
        )

        if form.is_valid():
            form.save()
            return redirect(
                'detalhes_equipamento',
                id=equipamento.id
            )

    else:
        form = EquipamentoForm(
            instance=equipamento
        )

    return render(
        request,
        'equipamentos/formulario.html',
        {
            'form': form,
            'titulo': 'Editar equipamento'
        }
    )


def excluir_equipamento(request, id):

    equipamento = get_object_or_404(
        Equipamento,
        id=id
    )

    if request.method == 'POST':
        equipamento.delete()
        return redirect('lista_equipamentos')

    return render(
        request,
        'equipamentos/excluir.html',
        {'equipamento': equipamento}
    )