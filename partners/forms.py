from django import forms
from .models import Partner

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['company_name','company_field','company_size','linkedin',
                  'company_website','why','contact_name','contact_mail','country_code2','contact_phone','contact_position']
        
        country_code2 = forms.CharField(widget=forms.HiddenInput())  # Hidden field for country code
