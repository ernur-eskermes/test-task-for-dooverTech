from django.http import HttpResponseForbidden
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import WishlistItemSerializer
from ..models import WishlistItem


class WishlistItemAPIView(ListCreateAPIView):
    serializer_class = WishlistItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(wishlist=self.request.user.client.wishlist)

    def get_queryset(self):
        return WishlistItem.objects.filter(
            wishlist__client=self.request.user.client
        )


class WishlistItemDeleteAPIView(DestroyAPIView):
    queryset = WishlistItem.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.wishlist.client != request.user.client:
            return HttpResponseForbidden()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

