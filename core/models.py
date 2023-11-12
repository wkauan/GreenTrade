from django.db import models

class ClienteModel(models.Model):
    nome = models.CharField('nome', max_length=30)
    cpf = models.CharField('cpf', max_length=11)
    telefone = models.CharField('telefone', max_length=11)
    endereco = models.CharField('endereco', max_length=50)
    email = models.CharField('email', max_length=30)
    senha = models.CharField('senha', max_length=15)

class EmpresaModel(models.Model):
    cnpj = models.CharField('cnpj',max_length=14)
    nome = models.CharField('nome', max_length=30)
    telefone = models.CharField('telefone', max_length=11)

class LoginModel(models.Model):
    email = models.CharField('email', max_length=30)
    senha = models.CharField('email', max_length=15)
