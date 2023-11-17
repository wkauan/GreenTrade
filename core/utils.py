
# utils.py
from django.contrib.auth.hashers import check_password
from .models import ClienteModel

def validar(email, senha):
    
    try:
        usuario = ClienteModel.objects.get(email=email)
        if check_password(senha, usuario.senha):
            return True, usuario
        else:
            return False, None
    except ClienteModel.DoesNotExist:
        return False, None
