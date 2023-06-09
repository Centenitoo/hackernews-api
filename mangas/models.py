from django.db import models
from django.conf import settings
# Create your models here.

class Manga(models.Model) :
    titulomanga = models.TextField(default=' ', blank=False)
    generomanga = models.TextField(default=' ', blank=False)
    descripcionmanga = models.TextField(default=' ', blank=False)
    preciomanga = models.TextField(default= '', blank=False)
    escritormanga = models.TextField(default=' ', blank=False)
    volumenesmanga = models.IntegerField(default=0, blank=True)
    capitulosmanga = models.IntegerField(default=0, blank=True)
    ilustradormanga = models.TextField(default=' ', blank=False)
    editorialmanga = models.TextField(default=' ', blank=True)
    clasificacionedadmanga = models.IntegerField(default=0, blank=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    manga = models.ForeignKey('mangas.Manga', related_name='votes', on_delete=models.CASCADE)