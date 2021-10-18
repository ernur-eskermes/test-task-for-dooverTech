from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from admintools.models import CoreModel

User = get_user_model()


class Client(CoreModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    phone = PhoneNumberField(
        'Phone number',
        unique=True,
    )
    avatar = models.ImageField(
        upload_to='user/avatar/'
    )
    bonus = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return str(self.user)


class UserAddress(CoreModel):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
    street = models.CharField(
        max_length=255
    )
    city = models.CharField(
        max_length=255
    )
    state = models.CharField(
        max_length=255
    )
    zipcode = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.street

    def get_address(self):
        return "%s, %s, %s %s" % (
            self.street, self.city, self.state, self.zipcode
        )
