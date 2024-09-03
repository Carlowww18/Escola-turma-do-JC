from django.shortcuts import render, redirect
from login.models import Usuarios
from . forms import RegisterForm
from django.http import Http404
from django.contrib import messages

def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario'])

        return render(request, 'home.html', {'usuario_logado': request.session.get('usuario'),
                                             'usuario_id': usuario})
    else:
        return render(request, 'home.html')
    
def register_aluno(request):
    usuario = Usuarios.objects.get(id = request.session['usuario'])
    register = request.session.get('register', None)
    form = RegisterForm(register)
  
    return render(request, 'register_aluno.html',{'usuario_logado': request.session.get('usuario'),
                                                  'usuario_id': usuario,
                                                  'form': form})


def register_admin(request):
    return render(request, 'register_admin.html')


def register_create(request):
    if not request.POST:
        raise Http404()      
    POST = request.POST
    request.session['register'] = POST
    form = RegisterForm(request.POST)
    
    idade = request.POST.get('idade')

    if idade == '':
        return redirect('register')
    else:
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso!')

            del(request.session['register'])

        else:
            messages.error(request, 'Corrija os campos inválidos')

    return redirect('register')