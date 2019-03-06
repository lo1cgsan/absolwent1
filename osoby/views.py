from django.shortcuts import render
# from django.http import HttpResponse
from osoby.models import Klasa, Absolwent

def index(request):
    return render(request, 'osoby/index.html')

def test(request):
    return HttpResponse("To tylko test")
