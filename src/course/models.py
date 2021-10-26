from django.db import models
from django.urls import reverse

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    thumbnail = models.ImageField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course:details', kwargs={'pk': self.pk})
