
from django.urls import path
from . import views

urlpatterns = [
    path('', views.greet, name='greet'),
    path('about/', views.about_page, name='blog-about')
]
