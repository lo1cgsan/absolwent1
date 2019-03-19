from django.shortcuts import render

from wiadomosci.models import Wiadomosc

def lista_wiadomosci(request):
    wiadomosci = Wiadomosc.objects.all()
    kontekst = {'wiadomosci': wiadomosci}
    return render(request, 'wiadomosci/lista_wiadomosci1.html', kontekst)
