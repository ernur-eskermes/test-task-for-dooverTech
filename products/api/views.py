from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from .serializers import ProductSerializer, ProductDetailSerializer
from ..models import Product


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
