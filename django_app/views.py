from django.shortcuts import redirect, render, HttpResponse
from django_app.models import Evento

# Create your views here.
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