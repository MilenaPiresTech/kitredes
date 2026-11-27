from django import forms
from .models import Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = [
            'nome',
            'descricao',
            'quantidade',
            'unidade_medida',
            'imagem',
            'categoria',
        ]

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome do equipamento'
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Descrição do equipamento'
                }
            ),
            'quantidade': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 0
                }
            ),
            'unidade_medida': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'imagem': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome']

        if len(nome.strip()) < 3:
            raise forms.ValidationError(
                'O nome deve possuir pelo menos 3 caracteres.'
            )

        return nome

    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']

        if quantidade < 0:
            raise forms.ValidationError(
                'A quantidade não pode ser negativa.'
            )

        return quantidade