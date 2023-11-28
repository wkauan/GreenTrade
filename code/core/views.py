from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ClienteModel,EmpresaModel, LoginModel
from .forms import ClienteForm,EmpresaForm, LoginForm
from . import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def index(request):
    return render(request, "index.html")

def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)       
        if ClienteModel.objects.filter(cpf=form.data['cpf']).exists():
            messages.error(request,'Este cliente já foi cadastrado!') 
        elif len(form.data['cpf']) != 11:
             messages.error(request,'O CPF informado é inválido!') 
        else:
            cliente = ClienteModel()
            cliente.cpf = form.data['cpf']
            cliente.nome = form.data['nome']
            cliente.telefone = form.data['telefone']
            cliente.endereco = form.data['endereco']
            cliente.email = form.data['email']
            cliente.password = form.data['password']
            cliente.save()

            cliente = User.objects.create_user(username = form.data['cpf'], password = form.data ['password'])
            cliente.save()
            

                      
    return render(request, 'cadastro.html')


def empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)       
        if EmpresaModel.objects.filter(cnpj=form.data['cnpj']).exists():
            messages.error(request,'Esta empresa já foi cadastrado!') 
        elif len(form.data['cnpj']) != 14:
             messages.error(request,'O CNPJ informado é inválido!') 
        else:
            empresa = EmpresaModel()
            empresa.cnpj = form.data['cnpj']
            empresa.nome = form.data['nome']
            empresa.telefone = form.data['telefone']
            empresa.endereco = form.data['endereco']
            empresa.email = form.data['email']
            empresa.password = form.data['password']
            empresa.save()

            empresa = User.objects.create_user(username = form.data['cnpj'], password = form.data ['password'])
            empresa.save()
            
    return render(request, 'empresa.html')


def login(request):
     if request.method == 'GET':
        return render(request, 'login.html') 
     else:
        username = request.POST.get('cpf')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)
        if user:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    
     return render(request, 'login.html')  

            

    
            
    




def pontos(request):
    if request.user.is_authenticated:
        return render(request, 'pontos.html')
    return render(request, 'index.html')

def produto(request):
    if request.user.is_authenticated:
        return render(request, 'produto.html')
    return render(request, 'index.html')


    

def coleta(request):
    empresas = EmpresaModel.objects.all()
    return render(request, 'coleta.html', {'empresas': empresas})
    

def ticket(request):
    return render(request, 'ticket.html')

def material(request):
    return render(request, 'material.html')

def trocas(request):
    return render(request, 'trocas.html')

