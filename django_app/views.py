from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, name, age):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(name, age))

def sum_values(request, first: int, last: int) -> HttpResponse:
    return HttpResponse(f'<h1>{first + last}</h1>')