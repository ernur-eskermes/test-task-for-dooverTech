from django.urls import path

from . import views

urlpatterns = [
    path(
        'create/',
        views.OrderCreateAPIView.as_view(),
        name='order_create_api'
    ),
    path(
        'payment-process/',
        views.PaymentRequestAPIView.as_view(),
        name='payment_process_api'
    )
]
