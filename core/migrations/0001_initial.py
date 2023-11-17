# Generated by Django 4.1.13 on 2023-11-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='cpf')),
                ('telefone', models.CharField(max_length=11, verbose_name='telefone')),
                ('endereco', models.CharField(max_length=50, verbose_name='endereco')),
                ('email', models.CharField(max_length=30, verbose_name='email')),
                ('senha', models.CharField(max_length=15, verbose_name='senha')),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14, verbose_name='cnpj')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('telefone', models.CharField(max_length=11, verbose_name='telefone')),
            ],
        ),
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, verbose_name='email')),
                ('senha', models.CharField(max_length=15, verbose_name='email')),
            ],
        ),
    ]
