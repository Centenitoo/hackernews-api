from django.db import models
from django.utils.timezone import now

# Create your models here.

class Manga(models.Model) :
    titulomanga = models.TextField(default=' ', blank=False)
    generomanga = models.TextField(default=' ', blank=False)
    descripcionmanga = models.TextField(default=' ', blank=False)
    lanzamientomanga = models.DateTimeField(default= now, blank=False)
    escritormanga = models.TextField(default=' ', blank=False)
    volumenesmanga = models.IntegerField(default=0, blank=True)
    capitulosmanga = models.IntegerField(default=0, blank=True)
    ilustradormanga = models.TextField(default=' ', blank=False)
    editorialmanga = models.TextField(default=' ', blank=True)
    clasificacionedadmanga = models.IntegerField(default=0, blank=True)
