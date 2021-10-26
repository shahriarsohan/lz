
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import instructors, allcourses, feedback, about, students

urlpatterns = [
    path('admin/', admin.site.urls),


    # path('', index, name='home'),
    path('instructors', instructors),
    # path('allcourses', allcourses),
    path('feedback', feedback),
    path('about', about),
    path('students', students),


    path('', include('course.urls', namespace='course')),

    path('accounts/', include('allauth.urls')),
    path('user/', include('accounts.urls', namespace='accounts')),
    path('contact/', include('contact.urls', namespace='contact')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
