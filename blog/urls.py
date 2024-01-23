from django.urls import path
# from django.http import HttpResponse
from blog.views import my_view, exemplo

urlpatterns = [
    path('', my_view),
    path('exemplo/', exemplo),
]
