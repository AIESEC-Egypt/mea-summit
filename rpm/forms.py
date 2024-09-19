from django import forms
from .models import UserRegistration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = [
            'first_name', 'last_name', 'personal_mail', 'gender','country_code', 
            'whatsapp_number', 'telegram_username', 'country',
            'position', 'aiesec_mail', 'nationality', 'dob', 'image', 'motivation', 'unique_events',
            'experiences', 'expectations', 'allergies','entity'
        ]
    country_code = forms.CharField(widget=forms.HiddenInput())  # Hidden field for country code
