import graphene
from rpm.schema import Query as UsersQuery, Mutation as UsersMutation
from partners.schema import Query as PartnersQuery, Mutation as PartnersMutation

class Query(UsersQuery, PartnersQuery, graphene.ObjectType):
    pass

class Mutation(UsersMutation, PartnersMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
