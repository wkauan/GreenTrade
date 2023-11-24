# backends.py

from django.contrib.auth.backends import ModelBackend
from .models import ClienteModel, EmpresaModel

class CustomBackend(ModelBackend):
    def authenticate(self, request, cpf=None, cnpj=None, password=None, user_type=None, **kwargs):
        if user_type == 'cliente':
            try:
                user = ClienteModel.objects.get(cpf=cpf)
            except ClienteModel.DoesNotExist:
                return None
        elif user_type == 'empresa':
            try:
                user = EmpresaModel.objects.get(cnpj=cnpj)
            except EmpresaModel.DoesNotExist:
                return None
        else:
            return None
        print(f"Autenticando usuário: {user.username} ({user.user_type})")
        print(f"Senha recebida: {password}")
        print(f"Senha armazenada: {user.password}")
     
        if user is not None:
            
            if user is not None and user.check_password(password):
                print("Senha correta.")
                return user
            else:
                print("Senha incorreta.")
        else:
            print("Usuário não encontrado.")

        return None

