from django.contrib import admin
from .models import UserRegistration

@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'aiesec_mail', 'position','image')
    search_fields = ('first_name', 'last_name', 'aiesec_mail', 'position')
    list_filter = ('position',)
