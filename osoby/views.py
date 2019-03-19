from django.shortcuts import render
from django.http import HttpResponse

from osoby.models import Absolwent

def index(request):
    return HttpResponse("<h1>Witaj w Django!</h1>")

def lista_osob(request):
    osoby = Absolwent.objects.all()
    kontekst = {'osoby': osoby}
    return render(request, 'osoby/lista_osob1.html', kontekst)
