from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/',views.cadastro, name='cadastro'),
    path('empresa/', views.empresa, name='empresa'),
    path('login/', views.login, name='login'),
    path('produto/', views.produto, name='produto'),
    path('pontos/', views.pontos, name='pontos'),
]