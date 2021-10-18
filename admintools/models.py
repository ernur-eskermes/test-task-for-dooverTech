from django.db import models


class CoreModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True
        ordering = ['-updated']
