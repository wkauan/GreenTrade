# core.forms
from django import forms
from .models import ClienteModel, EmpresaModel, LoginModel
from . import views  # Importe todo o módulo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteModel
        fields = ['nome','cpf','telefone','endereco','email','password']

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = EmpresaModel
        fields = ['nome','cnpj','telefone','endereco','email','senha']

class LoginForm(forms.ModelForm):
    class meta:
        model = LoginModel
        fields=['cpf','senha']
