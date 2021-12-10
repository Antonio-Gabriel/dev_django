from django.shortcuts import HttpResponse

def user(request) -> HttpResponse:
    return HttpResponse("User Route")
