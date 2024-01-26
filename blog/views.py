from django.shortcuts import render
from django.http import HttpResponse, Http404
from blog.data import posts
from typing import Any


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


def post(request: HttpResponse, post_id: int):
    print('post')
    encontrar_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            encontrar_post = post
            break

    if encontrar_post is None:
        raise Http404('Post não existe.')

    contexto2 = {
        # 'text': 'Exemplo',
        'post': encontrar_post,
        'title': str(encontrar_post['id']) + ' - ' + encontrar_post['title']
    }

    return render(
        request,
        'blog/post.html',
        contexto2
    )
