from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.WishlistItemAPIView.as_view(),
        name='wishlist_list_create_api'
    ),
    path(
        '<int:pk>/',
        views.WishlistItemDeleteAPIView.as_view(),
        name='wishlist_api'
    )
]
