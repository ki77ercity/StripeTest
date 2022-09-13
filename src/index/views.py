import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from index.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    item = Item.objects.all()
    context = {
        'item': item,
    }
    return render(request, 'index/index.html', context)

def item(request, id):
    item = get_object_or_404(Item, id=id)
    context = {
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        'item': item,
    }
    return render(request, 'index/item.html', context)

def success(request):
    context = {}
    return render(request, 'index/success.html', context)

def cancel(request):
    context = {}
    return render(request, 'index/cancel.html', context)

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000/"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })