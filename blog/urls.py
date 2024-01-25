from django.urls import path
# from django.http import HttpResponse
from blog.views import my_view, exemplo

# app_name = 'blog'

urlpatterns = [
    path('', my_view, name='blog'),
    path('exemplo/', exemplo, name='exemplo'),
]
