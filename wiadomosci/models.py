from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Wiadomosc(models.Model):
    tresc = models.TextField("treść wiadomości")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_d = models.DateTimeField("dodana", default=timezone.now)

    class Meta:
        verbose_name = 'wiadomość'
        verbose_name_plural = 'wiadomości'

    def __str__(self):
        return self.tresc[0:50]

    def wiadomosc_skrot(self):
        return self.tresc[0:40]