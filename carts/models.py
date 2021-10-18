from django.db.models.signals import pre_save
from django.dispatch import receiver

from admintools.models import CoreModel
from django.db import models


class Cart(CoreModel):
    client = models.OneToOneField(
        "accounts.Client",
        related_name="user_cart",
        on_delete=models.CASCADE
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        blank=True,
        null=True
    )

    def clear(self):
        self.items.all().delete()
        self.total = 0
        self.save()

    def get_total(self):
        return sum(item.get_cost() for item in self.items.all())


class CartItem(CoreModel):
    cart = models.ForeignKey(
        Cart,
        related_name="items",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product",
        related_name="cart_product",
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()

    def get_cost(self):
        return self.product.price * self.quantity


@receiver(pre_save, sender=CartItem)
def pre_save_cart(sender, instance, *args, **kwargs):
    instance.cart.total = instance.cart.get_total()
    instance.cart.save(update_fields=["total"])
