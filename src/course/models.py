from django.db import models
from django.urls import reverse


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

    def get_add_to_cart_url(self):
        return reverse("cart:add-to-cart", kwargs={
            'pk': self.pk
        })

    def get_course_details(self):
        return reverse('user:course-details', kwargs={'pk': self.pk})


class CourseContent(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default=False)
    video = models.FileField(upload_to='video/%Y', blank=True, null=True)
