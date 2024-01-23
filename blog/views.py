from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.

def my_view(Request):
    print('blog')
    # return HttpResponse('Blog')
    return render(
        Request,
        'blog/index.html'
    )


def exemplo(Request):
    print('Exemplo')
    # return HttpResponse('Blog')
    return render(
        Request,
        'blog/exemplo.html'
    )
