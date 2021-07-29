# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('theme', views.theme, name='theme'),
    path('animals', views.animals, name='animals'),
    path('random', views.random, name='random'),
    path('structures', views.structures, name='structures'),
    path('result', views.result, name='result'),
    path('v2', views.v2, name='v2'),
    path('<str:room_name>/', views.room, name='room'),

]
