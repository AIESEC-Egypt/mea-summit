from django.contrib import admin
from .models import Partner

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('company_name','company_field','contact_name')
    search_fields = ('company_name',)
    list_filter = ('company_name',)

# Register your models here.
