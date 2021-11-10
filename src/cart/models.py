from django.conf import settings
from django.db import models
from django.db.models.signals import m2m_changed

from course.models import Courses


User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    total = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def total_price(self):
        total = 0
        for cart in self.cart.all():
            print(cart.course.price)
            total += cart.course.price
            self.total = total
            self.save()
        return total
