from rest_framework import serializers

from ..models import Review
from orders.models import Order


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'rate',
            'subject',
            'text',
            'product',
            'client',
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'client': {'read_only': True},
        }

    def validate(self, attrs):
        user = self.context['request'].user
        if not Order.objects.filter(
            client=user.client,
            status='shipped',
            order_items__product_id=attrs['product']
        ).exists():
            raise serializers.ValidationError(
                "You didn't buy this product"
            )
        return attrs
