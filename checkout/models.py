import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from products.models import Product


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    forename = models.CharField(max_length=25, null=False, blank=False)
    surname = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    address1 = models.CharField(max_length=100, null=False, blank=False)
    address2 = models.CharField(max_length=100, null=False, blank=True)
    town = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=40, null=False, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_shoppingbag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """ Creates a random and unique order number using uuid """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Updates the grand total each time a line item is added, including any delivery costs """

        self.order_total = self.lineitems.aggregate(Sum('line_total'))['line_total__sum'] or 0
        if self.order_total > settings.SUBSCRIPTION_LEVEL:
            self.delivery_cost = 0
        else:
            self.delivery_cost = 5
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """ Overrides the original save method to set the order number if it hasn't already been set """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderContents(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ Overrides the original save method to set the line total and update the order total """

        self.line_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Name {self.product.name} on order {self.order.order_number}'
