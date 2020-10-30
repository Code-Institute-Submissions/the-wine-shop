from decimal import Decimal
from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404


def shoppingbag_contents(request):

    shoppingbag_items = []
    total = 0
    product_count = 0
    shoppingbag = request.session.get('shoppingbag', {})

    for item_id, quantity in shoppingbag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        shoppingbag_items.append({
            'item_id': item_id,
            'product': product,
            'quantity': quantity,
        })

    if total > settings.SUBSCRIPTION_LEVEL and settings.SUBSCRIPTION:
        total = total - Decimal(total * Decimal(settings.SUBSCRIPTION_DISCOUNT / 100))
        delivery = 0
    elif total == 0:
        delivery = 0
    else:
        delivery = 5

    grand_total = delivery + total

    context = {
        'shoppingbag_items': shoppingbag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'subscription_discount': settings.SUBSCRIPTION_DISCOUNT,
        'subscription_level': settings.SUBSCRIPTION_LEVEL,
        'grand_total': grand_total,
        'subscription': settings.SUBSCRIPTION,
    }

    return context
