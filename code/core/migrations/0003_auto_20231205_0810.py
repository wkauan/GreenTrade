# Generated by Django 3.2.19 on 2023-12-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_loginmodel_senha'),
    ]

    operations = [
        migrations.CreateModel(
            name='MongoClienteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('user_type', models.CharField(default='cliente', max_length=10)),
                ('password', models.CharField(max_length=15)),
                ('pontuacao', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metais', models.CharField(max_length=14, verbose_name='metais')),
                ('eletronicos', models.CharField(max_length=14, verbose_name='eletronicos')),
                ('plastico', models.CharField(max_length=14, verbose_name='plastico')),
                ('quantidade', models.CharField(max_length=14, verbose_name='quantidade')),
            ],
        ),
        migrations.CreateModel(
            name='TrocasForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto_macarrao', models.CharField(max_length=14, verbose_name='produto_macarrao')),
                ('produto_frango', models.CharField(max_length=14, verbose_name='produto_frango')),
                ('produto_leite', models.CharField(max_length=14, verbose_name='produto_leite')),
                ('produto_requeijao', models.CharField(max_length=14, verbose_name='produto_requeijao')),
                ('quantidade', models.CharField(max_length=14, verbose_name='quantidade')),
            ],
        ),
        migrations.RemoveField(
            model_name='clientemodel',
            name='senha',
        ),
        migrations.RemoveField(
            model_name='loginmodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='loginmodel',
            name='senha',
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='password',
            field=models.CharField(default='temporary_hash', max_length=15, verbose_name='senha'),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='pontuacao',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='user_type',
            field=models.CharField(default='cliente', max_length=10, verbose_name='user_type'),
        ),
        migrations.AddField(
            model_name='empresamodel',
            name='email',
            field=models.CharField(default='temp@example.com', max_length=30, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='empresamodel',
            name='endereco',
            field=models.CharField(default='temp_endereco', max_length=50, verbose_name='endereco'),
        ),
        migrations.AddField(
            model_name='empresamodel',
            name='password',
            field=models.CharField(default='temporary_hash', max_length=15, verbose_name='senha'),
        ),
        migrations.AddField(
            model_name='loginmodel',
            name='cpf',
            field=models.CharField(default='temp_cpf', max_length=11, verbose_name='cpf'),
        ),
        migrations.AddField(
            model_name='loginmodel',
            name='password',
            field=models.CharField(default='temporary_hash', max_length=15, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='cpf',
            field=models.CharField(default='temp_cpf', max_length=11, unique=True, verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='email',
            field=models.CharField(default='temp@example.com', max_length=30, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='clientemodel',
            name='endereco',
            field=models.CharField(default='temp_endereco', max_length=50, verbose_name='endereco'),
        ),
    ]
