from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    rating = models.IntegerField(range(0, 6), null=False, blank=False)
    review_text = models.CharField(max_length=200, null=False, blank=False)
    product = models.ForeignKey('Product', null=False, blank=False, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
