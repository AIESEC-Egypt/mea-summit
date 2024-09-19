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
    gender = graphene.String(required=True)
    PersonalEmail = graphene.String(required=True)
    phone_number = graphene.String(required=True)
    telegram_username = graphene.String(required=True)
    country = graphene.String(required=True)
    nationality = graphene.String(required=True)
    AiesecEmail = graphene.String(required=True)
    Position = graphene.String(required=True)
    dob = graphene.Date(required=True)
    motivation = graphene.String(required=True)
    unique_events = graphene.String(required=True)
    experiences = graphene.String(required=True)
    expectations = graphene.String(required=True)
    allergies = graphene.String(required=True)
    image = Upload(required=True)  # Use Upload for image file uploads
    entity = graphene.String(required=True)


class RegistrationMutation(graphene.Mutation):
    class Arguments:
        input = UserRegistrationInput(required=True)

    user = graphene.Field(UserRegistrationType)

    def mutate(self, info, input):
        # Save the uploaded image file
        image_file = input.image  # `image_file` will be the uploaded file

        # Create a new UserRegistration object with the provided data
        user = UserRegistration(
            
            first_name=input.first_name,
            last_name=input.last_name,
            gender=input.gender,
            PersonalEmail=input.PersonalEmail,
            phone_number=input.phone_number,
            telegram_username=input.telegram_username,
            country=input.country,
            nationality=input.nationality,
            AiesecEmail=input.AiesecEmail,
            Position=input.Position,
            dob=input.dob,
            entity =input.entity,
            motivation=input.motivation,
            unique_events=input.unique_events,
            experiences=input.experiences,
            expectations=input.expectations,
            allergies=input.allergies,
            image=image_file.name  # Store the image filename or handle it as needed
        )
        user.save()

        # Save the file if you want to handle it manually
        with open(f'media/uploads/{image_file.name}', 'wb') as f:
            for chunk in image_file.chunks():
                f.write(chunk)

        return RegistrationMutation(user=user)

class Mutation(graphene.ObjectType):
    create_user_registration = RegistrationMutation.Field()

class Query(graphene.ObjectType):
    all_users = graphene.List(UserRegistrationType)

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
