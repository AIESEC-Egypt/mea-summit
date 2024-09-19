import graphene
from graphene_django import DjangoObjectType
from .models import Partner
import datetime

class PartnerRegistration(DjangoObjectType):
    class Meta:
        model = Partner
        fields = '__all__'
        created_at = graphene.DateTime()



class PartnerRegistrationInput(graphene.InputObjectType):
    company_name = graphene.String(required=True)
    company_field = graphene.String(required=True)
    company_size = graphene.String(required=True)
    company_website = graphene.String(required=True)
    company_linkedin = graphene.String(required=True)
    why = graphene.String(required=True)
    contact_name = graphene.String(required=True)
    contact_mail = graphene.String(required=True)
    contact_phone = graphene.String(required=True)
    position = graphene.String(required=True)


class PartnerRegistrationMutation(graphene.Mutation):
    class Arguments:
        input = PartnerRegistrationInput(required=True)

    partner = graphene.Field(PartnerRegistration)

    def mutate(self, info, input):

        partner = Partner(
            company_name=input.company_name,
            company_field=input.company_field,
            company_size=input.company_size,
            company_website=input.company_website,
            company_linkedin=input.company_linkedin,
            why=input.why,
            contact_name=input.contact_name,
            contact_mail=input.contact_email,
            contact_phone=input.contact_phone,
            position=input.position
        )
        partner.save()
        return PartnerRegistrationMutation(partner=partner)


class Mutation(graphene.ObjectType):
    create_partner = PartnerRegistrationMutation()


class Query(graphene.ObjectType):
    all_partners = graphene.List(PartnerRegistration)


schema = graphene.Schema(query=Query, mutation=Mutation)

