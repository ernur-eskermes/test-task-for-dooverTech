from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable, PermissionDenied

from products.models import Product
from ..models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            "id",
            "product",
            "quantity"
        )

    def validate(self, attrs):
        request = self.context['request']
        cart = request.user.client.user_cart
        product = get_object_or_404(Product, pk=request.data["product"])

        if CartItem.objects.filter(
                cart=cart,
                product=product
        ).exists():
            raise NotAcceptable(
                "You already have this item in your shopping cart"
            )
        if attrs['quantity'] > product.quantity:
            raise NotAcceptable(
                "You order quantity more than the seller have"
            )
        return attrs


class CartItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'quantity',
        )

    def get_object(self):
        return CartItem.objects.get(
            pk=self.context['request'].parser_context['kwargs']['pk']
        )

    def validate(self, attrs):
        request = self.context['request']
        cart_item = self.get_object()
        cart_item_user_exists = CartItem.objects.filter(
            id=request.parser_context['kwargs']['pk'],
            cart__client=request.user.client
        ).exists()

        if not cart_item_user_exists:
            raise PermissionDenied(
                "Sorry this cart not belong to you"
            )
        if attrs["quantity"] > cart_item.product.quantity:
            raise NotAcceptable(
                "Your order quantity more than the seller have"
            )
        return attrs
