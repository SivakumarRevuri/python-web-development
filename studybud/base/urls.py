from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.hello_world, name='hello_world'),
    path('room/<str:pk>/', views.room, name='room'),
    
    path('create_room/', views.create_room, name = 'create_room'),
]
