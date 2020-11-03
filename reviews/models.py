from django.db import models


class Review(models.Model):
    # origin = models.ForeignKey('WineOrigin', null=True, blank=True, on_delete=models.SET_NULL)
    # colour = models.ForeignKey('WineColour', null=True, blank=True, on_delete=models.SET_NULL)
    # name = models.CharField(max_length=50)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    # description = models.TextField()
    # brand = models.CharField(max_length=50, null=True, blank=True)
    # image = models.ImageField(null=True, blank=True)

    title = models.CharField(max_length=20, null=False, blank=False)
    rating = models.IntegerField(range(0, 6), null=False, blank=False)
    review_text = models.CharField(max_length=200, null=False, blank=False)

    # def __str__(self):
    #     return self.name
