"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
# from django.http import HttpResponse
from home.views import my_home
from blog.views import my_view

# HTTP Request <-> HTTP Response
# MVT (MVC)

# Códigos de status HTTP: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status#respostas_de_erro_do_cliente

# Essa função mostra como funciona uma requisição http, ela recebe a requisição do usuário e o servidor retorna algo como resposta
# a aquela requisição, no caso requisitamos acesso a uma view e o servidor retorna uma pagina com o texto 'Hello World'.


# def my_home(Request):  # Isso é uma função chamada de view
#     print('Home')
#     return HttpResponse('HOME')


# def my_view(Request):
#     print('Hello Mother')
#     return HttpResponse('Hello World')


urlpatterns = [
    path('admin/', admin.site.urls),
    # Aninhamento de urls, vincular mais caminhos para a mesma url, include e a url do app
    path('blog/', include('blog.urls')),
    path('', include('home.urls')),

]
