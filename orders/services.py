import braintree
from django.conf import settings

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


def pay_order(amount: str, payment_method_nonce, options: dict):
    result = gateway.transaction.sale({
        'amount': f'{amount:.2f}',
        'payment_method_nonce': payment_method_nonce,
        'options': options
    })
    return result


def get_client_token():
    return gateway.client_token.generate()
