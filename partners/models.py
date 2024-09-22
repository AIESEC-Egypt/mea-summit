from django.db import models
from django.utils import timezone

# Create your models here.



class Partner(models.Model):
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    company_name = models.CharField(max_length=255)
    company_field = models.CharField(max_length=255)
    company_size = models.CharField(max_length=255)
    company_website = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)
    why = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_mail = models.EmailField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    contact_position = models.CharField(max_length=255)
    country_code2 = models.CharField(max_length=3,default=+20)  # Adjust max_length if needed


    def __str__(self):
        return self.company_name