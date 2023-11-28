from django.db import models


class ClienteModel(models.Model):
    cpf = models.CharField('cpf', max_length=11, unique=True)
    nome = models.CharField('nome', max_length=30)
    telefone = models.CharField('telefone', max_length=11)
    endereco = models.CharField('endereco', max_length=50)
    email = models.CharField('email', max_length=30)
    user_type = models.CharField('user_type', max_length=10, default='cliente')
    password = models.CharField('senha', max_length=15)


class EmpresaModel(models.Model):
    cnpj = models.CharField('cnpj',max_length=14)
    nome = models.CharField('nome', max_length=30)
    telefone = models.CharField('telefone', max_length=11)
    endereco = models.CharField('endereco', max_length=50)
    email = models.CharField('email', max_length=30)
    password = models.CharField('senha', max_length=15)
    
class LoginModel(models.Model):
    cpf = models.CharField('cpf', max_length=11)
    password = models.CharField('password', max_length=15)