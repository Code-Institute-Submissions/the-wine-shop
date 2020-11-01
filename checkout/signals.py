from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderContents


@receiver(post_save, sender=OrderContents)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total each time a line item is created/updated """

    instance.order.update_total()


@receiver(post_delete, sender=OrderContents)
def update_on_delete(sender, instance, **kwargs):
    """ Update order total each time a line item is deleted """

    instance.order.update_total()
