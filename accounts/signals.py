from django.db.models.signals import post_save
from django.dispatch import receiver

from carts.models import Cart
from wishlist.models import Wishlist
from .models import Client


@receiver(post_save, sender=Client)
def create_user_cart(sender, created, instance, *args, **kwargs):
    if created:
        Cart.objects.create(client=instance)
        Wishlist.objects.create(client=instance)
