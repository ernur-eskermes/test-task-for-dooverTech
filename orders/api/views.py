from django.db.models import F
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import OrderCreateSerializer
from ..models import Order
from ..services import pay_order, get_client_token


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = self.perform_create(serializer)
        request.session['order_id'] = order.id
        return redirect(reverse('payment_process_api'))

    def perform_create(self, serializer):
        return serializer.save()


class PaymentRequestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        client_token = get_client_token()
        return render(
            request,
            'payment/process.html',
            {'client_token': client_token}
        )

    def post(self, request, *args, **kwargs):
        order = get_object_or_404(Order, id=request.session.get('order_id'))
        client = order.client
        total = order.order_total
        print(1)
        if order.bonus_apply:
            print(12)
            total = total - client.bonus
            if total >= 0:
                client.bonus = 0
            elif total < 0:
                client.bonus = F("bonus") - total
            client.save()
        print(123)
        if total <= 0:
            print(1234)
            order.status = 'paid'
            order.save()
            return Response(
                {"status": "ok"},
                status=status.HTTP_200_OK,
            )
        nonce = request.POST.get('payment_method_nonce', None)
        result = pay_order(
            amount=order.order_total,
            payment_method_nonce=nonce,
            options={'submit_for_settlement': True}
        )
        print(12345)
        if result.is_success:
            order.status = 'paid'
            order.braintree_id = result.transaction.id
            order.save()

            client.bonus = F("bonus") + order.get_bonus()
            client.user_cart.clear()

            return Response(
                {"status": "ok"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"status": "error"},
            status=status.HTTP_400_BAD_REQUEST,
        )
