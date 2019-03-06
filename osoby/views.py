from django.shortcuts import render
from django.http import HttpResponse
from osoby.models import Klasa, Absolwent

def index(request):
    return render(request, 'osoby/index.html')

def test(request):
    return HttpResponse("To tylko test")


def lista(request):
    # https: // docs.djangoproject.com / en / 2.1 / topics / db / queries /
    osoby = Absolwent.objects.all()
    context = {'osoby': osoby}
    return render(request, 'osoby/osoby_lista.html', context)
