from django.urls import path
# from django.http import HttpResponse
from home.views import my_home

urlpatterns = [
    path('', my_home),
]
