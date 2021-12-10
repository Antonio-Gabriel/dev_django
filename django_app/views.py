from django.shortcuts import redirect, render, HttpResponse
from django_app.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    evento = Evento.objects.all()

    # Filter with current user
    # usuario = request.user
    # evento_of_user = Evento.objects.filter(user=usuario)

    return render(request, 'pages/home.html', {
        "evento": evento
    })

def hello(request, name, age):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(name, age))

def sum_values(request, first: int, last: int) -> HttpResponse:
    return HttpResponse(f'<h1>{first + last}</h1>')

def evento(request, titulo_evento: str) -> HttpResponse:
    return HttpResponse(f'<h1>{Evento.objects.get(titulo=titulo_evento.capitalize())}</h1>')

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
            return redirect('/login/')    
    else:
        raise Exception("Method is not Post")
        