from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from admintools.models import CoreModel


class Review(CoreModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('in_waiting', 'In waiting'),
        ('blocked', 'Blocked'),
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    client = models.ForeignKey(
        "accounts.Client",
        on_delete=models.CASCADE
    )
    rate = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    subject = models.CharField(
        max_length=255,
        blank=True
    )
    text = models.TextField(
        max_length=500,
        blank=True
    )
    block_reason = models.TextField(
        blank=True,
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default='in_waiting',
        max_length=50
    )

    def __str__(self):
        return self.subject
