from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Create your models here.
class Musica(models.Model):
    titulo = models.TextField(default='',blank=False)
    duracion =  models.IntegerField(default=0, blank=False)
    lanzamiento = models.TextField(default=' ', blank=False)
    autor = models.TextField(default='',blank=False)
    clasificacion =  models.IntegerField(default=0, blank=False)
    pais = models.TextField(default='',blank=False)
    genero = models.TextField(default='',blank=False)
    album = models.TextField(default='', blank=False)
    disponible_Spotify = models.TextField(default='', blank=False)
    precio = models.FloatField(default=0, blank=False)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    music = models.ForeignKey('Music.Musica', related_name='Music', on_delete=models.CASCADE)
