
from django.contrib import admin
from django.urls import path, include

from .views import index, instructors, allcourses, feedback, about, students

urlpatterns = [
    path('admin/', admin.site.urls),


    path('', index, name='home'),
    path('instructors', instructors),
    path('allcourses', allcourses),
    path('feedback', feedback),
    path('about', about),
    path('students', students),


    path('accounts/', include('allauth.urls')),
    path('user/', include('accounts.urls', namespace='accounts')),
    path('contact/', include('contact.urls', namespace='contact')),
]
