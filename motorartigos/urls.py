from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('artigo/<int:artigo_id>/', views.artigo, name='artigo'),
]