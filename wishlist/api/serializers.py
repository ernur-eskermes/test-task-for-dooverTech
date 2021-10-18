from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable

from ..models import WishlistItem


class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = (
            'id',
            'product'
        )

    def validate(self, attrs):
        if WishlistItem.objects.filter(
            wishlist__client=self.context['request'].user.client,
            product_id=attrs['product']
        ).exists():
            raise NotAcceptable(
                "You already have this item in your wishlist"
            )
        return attrs
