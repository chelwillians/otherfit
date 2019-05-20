from django import forms
from website.models import Costumer

class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = [
            'nome_empresa',
            'endereco',
            'telefone',
            'cnpj',
            'desc'
        ]