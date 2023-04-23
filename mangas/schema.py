import graphene
from graphene_django import DjangoObjectType

from .models import Manga

class MangaType(DjangoObjectType) : 
    class Meta :
        model = Manga

class Query(graphene.ObjectType) : 
    mangas = graphene.List(MangaType)
    
    def resolve_mangas(self, info, **kwargs) :
        return Manga.objects.all()

class CreateManga(graphene.Mutation) :
    id = graphene.Int()
    titulomanga = graphene.String()
    generomanga = graphene.String()
    descripcionmanga = graphene.String()
    preciomanga = graphene.Int()
    escritormanga = graphene.String()
    volumenesmanga = graphene.Int()
    capitulosmanga = graphene.Int()
    ilustradormanga = graphene.String()
    editorialmanga = graphene.String()
    clasificacionedadmanga = graphene.Int()
    
    class Arguments : 
        titulomanga = graphene.String()
        generomanga = graphene.String()
        descripcionmanga = graphene.String()
        preciomanga = graphene.Int()
        escritormanga = graphene.String()
        volumenesmanga = graphene.Int()
        capitulosmanga = graphene.Int()
        ilustradormanga = graphene.String()
        editorialmanga = graphene.String()
        clasificacionedadmanga = graphene.Int()
        
    def mutate(self, info, titulomanga, generomanga, descripcionmanga, preciomanga, escritormanga, volumenesmanga, capitulosmanga, ilustradormanga, editorialmanga, clasificacionedadmanga):
        manga = Manga( titulomanga = titulomanga, generomanga = generomanga, descripcionmanga = descripcionmanga, preciomanga = preciomanga, escritormanga = escritormanga, volumenesmanga = volumenesmanga, capitulosmanga= capitulosmanga, ilustradormanga = ilustradormanga, editorialmanga = editorialmanga, clasificacionedadmanga = clasificacionedadmanga)
        manga.save()
        
        return CreateManga(
            id = manga.id,
            titulomanga = manga.titulomanga,
            generomanga = manga.generomanga, 
            descripcionmanga = manga.descripcionmanga,
            preciomanga = manga.preciomanga,
            escritormanga = manga.escritormanga,
            volumenesmanga = manga.volumenesmanga, 
            capitulosmanga = manga.capitulosmanga,
            ilustradormanga = manga.ilustradormanga,
            editorialmanga = manga.editorialmanga,
            clasificacionedadmanga = manga.clasificacionedadmanga
        )
        
class Mutation(graphene.ObjectType) : 
    create_manga = CreateManga.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)