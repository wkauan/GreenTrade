# utils.py
from django.contrib.auth.hashers import check_password
from .models import ClienteModel

def validar(cpf, senha):
    
    try:
        usuario = ClienteModel.objects.get(cpf=cpf)
        if check_password(senha, usuario.senha):
            print(f"autenticado: {e}")
            return True, usuario
        else:
            return False, None
    except ClienteModel.DoesNotExist:
        print(f"Ocorreu um erro durante a autenticação: {e}")
        return False, None
