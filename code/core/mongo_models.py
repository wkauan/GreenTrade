from djongo import models

class MongoClienteModel(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    user_type = models.CharField(max_length=10, default='cliente')
    password = models.CharField(max_length=15)
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
