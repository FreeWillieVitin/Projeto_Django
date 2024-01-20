from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def my_view(Request):
    print('Hello Mother')
    return HttpResponse('Blog')
