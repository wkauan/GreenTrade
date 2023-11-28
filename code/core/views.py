from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ClienteModel,EmpresaModel, LoginModel
from .forms import ClienteForm,EmpresaForm, LoginForm
from . import views


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
            cliente.password = form.data['senha']
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
            empresa.senha = form.data['senha']
            empresa.save()
            
    return render(request, 'empresa.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('cpf_cnpj')
        password = request.POST.get('password')
        User = None
        print(f"Username: {username}")
        print(f"Senha: {password}")
        


        if username is not None:
            if len(username) == 11:
                user = authenticate(request, cpf=username, password = password, user_type = 'cliente')
                
            elif len(username) ==14:
                user = authenticate(request, cnpj=username, password = password, user_type = 'empresa')
            
            if user is not None:
                login(request, user)
                print(f"Usuário autenticado: {user.username} ({user.user_type})")
                if user.user_type == 'cliente':
                    return redirect('index.html')
                elif user.user_type == 'empresa':
                    return redirect('index.html')
            else:
                print("Autenticação falhou.")
                return render(request, 'login.html', {'error':'Credenciais Inválidas'})
        else:
            return render(request, 'login.html', {'error':'Campo CPF/CNPJ não informado'})
            
    return render(request, 'login.html')




def pontos(request):
    return render(request, 'pontos.html')


def produto(request):
    return render(request, 'produto.html')

def coleta(request):
    empresas = EmpresaModel.objects.all()
    return render(request, 'coleta.html', {'empresas': empresas})
    

def ticket(request):
    return render(request, 'ticket.html')

def material(request):
    return render(request, 'material.html')

def trocas(request):
    return render(request, 'trocas.html')

