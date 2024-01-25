from django.shortcuts import render
# from django.http import HttpResponse
from blog.data import posts


# Create your views here.

def my_view(Request):
    print('blog')
    # return HttpResponse('Blog')

    contexto = {
        'text': 'Blog',
        'title': 'Blog',
        'posts': posts
    }

    return render(
        Request,
        'blog/index.html',
        contexto
    )


def exemplo(Request):
    print('Exemplo')
    # return HttpResponse('Blog')

    contexto1 = {
        'text': 'Exemplo',
        'title': 'Exemplo'
    }

    return render(
        Request,
        'blog/exemplo.html',
        contexto1
    )
