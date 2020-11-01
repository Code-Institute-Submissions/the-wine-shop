from django.http import HttpResponse

from .models import Order, OrderContents
from products.models import Product

import json
import time


class StripeWH_Handler:
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic, unknown or unexpected webhook event """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook from stripe """

        intent = event.data.object
        pid = intent.id
        shoppingbag = intent.metadata.shoppingbag
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    forename=shipping_details.name.split(" ")[0],
                    surname=shipping_details.name.split(" ")[1],
                    email__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town__iexact=shipping_details.address.city,
                    address1__iexact=shipping_details.address.line1,
                    address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_shoppingbag=shoppingbag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    forename=shipping_details.name.split(" ")[0],
                    surname=shipping_details.name.split(" ")[1],
                    email=billing_details.email,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town=shipping_details.address.city,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_shoppingbag=shoppingbag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(shoppingbag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderContents(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook from stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
