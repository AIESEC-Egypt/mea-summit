from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin  # used for more control over the user model
import datetime
from django.utils import timezone

# Create your models here.

Nationality_choices = [
    ('Algeria', 'Algeria'),
    ('Bahrain', 'Bahrain'),
    ('Benin', 'Benin'),
]
allergies_choices = [
    ("I don't have any allergies or food preferences", "I don't have any allergies or food preferences"),
    ("Vegetarian", "Vegetarian"),
    ("Vegan", "Vegan"),
    ("Lactose-free", "Lactose-free"),
    ("Gluten-free", "Gluten-free"),
    ("Other", "Other"),
]


class UserRegistration(models.Model):
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    personal_mail = models.EmailField(default='default@example.com')
    whatsapp_number = models.CharField(max_length=50, null=True, blank=True)
    country_code = models.CharField(max_length=3,default=+20)  # Adjust max_length if needed
    telegram_username = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    aiesec_mail = models.EmailField(default='default@aiesec.net')
    position = models.CharField(max_length=50,null=True, blank=True)
    dob = models.DateField(default=datetime.date.today)
    motivation = models.CharField(max_length=250, null=True, blank=True)
    unique_events = models.CharField(max_length=250, null=True, blank=True)
    experiences = models.CharField(max_length=250, null=True, blank=True)
    expectations = models.CharField(max_length=250, null=True, blank=True)
    allergies = models.CharField(max_length=50, choices=allergies_choices, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    entity = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

