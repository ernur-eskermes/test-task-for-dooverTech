from django.http import HttpResponseForbidden
from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView, ListCreateAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    CartItemSerializer,
    CartItemDetailSerializer
)
from ..models import CartItem


class CartItemAPIView(ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(cart=self.request.user.client.user_cart)

    def get_queryset(self):
        client = self.request.user.client
        queryset = CartItem.objects.filter(cart__client=client)
        return queryset


class CartItemDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemDetailSerializer
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.cart.client != request.user.client:
            return HttpResponseForbidden()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
