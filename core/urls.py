"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_app import views
from django.views.generic import RedirectView
from django_app import routes

urlpatterns = [
    path('', views.index),
    
    path('admin/', admin.site.urls),
    path('hello/<name>/<int:age>', views.hello),
    path('sum/<int:first>/<int:last>', views.sum_values),
    path('user/', routes.user),
    path('evento/<str:titulo_evento>', views.evento),

    path('login/', views.auth_user),
    path('login/auth', views.auth_user_request),
]
