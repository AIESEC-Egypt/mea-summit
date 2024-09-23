import graphene
import rpm.schema
import partners.schema

class Query(rpm.schema.Query, partners.schema.Query):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass
  
class Mutation(rpm.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)