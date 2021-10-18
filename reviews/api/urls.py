from django.urls import path

from . import views

urlpatterns = [
    path(
        '<int:product_id>/',
        views.ReviewListAPIView.as_view(),
        name="review-list"
    ),
    path(
        'create/',
        views.ReviewCreateAPIView.as_view(),
        name="review-create"
    ),
]
