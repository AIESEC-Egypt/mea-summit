from django import forms
from .models import UserRegistration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = [
            'first_name', 'last_name', 'gender','country_code', 
            'whatsapp_number', 'telegram_username', 'country',
            'position', 'aiesec_mail', 'nationality', 'dob', 'image', 'motivation', 'unique_events',
            'experiences', 'expectations', 'allergies','entity','nickname','emergency','lc','expectations_faci','expectations_cc','country_code1',
            'visa','visa_type','assistance','invitation','passport','passport_number','issue','expiry','place','arrival','leaving','passport_image','condition'
        ]
    country_code = forms.CharField(widget=forms.HiddenInput())  # Hidden field for country code
    country_code1 = forms.CharField(widget=forms.HiddenInput())  # Hidden field for country code
