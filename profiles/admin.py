from django.contrib import admin
from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display= (
        'default_address1',
        'default_address2',
        'default_town',
        'default_county',
        'default_country',
        'default_postcode',
        'default_phone_number',
    )


admin.site.register(UserProfile, ProfileAdmin)
