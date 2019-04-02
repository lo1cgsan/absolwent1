from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from wiadomosci.models import Wiadomosc
from wiadomosci.forms import WiadomoscForm
from django.contrib.auth.decorators import login_required

def lista_wiadomosci(request):
    wiadomosci = Wiadomosc.objects.all()
    kontekst = {'wiadomosci': wiadomosci}
    return render(request, 'wiadomosci/lista_wiadomosci2.html', kontekst)


@login_required()
def dodaj_wiadomosc(request):
    if request.method == 'POST':
        form = WiadomoscForm(request.POST)
        if form.is_valid():
            tresc = form.cleaned_data['tresc']
            data = form.cleaned_data['data_d']
            w = Wiadomosc(tresc=tresc, autor=request.user, data_d=data)
            w.save()
            messages.success(request, "Dodano nową wiadomość!")
            return redirect(reverse('wiadomosci:lista'))
    else:
        form = WiadomoscForm()
    return render(request, 'wiadomosci/dodaj_wiadomosc1.html', {'form': form})

