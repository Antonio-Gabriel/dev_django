from django.shortcuts import render, HttpResponse
from django_app.models import Evento

# Create your views here.
def hello(request, name, age):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(name, age))

def sum_values(request, first: int, last: int) -> HttpResponse:
    return HttpResponse(f'<h1>{first + last}</h1>')

def evento(request, titulo_evento: str) -> HttpResponse:
    return HttpResponse(f'<h1>{Evento.objects.get(titulo=titulo_evento.capitalize())}</h1>')