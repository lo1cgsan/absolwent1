from django.db import models
from django.contrib.auth.models import User

class Klasa(models.Model):
    nazwa = models.CharField("nazwa klasy", max_length=3, default="")
    rok_matury = models.IntegerField("rok matury", default=0)
    rok_naboru = models.IntegerField("rok naboru", default=0)


class Absolwent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    klasa = models.ForeignKey(Klasa, on_delete=models.SET_NULL, blank=True, null=True, related_name="uczniowie")
