from django.urls import path

from index.views import index, item, cancel, success, CreateCheckoutSessionView

urlpatterns = [
    path('', index, name='index'),
    path('item/<id>', item, name='item'),
    path('cancel/', cancel, name='cancel'),
    path('success/', success, name='success'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]