from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import ReviewSerializer
from ..models import Review


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class ReviewListAPIView(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(
            status='active',
            product_id=self.kwargs['product_id']
        )
