from django.db import models

from admintools.models import CoreModel


class Wishlist(CoreModel):
    client = models.OneToOneField(
        "accounts.Client",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.pk)


class WishlistItem(CoreModel):
    wishlist = models.ForeignKey(
        Wishlist,
        related_name="items",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product",
        related_name="wishlist_product",
        on_delete=models.CASCADE
    )
