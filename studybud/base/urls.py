from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('', views.home, name='home'),
    path('hello', views.hello_world, name='hello_world'),
    path('room/<str:pk>/', views.room, name='room'),
    
    path('create_room/', views.create_room, name = 'create_room'),
    path('update_room/<str:pk>/', views.update_room, name = 'update_room'),
    path('delete_room/<str:pk>/', views.delete_room, name = 'delete_room'),
]
