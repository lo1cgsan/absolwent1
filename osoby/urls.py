from django.urls import path

from . import views

app_name='osoby'
urlpatterns = [
    path('', views.lista_osob, name='lista'),
]