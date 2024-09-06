import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuarios
from hashlib import sha256
from django.contrib import messages


def login(request):
    return render(request, 'login.html')
    
def cadastro(request):
    return render(request, 'cadastro.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    usuarios = Usuarios.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.warning(request, 'Nome e E-mail não podem estar vazios')
        return redirect('/cadastro')
        #return redirect('/cadastro?status=1')
    if len(senha) < 8:
        messages.warning(request, 'Sua senha deve ter pelo menos 8 caracteres')
        return redirect('/cadastro')
        #return redirect('/cadastro?status=2')
    if senha != senha2:
        messages.error(request, 'As senhas são diferentes')
        return redirect('/cadastro')
    if Usuarios.objects.filter(email=email).exists():
        messages.warning(request, 'Usuário já existe')
        return redirect('/cadastro')
        #return redirect('/cadastro?status=3')
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuarios = Usuarios(nome = nome, email = email, senha = senha)
        usuarios.save()
        messages.success(request, 'Cadastro feito com sucesso')
        return redirect('/cadastro')
    except:
        messages.warning(request, 'Erro do sistema')
        return redirect('/cadastro')
        #return redirect('/cadastro?status=4')


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuarios.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        messages.error(request, 'Usuário não encontrado')
        return redirect('/login')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/cadastros/home/')
    
def sair(request):
    request.session.flush()
    return redirect('/login/')