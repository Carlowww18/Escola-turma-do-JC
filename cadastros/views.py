from django.shortcuts import render, redirect
from login.models import Usuarios
from . forms import RegisterForm, RegisterAdmin
from django.http import Http404
from django.contrib import messages
from cadastros.models import Aluno
from django.urls import reverse

def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario'])

        return render(request, 'home.html', {'usuario_logado': request.session.get('usuario'),
                                             'usuario_id': usuario})
    else:
        return render(request, 'home.html')
    
def register_aluno(request):
    usuario = Usuarios.objects.get(id = request.session['usuario'])
    register_aluno = request.session.get('register_aluno', None)
    form = RegisterForm(register_aluno)
  
    return render(request, 'register/register_aluno.html',{'usuario_logado': request.session.get('usuario'),
                                                  'usuario_id': usuario,
                                                  'form': form})

def create_aluno(request):
    if not request.POST:
        raise Http404()      
    POST = request.POST
    request.session['register_aluno'] = POST
    form = RegisterForm(request.POST)
    
    idade = request.POST.get('idade')
    email = request.POST.get('email')

    if idade == '':
        return redirect('register_aluno')
    if Aluno.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já cadastrado')
        return redirect('register_aluno')
    else:
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso!')

            del(request.session['register_aluno'])

        else:
            messages.error(request, 'Corrija os campos corretamente')

    return redirect('register_aluno')


def register_admin(request):
    usuario = Usuarios.objects.get(id=request.session['usuario'])
    
    if request.method == 'POST':
        form = RegisterAdmin(request.POST)
        
        cargo = request.POST.get('cargo')
        if not cargo:
            messages.error(request, 'Cargo não pode estar vazio.')
        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'Cadastro realizado com sucesso')
                return redirect('register_admin')
            else:
                messages.error(request, 'Preencha os campos corretamente')
    else:
        form = RegisterAdmin(request.session.get('register_admin', None))
    
    return render(request, 'register/register_admin.html', {
        'usuario_logado': request.session.get('usuario'),
        'usuario_id': usuario,
        'form': form
    })

def boletim(request):
    usuario = Usuarios.objects.get(id=request.session['usuario'])
    aluno = Aluno.objects.all()

    return render(request, 'aluno/boletim.html', {
        'aluno': aluno,
        'usuario_logado': request.session.get('usuario'),
        'usuario_id': usuario,
    })

def update_aluno(request, id):
    usuario = Usuarios.objects.get(id=request.session['usuario'])
    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados atualizados com sucesso')
            return redirect('update_aluno', id=id)
    else:
        form = RegisterForm(instance=aluno)

    return render(request, 'update/update_aluno.html', {
        'aluno': aluno,
        'form': form,
        'usuario_logado': request.session.get('usuario'),
        'usuario_id': usuario,
    })
