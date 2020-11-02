from django.contrib import admin
from .models import Order, OrderContents


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderContents
    readonly_fields = ('line_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_shoppingbag', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'forename', 'surname', 'email',
              'phone', 'address1', 'address2', 'town', 'county', 'country',
              'postcode', 'delivery_cost', 'order_total', 'grand_total',
              'original_shoppingbag', 'stripe_pid')

    list_display = ('order_number', 'date', 'forename', 'surname',
                    'order_total', 'delivery_cost', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
