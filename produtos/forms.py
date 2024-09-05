import re
from django import forms
from django.core.exceptions import ValidationError
from . models import Aluno, Administrador

class RegisterForm(forms.ModelForm):
    nome_completo = forms.CharField(
        label='Nome Completo:',
        required=True,
        widget = forms.TextInput(attrs={
        'placeholder': 'Ex.: John Doe'
    })
    )
    endereco = forms.CharField(
        label='Endereço:',
        required=True,
        widget = forms.TextInput(attrs={
        'placeholder': 'Ex.: Rua pereira, N°15'
    })
    )
    cpf = forms.CharField(
        label='CPF:',
        max_length=14,
        required=True,
        widget = forms.TextInput(attrs={
        'placeholder': 'Ex.:452-565-552-55',
        'id': 'id_cpf',
    })
    )
    telefone = forms.CharField(
        label='Telefone:',
        max_length=15,
        required=True,
        widget = forms.TextInput(attrs={
            'placeholder': 'Ex.:(99)9 8754-8332',
            'id': 'id_telefone',
        })
    )
    data_nascimento = forms.DateField(
        label='Data de nascimento:',
        required=True,
        widget = forms.DateInput(attrs={
            'placeholder': 'Ex.:DD/MM/YYYY',
            'id': 'id_data',
            'onkeypress':'mascaraData(this)',
        })
    )
    sexo = forms.ChoiceField(
        choices=Aluno.sexo_choices,
        label='Sexo:',
        required=True,
        widget = forms.Select()
    )
    email = forms.EmailField(
        label='E-mail:',
        required=True,  
        widget = forms.TextInput(attrs={
            'placeholder': 'Ex.:ricardo@gmail.com',
        })
    )
    matricula = forms.CharField(
        label='Matricula:',
        max_length=15,
        required=True,
        widget = forms.TextInput(attrs={
        'placeholder': 'Ex.:321315856194894',
    })
    )
    class Meta:
        model = Aluno
        fields = {
            'nome_completo',
            'endereco',
            'cpf',
            'telefone',
            'data_nascimento',
            'sexo',
            'email',
            'matricula',
        }

class RegisterAdmin(forms.ModelForm):
    endereco = forms.CharField(
        widget = forms.TextInput(attrs={
            'placeholder': 'Ex:.Rua gonçalves, n°4'
        })
    )
    data_nascimento = forms.DateField(
        label='Data de nascimento:',
        required=True,
        widget = forms.DateInput(attrs={
            'placeholder': 'Ex.:DD/MM/YYYY',
            'id': 'id_data',
            'onkeypress':'mascaraData(this)',
        })
    )
    cpf = forms.CharField(
        label='CPF:',
        max_length=14,
        required=True,
        widget = forms.TextInput(attrs={
        'placeholder': 'Ex.:452-565-552-55',
        'id': 'id_cpf',
    })
    )
    telefone = forms.CharField(
        label='Telefone:',
        max_length=15,
        required=True,
        widget = forms.TextInput(attrs={
            'placeholder': 'Ex.:(99)9 8754-8332',
            'id': 'id_telefone',
        })
    )
    nome = forms.CharField(
        label='Nome:',
        required=True,
        widget = forms.TextInput(attrs={
        'placeholder': 'Ex.: John Doe'
    })
    )
    cargo = forms.CharField(
        label = 'Cargo:',
        required=True,
        widget = forms.TextInput(attrs={
            'placeholder': 'Ex.:Coordenador',
        })
    )
    class Meta:
        model = Administrador
        fields = {
            'nome',
            'cpf',
            'telefone',
            'data_nascimento',  
            'endereco',
            'cargo',
        }