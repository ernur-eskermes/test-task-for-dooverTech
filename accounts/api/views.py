from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView, ListAPIView
)
from rest_framework.permissions import IsAuthenticated

from products.api.serializers import ProductSerializer
from products.models import Product
from .mixins import OnlyClientMixin
from .serializers import (
    ClientCreateSerializer,
    ClientUpdateSerializer,
    ClientDetailSerializer, UserAddressSerializer
)
from ..models import Client, UserAddress


class ClientCreateAPIView(CreateAPIView):
    serializer_class = ClientCreateSerializer
    queryset = Client.objects.all()


class ClientDetailAPIView(OnlyClientMixin, RetrieveAPIView):
    serializer_class = ClientDetailSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"
    lookup_url_kwarg = "client_id"


class ClientUpdateAPIView(OnlyClientMixin, UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = "client_id"


class ClientDeleteAPIView(OnlyClientMixin, DestroyAPIView):
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"
    lookup_url_kwarg = "client_id"


class ClientProductAPIView(OnlyClientMixin, ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.filter(
            product_order__order__client=self.request.user.client,
            product_order__order__status='paid'
        )
        return qs


class UserAddressCreateAPIView(OnlyClientMixin, CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()

    def perform_create(self, serializer):
        serializer.save(client=self.request.user.client)
