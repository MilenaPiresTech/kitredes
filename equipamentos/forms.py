from django import forms
from .models import Equipamento


class EquipamentoForm(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = ['nome', 'descricao', 'quantidade', 'categoria', 'kits']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do equipamento'
            }),

            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Digite uma descrição'
            }),

            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),

            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),

            'kits': forms.SelectMultiple(attrs={
                'class': 'form-select'
            }),
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome']

        if len(nome.strip()) < 3:
            raise forms.ValidationError(
                'O nome deve ter pelo menos 3 caracteres.'
            )

        return nome

    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']

        if quantidade < 0:
            raise forms.ValidationError(
                'A quantidade não pode ser negativa.'
            )

        return quantidade