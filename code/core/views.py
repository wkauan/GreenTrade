from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ClienteModel,EmpresaModel, LoginModel , ProdutoModel, ProdutoModel
from djongo import models
from .forms import ClienteForm,EmpresaForm, LoginForm , ProdutoForm,TrocasForm
from . import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .mongo_models import MongoClienteModel
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.core.exceptions import MultipleObjectsReturned
from validate_docbr import CPF, CNPJ

# Create your views here.

def index(request):
    return render(request, "index.html")

def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        cpf_validator = CPF()
        if not cpf_validator.validate(form.data['cpf']):
            messages.error(request, 'CPF inválido!')
        elif ClienteModel.objects.filter(cpf=form.data['cpf']).exists():
            messages.error(request, 'Este cliente já foi cadastrado!')
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
        cnpj_validator = CNPJ()
        if not cnpj_validator.validate(form.data['cnpj']):
            messages.error(request, 'CNPJ inválido!')
        elif EmpresaModel.objects.filter(cnpj=form.data['cnpj']).exists():
            messages.error(request, 'Esta empresa já foi cadastrada!')
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
            messages.success(request, 'Cadastro realizado com sucesso!')
            
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
    cpf_usuario = request.user.username
    ccliente = None  # Inicializa ccliente fora do bloco try-except

    # Recupera todos os documentos com o mesmo CPF no MongoDB
    documentos = MongoClienteModel.objects.filter(cpf=cpf_usuario)

    # Soma todos os pontos usando o método aggregate
    total_pontos = documentos.aggregate(Sum('pontuacao'))['pontuacao__sum'] or 0

    try:
        # Tenta obter o objeto ClienteModel
        ccliente =MongoClienteModel.objects.get(cpf=cpf_usuario)
        # Atualiza a pontuação se já existir
        ccliente.pontuacao = total_pontos
        ccliente.save()
    except MongoClienteModel.DoesNotExist:
        # Se não existir, cria um novo
        ccliente = MongoClienteModel.objects.create(cpf=cpf_usuario, pontuacao=total_pontos)
    except MultipleObjectsReturned:
        # Se houver múltiplos objetos, escolha um (pode variar dependendo da lógica do seu aplicativo)
        ccliente = MongoClienteModel.objects.filter(cpf=cpf_usuario).first()

    print(f"Pontuação total do MongoDB: {total_pontos}")

    # Passa ccliente para o contexto ao renderizar a página
    return render(request, 'pontos.html', {'ccliente': ccliente, 'total_pontos':total_pontos})


@login_required(login_url="/login")
def produto(request):
    cpf_usuario = request.user.username
    cclientes = ClienteModel.objects.filter(cpf=cpf_usuario)

    if cclientes.exists():
        ccliente = cclientes.first()  # Pega o primeiro objeto da queryset
        if request.method == 'POST':
            form = ProdutoForm(request.POST)
            tipo_material = form.data['material']
            multiplicador = {'Metais': 30, 'Eletronicos': 20, 'Plastico': 10}

            if tipo_material not in multiplicador:
                messages.error(request, 'Tipo de material inválido!')
                print('Tipo de material inválido!')
            else:
                quantidade = int(form.data['quantidade'])

                # Atualiza a pontuação no modelo do Django
                if ccliente.pontuacao is None:
                    ccliente.pontuacao = 0
                ccliente.pontuacao += quantidade * multiplicador[tipo_material]
                ccliente.save()

                try:
                    # Tenta obter o objeto correspondente no MongoDB
                    cliente_doc = MongoClienteModel.objects.get(cpf=cpf_usuario)
                except MongoClienteModel.MultipleObjectsReturned:
                    # Se houver múltiplos objetos, escolha o primeiro (pode ajustar conforme necessário)
                    cliente_doc = MongoClienteModel.objects.filter(cpf=cpf_usuario).first()
                except MongoClienteModel.DoesNotExist:
                    # Se não existir, cria um novo
                    cliente_doc = MongoClienteModel.objects.create(cpf=cpf_usuario, pontuacao=str(quantidade * multiplicador[tipo_material]))

                # Atualiza a pontuação no modelo do MongoDB
                cliente_doc.pontuacao = str(int(cliente_doc.pontuacao or 0) + quantidade * multiplicador[tipo_material])
                cliente_doc.save()

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




@login_required(login_url="/login")
def trocas(request):
    cpf_usuario = request.user.username
    ccliente = ClienteModel.objects.filter(cpf=cpf_usuario).first()

    if request.method == 'POST':
        multiplicador = {'produto_macarrao': 100, 'produto_frango': 150, 'produto_leite': 40, 'produto_requeijao': 90}

        for produto in ['produto_macarrao', 'produto_frango', 'produto_leite', 'produto_requeijao']:
            quantidade_key = f'quantidade_{produto}'
            if quantidade_key in request.POST:
                try:
                    quantidade = int(request.POST[quantidade_key])
                except ValueError:
                    quantidade = 0  # Ou qualquer valor padrão que faça sentido no seu contexto

                # Atualiza a pontuação no modelo do Django
                if ccliente.pontuacao is None:
                    ccliente.pontuacao = 0
                ccliente.pontuacao -= quantidade * multiplicador[produto]

                # Tenta obter o objeto correspondente no MongoDB
                cliente_doc = MongoClienteModel.objects.filter(cpf=cpf_usuario).first()

                if cliente_doc:
                    # Atualiza a pontuação no modelo do MongoDB
                    cliente_doc.pontuacao = str(int(cliente_doc.pontuacao or 0) - quantidade * multiplicador[produto])
                    cliente_doc.save()
                else:
                    
                    print(f"Documento para cliente {cpf_usuario} não encontrado no MongoDB")

                messages.success(request, 'Troca realizada!')
                print('Troca realizada!')

    return render(request, 'trocas.html')














