from django.db import models


class WineOrigin(models.Model):
    origin = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.origin


class WineColour(models.Model):
    colour = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.colour


class Product(models.Model):
    origin = models.ForeignKey('WineOrigin', null=True, blank=True, on_delete=models.SET_NULL)
    colour = models.ForeignKey('WineColour', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    brand = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
