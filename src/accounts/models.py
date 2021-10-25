
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    fullname = models.CharField(verbose_name=_(
        "Full name"), max_length=30, help_text=_("Will be shown e.g. when commenting"))

    phone = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['fullname']

    def __str__(self):
        return self.fullname
