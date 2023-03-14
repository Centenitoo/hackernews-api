import graphene

import mangas.schema

class Query(mangas.schema.Query, graphene.ObjectType) :
    pass 

class Mutation(mangas.schema.Mutation, graphene.ObjectType) : 
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
