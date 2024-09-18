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

    def resolve_all_partners(self, info, **kwargs):
        date_from = kwargs.get('date_from')
        page = kwargs.get('page', 1)
        per_page = kwargs.get('per_page', 10)

        start_index = (page - 1) * per_page
        end_index = start_index + per_page

        if date_from is not None:
            return Partner.objects.filter(created_at__range=(date_from, datetime.datetime.now()))[start_index:end_index]
        else:
            return Partner.objects.all()[start_index:end_index]

    def resolve_partner(self, info, id):
        return Partner.objects.get(pk=id)

schema = graphene.Schema(query=Query, mutation=Mutation)

