from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ClienteModel,EmpresaModel, LoginModel , ProdutoModel
from .forms import ClienteForm,EmpresaForm, LoginForm , ProdutoForm
from . import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .mongo_models import MongoClienteModel
from django.shortcuts import get_object_or_404

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
            login_django(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    
     return render(request, 'login.html')  


@login_required(login_url="/login")
def pontos(request):
    return render(request, 'index.html')


@login_required(login_url="/login")
def produto(request):
    cpf_usuario = request.user.username
    ccliente = ClienteModel.objects.get(cpf=cpf_usuario)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        tipo_material = form.data['material']
        multiplicador = {'Metais': 2, 'Eletronicos': 3, 'Plastico': 1}

        if tipo_material not in multiplicador:
            messages.error(request, 'Tipo de material inválido!')
            print('Tipo de material inválido!')
        else:
            quantidade = int(form.data['quantidade'])
            
            # Tenta encontrar o documento existente para o cliente no MongoDB
            cliente_doc = get_object_or_404(ClienteModel, cpf=cpf_usuario)
            
            # Atualiza o documento existente no MongoDB
            cliente_doc.pontuacao = (cliente_doc.pontuacao or 0) + quantidade * multiplicador[tipo_material]
            cliente_doc.save()

            # Atualiza a pontuação no modelo do Django
            if ccliente.pontuacao is None:
                ccliente.pontuacao = 0
            ccliente.pontuacao += quantidade * multiplicador[tipo_material]
            ccliente.save()

            messages.success(request, 'Produto cadastrado com sucesso!')
            print('Produto cadastrado com sucesso!')

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

