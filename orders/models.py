from datetime import datetime
from decimal import Decimal

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from admintools.models import CoreModel
from bonuses.models import Bonus


class Order(CoreModel):
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('refunded', 'Refunded'),
    )
    status = models.CharField(
        max_length=120,
        choices=STATUS_CHOICES,
        default='created'
    )
    client = models.ForeignKey(
        "accounts.Client",
        on_delete=models.CASCADE,
        related_name="orders"
    )
    shipping_address = models.ForeignKey(
        "accounts.UserAddress",
        related_name='shipping_address',
        on_delete=models.CASCADE
    )
    shipping_total_price = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=5.99
    )
    order_total = models.DecimalField(
        max_digits=50,
        decimal_places=2
    )
    braintree_id = models.CharField(
        max_length=255,
        blank=True
    )
    bonus_apply = models.BooleanField(
        default=False
    )

    def get_bonus(self):
        now = datetime.now()
        bonuses = []
        for item in self.order_items.filter(
                product__product_bonus__valid_from__lte=now,
                product__product_bonus__valid_to__gte=now,
                product__product_bonus__active=True,
        ):
            bonuses.append(item.product.product_bonus.bonus)
        return sum(bonuses)

    def get_total(self):
        total = sum(i.total for i in self.order_items.all())
        return Decimal(total) + Decimal(self.shipping_total_price)

    def __str__(self):
        return str(self.pk)


@receiver(pre_save, sender=Order)
def order_pre_save(sender, instance, *args, **kwargs):
    instance.order_total = instance.get_total()


class OrderItem(CoreModel):
    order = models.ForeignKey(
        Order,
        related_name="order_items",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        "products.Product",
        related_name="product_order",
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        default=1
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return str(self.pk)
