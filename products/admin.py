from django.contrib import admin
from .models import Product, WineOrigin, WineColour

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display= (
        'name',
        'colour',
        'description',
        'brand',
        'origin',
        'price',
        'image',
    )

    ordering = ('name',)


class WineOriginAdmin(admin.ModelAdmin):
    list_display = (
        'origin',
    )


class WineColourAdmin(admin.ModelAdmin):
    list_display = (
        'colour',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(WineOrigin, WineOriginAdmin)
admin.site.register(WineColour, WineColourAdmin)
