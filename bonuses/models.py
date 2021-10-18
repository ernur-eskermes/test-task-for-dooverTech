from django.core.exceptions import ValidationError
from django.db import models

from admintools.models import CoreModel


class Bonus(CoreModel):
    product = models.OneToOneField(
        "products.Product",
        on_delete=models.CASCADE,
        related_name='product_bonus',
    )
    bonus = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = "Bonus"
        verbose_name_plural = "Bonuses"
