from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class ClienteManager(BaseUserManager):
    def create_user(self, cpf, password=None, **extra_fields):
        if not cpf:
            raise ValueError('O campo CPF é obrigatório')
        
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, password=None, user_type='cliente', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(cpf, password, user_type=user_type, **extra_fields)

class ClienteModel(AbstractUser):
    cpf = models.CharField('cpf', max_length=11, unique=True)
    nome = models.CharField('nome', max_length=30)
    telefone = models.CharField('telefone', max_length=11)
    endereco = models.CharField('endereco', max_length=50)
    email = models.CharField('email', max_length=30)
    user_type = models.CharField('user_type', max_length=10, default='cliente')
    password = models.CharField('senha', max_length=15)

    objects = ClienteManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['nome', 'telefone', 'endereco', 'email']

    # Adicionando related_name para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='cliente_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='cliente_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )


class EmpresaModel(models.Model):
    cnpj = models.CharField('cnpj',max_length=14)
    nome = models.CharField('nome', max_length=30)
    telefone = models.CharField('telefone', max_length=11)
    endereco = models.CharField('endereco', max_length=50)
    email = models.CharField('email', max_length=30)
    senha = models.CharField('senha', max_length=15)
    
class LoginModel(models.Model):
    cpf = models.CharField('cpf', max_length=11)
    senha = models.CharField('senha', max_length=15)