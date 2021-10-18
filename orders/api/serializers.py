from rest_framework import serializers

from ..models import Order, OrderItem


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'shipping_address',
            'bonus_apply',
        )

    def create(self, validated_data):
        client = self.context['request'].user.client
        instance = Order.objects.create(
            client=client,
            shipping_address=validated_data['shipping_address'],
            bonus_apply=validated_data['bonus_apply']
        )
        order_items = [
            OrderItem(
                order=instance,
                product=item.product,
                quantity=item.quantity,
                total=item.get_cost()
            ) for item in client.user_cart.items.all()
        ]
        OrderItem.objects.bulk_create(order_items)
        return instance
