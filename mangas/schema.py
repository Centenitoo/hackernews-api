import graphene
from graphene_django import DjangoObjectType

from .models import Manga
from users.schema import UserType

from mangas.models import Manga, Vote
from graphql import GraphQLError
from django.db.models import Q

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class MangaType(DjangoObjectType) : 
    class Meta :
        model = Manga

class Query(graphene.ObjectType):
    mangas = graphene.List(MangaType, search=graphene.String())
    votes = graphene.List(VoteType)

    def resolve_mangas(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(titulomanga__icontains=search) |
                Q(generomanga__icontains=search)
            )
            return Manga.objects.filter(filter)

        return Manga.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()


class CreateManga(graphene.Mutation) :
    id = graphene.Int()
    titulomanga = graphene.String()
    generomanga = graphene.String()
    descripcionmanga = graphene.String()
    preciomanga = graphene.String()
    escritormanga = graphene.String()
    volumenesmanga = graphene.Int()
    capitulosmanga = graphene.Int()
    ilustradormanga = graphene.String()
    editorialmanga = graphene.String()
    clasificacionedadmanga = graphene.Int()
    posted_by = graphene.Field(UserType)
    
    class Arguments : 
        titulomanga = graphene.String()
        generomanga = graphene.String()
        descripcionmanga = graphene.String()
        preciomanga = graphene.String()
        escritormanga = graphene.String()
        volumenesmanga = graphene.Int()
        capitulosmanga = graphene.Int()
        ilustradormanga = graphene.String()
        editorialmanga = graphene.String()
        clasificacionedadmanga = graphene.Int()
        
    def mutate(self, info, titulomanga, generomanga, descripcionmanga, preciomanga, escritormanga, volumenesmanga, capitulosmanga, ilustradormanga, editorialmanga, clasificacionedadmanga):
        user = info.context.user or None
        manga = Manga( titulomanga = titulomanga, generomanga = generomanga, descripcionmanga = descripcionmanga, preciomanga = preciomanga, escritormanga = escritormanga, volumenesmanga = volumenesmanga, capitulosmanga= capitulosmanga, ilustradormanga = ilustradormanga, editorialmanga = editorialmanga, clasificacionedadmanga = clasificacionedadmanga, posted_by=user,)
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
            clasificacionedadmanga = manga.clasificacionedadmanga,
            posted_by=manga.posted_by,
        )
        
class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    manga = graphene.Field(MangaType)
    
    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to vote!')


        manga = Manga.objects.filter(id=id).first()
        if not manga:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            manga=manga,
        )

        return CreateVote(user=user, manga=manga)
        
class Mutation(graphene.ObjectType) : 
    create_manga = CreateManga.Field()
    create_vote = CreateVote.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
