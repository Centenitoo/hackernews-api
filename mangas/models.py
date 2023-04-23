from django.db import models

# Create your models here.
class Manga(models.Model) :
    titulomanga = models.TextField(default='', blank=False)
    generomanga = models.TextField(default='', blank=False)
    descripcionmanga = models.TextField(default='', blank=False)
    preciomanga = models.IntegerField(default=0)
    escritormanga = models.TextField(default='', blank=False)
    volumenesmanga = models.IntegerField(default=0)
    capitulosmanga = models.IntegerField(default=0)
    ilustradormanga = models.TextField(default='', blank=False)
    editorialmanga = models.TextField(default='', blank=False)
    clasificacionedadmanga = models.IntegerField(default=0)
