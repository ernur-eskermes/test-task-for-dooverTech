from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.CartItemAPIView.as_view(),
        name="cart_item_list_create_api"
    ),
    path(
        "<int:pk>/",
        views.CartItemDetailAPIView.as_view(),
        name="cart_item_detail_api"
    ),
]
