from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


from course.models import Courses

User = settings.AUTH_USER_MODEL


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=200, blank=True, null=True)
    l_name = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    courses = models.ManyToManyField(Courses, blank=True, null=True)

    def __str__(self) -> str:
        if self.f_name:
            return self.f_name
        else:
            return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
