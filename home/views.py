from django.shortcuts import render
# from django.http import HttpResponse

# Estudar classe de views
# Create your views here.


def my_home(Request):  # Isso é uma função chamada de view
    print('Home')
    # return HttpResponse('<b>HOME</b>')
    contexto = {
        'Texto': 'Estamos na Home',
        'title': 'Home'
    }
    return render(
        Request,
        'home/index.html',
        context=contexto
    )
