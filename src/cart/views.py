import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from sslcommerz_lib import SSLCOMMERZ


from course.models import Courses
from .models import Cart, Order


@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Courses, pk=pk)
    if request.user.is_authenticated:
        order_item, created = Cart.objects.get_or_create(
            course=item,
            user=request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.cart.filter(course__pk=item.pk).exists():
                return redirect("cart:order-summary")
            else:
                order.cart.add(order_item)
                return redirect("cart:order-summary")
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(
                user=request.user, ordered_date=ordered_date)
            order.cart.add(order_item)
            return redirect("cart:order-summary")
    else:
        return redirect('/accounts/login/')


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            cart = Cart.objects.filter(user=self.request.user, ordered=False)
            order = Order.objects.filter(
                user=self.request.user, ordered=False).first()
            context = {
                'object': cart,
                'order': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            return redirect("/")


class SslCommerzTest(View):

    def post(self, request, *args, **kwargs):

        user = request.user
        print(user)
        order_qs = Order.objects.filter(user=user, ordered=False).first()

        order_total = order_qs.total
        print(order_total)

        settings = {'store_id': 'proma6135dc6bc8c18',
                    'store_pass': 'proma6135dc6bc8c18@ssl', 'issandbox': True}
        sslcz = SSLCOMMERZ(settings)
        post_body = {}
        # post_body['user'] = user


def sslcommerz_payment_gateway(request, name, amount):

    settings = {'store_id': 'proma6135dc6bc8c18',
                'store_pass': 'proma6135dc6bc8c18@ssl', 'issandbox': True}

    sslcommez = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = amount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = random.randint(1000, 99000)
    post_body['success_url'] = 'http://127.0.0.1:8000/user/success'
    post_body['fail_url'] = 'http://127.0.0.1:8000/user/faild'
    post_body['cancel_url'] = 'http://127.0.0.1:8000/user/cancel'
    post_body['emi_option'] = 0
    post_body['cus_name'] = name
    post_body['cus_email'] = 'request.data["email"]'
    post_body['cus_phone'] = 'request.data["phone"]'
    post_body['cus_add1'] = 'request.data["address"]'
    post_body['cus_city'] = 'request.data["address"]'
    post_body['cus_country'] = 'Bangladesh'
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    # OPTIONAL PARAMETERS
    post_body['value_a'] = name

    response = sslcommez.createSession(post_body)
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]


def payment(request):
    order_qs = Order.objects.filter(user=request.user, ordered=False).first()
    amount = order_qs.total
    return redirect(sslcommerz_payment_gateway(request, amount))


def donateView(request):
    order_qs = Order.objects.filter(user=request.user, ordered=False).first()
    amount = order_qs.total
    name = 'sohan'
    return redirect(sslcommerz_payment_gateway(request, name, amount))
