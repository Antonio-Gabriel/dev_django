from django.shortcuts import redirect, render, HttpResponse
from django_app.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    #evento = Evento.objects.all()

    # Filter with current user
    usuario = request.user
    evento_of_user = Evento.objects.filter(usuario=usuario)

    return render(request, 'pages/home.html', {
        "evento": evento_of_user
    })

def hello(request, name, age):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(name, age))

def sum_values(request, first: int, last: int) -> HttpResponse:
    return HttpResponse(f'<h1>{first + last}</h1>')

def evento(request, titulo_evento: str) -> HttpResponse:
    return HttpResponse(f'<h1>{Evento.objects.get(titulo=titulo_evento.capitalize())}</h1>')

def create_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        usuario = request.user

        if Evento.objects.create(
                titulo=titulo, 
                descricao=descricao, 
                data_evento=data_evento, 
                usuario=usuario):
                            
           messages.error(request, "Evento criado com sucesso")  

    return redirect('/')
            

# def some_query(request, query: str):
#     return redirect('/')

def auth_user(request):
    return render(request, 'pages/login.html')

def auth_user_request(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        is_valid_user = authenticate(username=username, password=password)
        if is_valid_user is not None:
            
            login(request, is_valid_user)
            return redirect('/')
        else:
           messages.error(request, "Usuário ou senha inválidos")  
    
    return redirect('/login/')
    
def logout_user_request(request):
    logout(request)
    return redirect('/')