# core.forms
from django import forms
from .models import ClienteModel, EmpresaModel, LoginModel, ProdutoModel
from . import views  # Importe todo o módulo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteModel
        fields = ['nome','cpf','telefone','endereco','email','password','pontuacao']

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = EmpresaModel
        fields = ['nome','cnpj','telefone','endereco','email','password']

class LoginForm(forms.ModelForm):
    class meta:
        model = LoginModel
        fields=['cpf','password']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = ProdutoModel
        fields=['metais',  'eletronicos','plastico','quantidade']