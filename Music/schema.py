import graphene
from graphene_django import DjangoObjectType
from .models import Musica, Vote
from graphql import GraphQLError
from django.db.models import Q
from users.schema import UserType


class MusicaType(DjangoObjectType):
    class Meta:
        model = Musica

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class Query(graphene.ObjectType):
    musicas = graphene.List(MusicaType, search=graphene.String())
    votes = graphene.List(VoteType)
    
    def resolve_musicas(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(titulo__icontains=search) |
                Q(genero__icontains=search)
            )
            return Musica.objects.filter(filter)
        
        return Musica.objects.all()

    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()

class CreateMusica(graphene.Mutation):
    id = graphene.Int()
    titulo = graphene.String()
    duracion = graphene.Int()
    lanzamiento = graphene.String()
    autor = graphene.String()
    clasificacion = graphene.Int()
    pais = graphene.String()
    genero = graphene.String()
    album = graphene.String()
    disponible_Spotify = graphene.String()
    precio = graphene.Float()
    posted_by = graphene.Field(UserType)

    class Arguments:
        titulo = graphene.String()
        duracion = graphene.Int()
        lanzamiento = graphene.String()
        autor = graphene.String()
        clasificacion = graphene.Int()
        pais = graphene.String()
        genero = graphene.String()
        album = graphene.String()
        disponible_Spotify = graphene.String()
        precio = graphene.Float()

    def mutate(self, info, titulo, duracion, lanzamiento, autor, clasificacion, pais, genero, album, disponible_Spotify, precio):
        user = info.context.user or None
        
        musica = Musica(
            titulo=titulo,
            duracion=duracion,
            lanzamiento=lanzamiento,
            autor=autor,
            clasificacion=clasificacion,
            pais=pais,
            genero=genero,
            album=album,
            disponible_Spotify=disponible_Spotify,
            precio=precio,
            posted_by=user
        )
        musica.save()

        return CreateMusica(
            id=musica.id,
            titulo=musica.titulo,
            duracion=musica.duracion,
            lanzamiento=musica.lanzamiento,
            autor=musica.autor,
            clasificacion=musica.clasificacion,
            pais=musica.pais,
            genero=musica.genero,
            album=musica.album,
            disponible_Spotify=musica.disponible_Spotify,
            precio=musica.precio,
            posted_by=musica.posted_by
        )

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    music = graphene.Field(MusicaType)

    class Arguments:
        musica_id = graphene.Int()

    def mutate(self, info, musica_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('Debes iniciar sesión para votar.')

        music = Musica.objects.filter(id=musica_id).first()
        if not music:
            raise GraphQLError('Canción no válida.')

        Vote.objects.create(
            user=user,
            music=music
        )

        return CreateVote(user=user, music=music)

class Mutation(graphene.ObjectType):
    create_musica = CreateMusica.Field()
    create_link = CreateMusica.Field()
    create_vote = CreateVote.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
