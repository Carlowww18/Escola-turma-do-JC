from django.shortcuts import render, redirect
from login.models import Usuarios
from . forms import RegisterForm, RegisterAdmin
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
    register_aluno = request.session.get('register_aluno', None)
    form = RegisterForm(register_aluno)
  
    return render(request, 'register_aluno.html',{'usuario_logado': request.session.get('usuario'),
                                                  'usuario_id': usuario,
                                                  'form': form})

def create_aluno(request):
    if not request.POST:
        raise Http404()      
    POST = request.POST
    request.session['register_aluno'] = POST
    form = RegisterForm(request.POST)
    
    idade = request.POST.get('idade')

    if idade == '':
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
        # Se for uma requisição GET, inicialize o formulário com dados da sessão, se existirem
        form = RegisterAdmin(request.session.get('register_admin', None))
    
    return render(request, 'register_admin.html', {
        'usuario_logado': request.session.get('usuario'),
        'usuario_id': usuario,
        'form': form
    })