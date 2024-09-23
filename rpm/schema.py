import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload  # Import the Upload scalar for file uploads
from .models import UserRegistration
import datetime

class UserRegistrationType(DjangoObjectType):
    class Meta:
        model = UserRegistration
        fields = '__all__'
        created_at = graphene.DateTime()

class UserRegistrationInput(graphene.InputObjectType):

    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    nickname = graphene.String(required=True)  # Added nickname as required
    gender = graphene.String(required=True)
    whatsapp_number = graphene.String(required=True)
    telegram_username = graphene.String(required=True)
    country = graphene.String(required=True)
    nationality = graphene.String(required=True)
    aiesec_mail = graphene.String(required=True)
    position = graphene.String(required=True)
    dob = graphene.Date(required=True)
    motivation = graphene.String(required=True)
    unique_events = graphene.String(required=True)
    experiences = graphene.String(required=True)
    expectations = graphene.String(required=True)
    allergies = graphene.String(required=True)  # Update with actual field type if using choices
    image = Upload(required=True)
    entity = graphene.String(required=True)
    emergency = graphene.String(required=True)
    country_code1 = graphene.String(required=True)  # Added country_code1 as required
    visa = graphene.String(required=True)
    visa_type = graphene.String(required=True)
    assistance = graphene.String(required=True)
    invitation = graphene.String(required=True)
    passport = graphene.String(required=True)
    passport_number = graphene.String(required=True)
    issue = graphene.Date(required=True)
    expiry = graphene.Date(required=True)
    arrival = graphene.Date(required=True)
    leaving = graphene.Date(required=True)
    place = graphene.String(required=True)
    passport_image = Upload(required=True)
    condition = graphene.String(required=True)
    expecations_faci = graphene.String(required=True)
    expecations_cc = graphene.String(required=True)



class RegistrationMutation(graphene.Mutation):
    class Arguments:
        input = UserRegistrationInput(required=True)

    user = graphene.Field(UserRegistrationType)

    def mutate(self, info, input):
        # Save the uploaded image file
        passport1 = input.passport_image;  # `image_file` will be the uploaded file
        image_file = input.image;  # `image_file` will be the uploaded file

        # Create a new UserRegistration object with the provided data
        user = UserRegistration(
            first_name=input.first_name,
            last_name=input.last_name,
            nickname=input.nickname,  # Assuming nickname is present in input
            gender=input.gender,
            whatsapp_number=input.whatsapp_number,  # Assuming phone_number is whatsapp number
            telegram_username=input.telegram_username,
            country=input.country,
            nationality=input.nationality,
            aiesec_mail=input.aiesec_mail,  # Use lowercase for consistency
            position=input.Position,
            dob=input.dob,  # Assuming dob format
            entity=input.entity,
            motivation=input.motivation,
            unique_events=input.unique_events,
            experiences=input.experiences,
            expectations=input.expectations,
            allergies=input.allergies,
            # Handle image (adapt based on your image storage mechanism)
            image=image_file.name,  # Example, adjust for your storage logic
            passport_image= passport1.name,
            country_code=input.country_code,  # Assuming country_code1 should be country_code
            country_code1=input.country_code1,  # Assuming country_code1 should be country_code
            visa=input.visa,
            visa_type=input.visa_type,
            assistance=input.assistance,
            invitation=input.invitation,
            passport=input.passport,
            passport_number=input.passport_number,
            issue=input.issue,  # Assuming issue format
            expiry=input.expiry,  # Assuming expiry format
            arrival=input.arrival,  # Assuming arrival format
            leaving=input.leaving,  # Assuming leaving format
            place=input.place,
            condition=input.condition,
            expecations_faci=input.expecations_faci,
            expecations_cc=input.expecations_cc,
        )
        user.save()

        # Save the file if you want to handle it manually
        with open(f'media/uploads/personal/{image_file.name}', 'wb') as f:
            for chunk in image_file.chunks():
                f.write(chunk)
        with open(f'media/uploads/passport/{passport1.name}', 'wb') as f:
            for chunk in passport1.chunks():
                f.write(chunk)
        return RegistrationMutation(user=user)

class Mutation(graphene.ObjectType):
    create_user_registration = RegistrationMutation.Field()

class Query(graphene.ObjectType):
    all_leads = graphene.List(UserRegistrationType, date_from=graphene.String(), page=graphene.Int(), per_page=graphene.Int())

    def resolve_all_users(root, info, **kwargs):
        date_from = kwargs.get('date_from')
        page = kwargs.get('page', 1)
        per_page = kwargs.get('per_page', 10)

        start_index = (page - 1) * per_page
        end_index = start_index + per_page

        if date_from is not None:
            return UserRegistration.objects.filter(created_at__range=(date_from, datetime.datetime.now()))[start_index:end_index]
        else:
            return UserRegistration.objects.all()[start_index:end_index]

schema = graphene.Schema(query=Query, mutation=Mutation)
