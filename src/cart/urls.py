from django.urls import path

from .views import add_to_cart, OrderSummaryView, donateView


app_name = 'cart'

urlpatterns = [
    path('', OrderSummaryView.as_view(), name='order-summary'),
    path('add_to_cart/<pk>', add_to_cart, name='add-to-cart'),
    path('payment-initiate', donateView, name='payment-initiate'),
]
