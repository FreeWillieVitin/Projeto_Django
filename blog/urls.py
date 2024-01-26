from django.urls import path
# from django.http import HttpResponse
from blog.views import my_view, exemplo, post

app_name = 'blog'

urlpatterns = [
    path('', my_view, name='blog'),
    path('<int:post_id>/', post, name='post'),
    path('exemplo/', exemplo, name='exemplo'),
]
