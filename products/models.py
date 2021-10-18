from django.db import models

from admintools.models import CoreModel


class Category(CoreModel):
    name = models.CharField(
        max_length=255
    )
    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(CoreModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=255
    )
    description = models.TextField(
        max_length=5000
    )
    quantity = models.IntegerField(
        default=1
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.name
